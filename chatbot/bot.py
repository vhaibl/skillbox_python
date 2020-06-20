import logging
import random

import requests
import vk_api.bot_longpoll
from pony.orm import db_session
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import handlers
from models import UserState, Registration

try:
    import settings
except ImportError:
    exit('DO cp settings.py.default settings.py and set token and database settings!')
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
        # self.user_states = dict()  # user_id -> UserState

    def run(self):
        """Запуск бота."""
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception:
                log.exception('ошибка в обработке события')

    @db_session
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

        state = UserState.get(user_id=str(user_id))

        if state is not None:
            # continue scenario
            self.continue_scenario(text, state, user_id)

        else:
            # search intent
            for intent in settings.INTENTS:
                log.debug(f'User gets {intent}')
                if any(token in text.lower() for token in intent['tokens']):
                    if intent['answer']:
                        self.send_text(intent['answer'], user_id)

                    else:
                        self.start_scenario(user_id, intent['scenario'], text)
                    break
            else:
                self.send_text(settings.DEFAULT_ANSWER, user_id)

    def send_text(self, text_to_send, user_id):
        """ отправляем сообщение """
        self.api.messages.send(message=text_to_send,
                               random_id=random.randint(0, 2 ** 20),
                               peer_id=user_id)

    def send_image(self, image, user_id):
        """отправляем изображение"""
        upload_url = self.api.photos.getMessagesUploadServer()['upload_url']
        upload_data = requests.post(url=upload_url, files={'photo': ('image.png', image, 'image/png')}).json()
        image_data = self.api.photos.saveMessagesPhoto(**upload_data)

        owner_id = image_data[0]['owner_id']
        media_id = image_data[0]['id']
        attachment = f'photo{owner_id}_{media_id},'
        self.api.messages.send(attachment=attachment,
                               random_id=random.randint(0, 2 ** 20),
                               peer_id=user_id)

    def send_step(self, step, user_id, text, context):
        if 'text' in step:
            self.send_text(step['text'].format(**context), user_id)
        if 'image' in step:
            handler = getattr(handlers, step['image'])
            image = handler(text, context)
            self.send_image(image, user_id)

    def start_scenario(self, user_id, scenario_name, text):
        scenario = settings.SCENARIOS[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        self.send_step(step, user_id, text, context={})
        UserState(user_id=str(user_id), scenario_name=scenario_name, step_name=first_step, context={})

    def continue_scenario(self, text, state, user_id):
        steps = settings.SCENARIOS[state.scenario_name]['steps']
        step = steps[state.step_name]
        handler = getattr(handlers, step['handler'])

        if handler(text=text, context=state.context):
            if state.context['confirm'] == 'No':
                log.info('Отказ от оформления'.format(**state.context))
                text_to_send = 'Отказ от оформления. Введите /ticket чтобы начать заново.'
                self.send_text(text_to_send, user_id)
                state.delete()
                return text_to_send
            next_step = steps[step['next_step']]
            self.send_step(next_step, user_id, text, state.context)
            if next_step['next_step']:
                state.step_name = step['next_step']
                # switch to next step
            else:
                log.info(
                    'Билет из города {city_from} в город {city_to} на дату {flight_date} оформлен, телефон {phone}'.format(
                        **state.context))
                Registration(city_from=state.context['city_from'], city_to=state.context['city_to'],
                             flight_date=state.context['flight_date'], phone=state.context['phone'],
                             quantity=state.context['quantity'], comment=state.context['comment'])
                state.delete()
                # finish scenario

        else:
            if step['failure_step'] == 'step2':
                add_text = None
                if state.context['same']:
                    if state.context['same'] == 'одинаковые города':
                        add_text = 'Ошибка! Нельзя улететь из города {city_from} в город {city_to}. \nВведите /ticket' \
                                   ' чтобы начать заново'
                        text_to_send = add_text.format(**state.context)
                        self.send_text(text_to_send, user_id)

                        state.context['same'] = None
                        log.info('Ошибка! Нельзя улететь из города {city_from} в город {city_to}.'
                                 .format(**state.context))
                        state.delete()

                    elif state.context['same'] == 'нет прямых рейсов':
                        add_text = 'Ошибка! Нет прямых рейсов между городом {city_from} и городом {city_to} \n' \
                                   'Введите /ticket чтобы начать заново'
                        log.info('Ошибка! Нет прямых рейсов между городом {city_from} и городом {city_to}'
                                 .format(**state.context))

                        text_to_send = add_text.format(**state.context)
                        self.send_text(text_to_send, user_id)

                        state.context['same'] = None
                        state.delete()
                    else:
                        text_to_send = step['failure_text'].format(**state.context)
                        self.send_text(text_to_send, user_id)

                else:
                    text_to_send = step['failure_text'].format(**state.context)
                    self.send_text(text_to_send, user_id)

            else:
                text_to_send = step['failure_text'].format(**state.context)
                self.send_text(text_to_send, user_id)


if __name__ == '__main__':
    configure_logging()
    bot = Bot(settings.GROUP_ID, settings.TOKEN1)
    bot.run()
