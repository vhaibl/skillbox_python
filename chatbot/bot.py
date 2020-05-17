import random
import logging
import vk_api.bot_longpoll
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

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
        if event.type == VkBotEventType.MESSAGE_NEW:
            log.debug("отправляем сообщение назад")
            # print("Новое сообщение:", event.object.message['text'])
            peer_id = event.object.message['peer_id']
            self.api.messages.send(message="Привет! Я пока тупой, но я учусь",
                                   random_id=random.randint(0, 2 ** 20),
                                   peer_id=peer_id)
        else:
            log.info('мы пока не умеем обрабатывать событие такого типа %s', event.type)

    pass


if __name__ == '__main__':
    configure_logging()
    bot = Bot(settings.GROUP_ID, settings.TOKEN1)
    bot.run()
