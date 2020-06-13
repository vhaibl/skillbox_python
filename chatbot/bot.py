import random
import logging
import vk_api.bot_longpoll
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import handlers

try:
    import settings
except ImportError:
    exit('DO cp settings.py.default settings.py and set token!')
log = logging.getLogger("bot")


def configure_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    stream_handler.setLevel(logging.INFO)
    log.addHandler(stream_handler)

    file_handler = logging.FileHandler('bot.log', encoding='UTF-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%d-%m-%Y %H:%M'))
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)

    log.setLevel((logging.DEBUG))


class UserState:
    """Состояние пользователя внутри сценария"""

    def __init__(self, scenario_name, step_name, context=None):
        self.scenario_name = scenario_name
        self.step_name = step_name
        self.context = context or {}


class Bot:
    """
    Echo bot for vk.com
    Use Python 3.7
    """

    def __init__(self, group_id, _token1):
        """
        :param group_id: group id из группы Вк
        :param _token1: секретный токен
        """
        self.group_id = settings.GROUP_ID
        self.token = settings.TOKEN1
        self.vk = vk_api.VkApi(token=settings.TOKEN1)
        self.long_poller = VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()
        self.user_states = dict()  # user_id -> UserState

    def run(self):
        """Запуск бота."""
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception:
                log.exception('ошибка в обработке события')

    def on_event(self, event):
        """
        Отправляет сообщение назад, если это текст.
        :param event: VkBotMessageEvent object
        :return: None
        """
        if event.type != VkBotEventType.MESSAGE_NEW:
            log.info('%s не обрабатывается', event.type)
            return
        user_id = event.object.message['peer_id']
        text = event.object.message['text']
        if user_id in self.user_states:
            # continue scenario
            text_to_send = self.continue_scenario(user_id, text)

        else:
            # search intent
            for intent in settings.INTENTS:
                log.debug(f'User gets {intent}')
                if any(token in text.lower() for token in intent['tokens']):
                    if intent['answer']:
                        text_to_send = intent['answer']
                    else:
                        text_to_send = self.start_scenario(user_id, intent['scenario'])
                    break
            else:
                text_to_send = settings.DEFAULT_ANSWER

        self.api.messages.send(message=text_to_send,
                               random_id=random.randint(0, 2 ** 20),
                               peer_id=user_id)

    def start_scenario(self, user_id, scenario_name):
        scenario = settings.SCENARIOS[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        text_to_send = step['text']
        self.user_states[user_id] = UserState(scenario_name=scenario_name, step_name=first_step)
        return text_to_send

    def continue_scenario(self, user_id, text):

        state = self.user_states[user_id]
        steps = settings.SCENARIOS[state.scenario_name]['steps']
        step = steps[state.step_name]
        handler = getattr(handlers, step['handler'])

        if handler(text=text, context=state.context):
            # next step
            if state.context['confirm'] == 'No':
                log.info('Отказ от оформления'.format(**state.context))
                text_to_send = 'Отказ от оформления. Введите \\ticket чтобы начать заново.'
                self.user_states.pop(user_id)
                return text_to_send
            next_step = steps[step['next_step']]
            text_to_send = next_step['text'].format(**state.context)
            if next_step['next_step']:
                state.step_name = step['next_step']
                # switch to next step
            else:
                log.info(
                    'Билет из города {city_from} в город {city_to} на дату {date} оформлен, телефон {phone}'.format(
                        **state.context))
                self.user_states.pop(user_id)
                # finish scenario
            return text_to_send

        else:
            if step['failure_step'] == 'step2':
                add_text = None
                if state.context['same']:
                    if state.context['same'] == 'одинаковые города':
                        add_text = 'Ошибка! Нельзя улететь из города {from} в город {to}. \nВведите \\ticket ' \
                                   'чтобы начать заново'
                        self.user_states.pop(user_id)
                        text_to_send = add_text.format(**state.context)
                        state.context['same'] = None
                        log.info('Ошибка! Нельзя улететь из города {from} в город {to}.'
                                 .format(**state.context))

                    elif state.context['same'] == 'нет прямых рейсов':
                        add_text = 'Ошибка! Нет прямых рейсов между городом {from} и городом {to} \n' \
                                   'Введите \\ticket чтобы начать заново'
                        log.info('Ошибка! Нет прямых рейсов между городом {from} и городом {to}'
                                 .format(**state.context))

                        self.user_states.pop(user_id)
                        text_to_send = add_text.format(**state.context)
                        state.context['same'] = None
                    else:
                        text_to_send = step['failure_text'].format(**state.context)
                else:
                    text_to_send = step['failure_text'].format(**state.context)

            else:
                text_to_send = step['failure_text'].format(**state.context)
        return text_to_send


if __name__ == '__main__':
    configure_logging()
    bot = Bot(settings.GROUP_ID, settings.TOKEN1)
    bot.run()
