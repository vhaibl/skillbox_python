import random
from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch, Mock, ANY

from vk_api.bot_longpoll import VkBotMessageEvent, VkBotEvent

import settings
from bot import Bot


class Test1(TestCase):
    RAW_EVENT = {
        'type': 'message_new', 'object':
            {'message': {'date': 1589810404, 'from_id': 4863211, 'id': 90, 'out': 0, 'peer_id': 4863211,
                         'text': 'привет bot', 'conversation_message_id': 90, 'fwd_messages': [], 'important': False,
                         'random_id': 0, 'attachments': [], 'is_hidden': False}, 'client_info':
                 {'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link'],
                  'keyboard': True, 'inline_keyboard': True, 'lang_id': 0}},
        'group_id': 195353899, 'event_id': '5205a433410d11ef29601d99c9a440259ac19e15'}

    def test_run(self):
        count = 5
        obj = {'a': 1}

        events = [obj] * count
        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock
        with patch("bot.vk_api.VkApi"):
            with patch("bot.VkBotLongPoll", return_value=long_poller_listen_mock):
                bot = Bot('', '')
                bot.on_event = Mock()
                bot.run()

                bot.on_event.assert_called()
                bot.on_event.assert_any_call(obj)
                assert bot.on_event.call_count == count

    # def test_on_event(self):
    #     event = VkBotMessageEvent(raw=self.RAW_EVENT)
    #
    #     send_mock = Mock()
    #     with patch("bot.vk_api.VkApi"):
    #         with patch("bot.VkBotLongPoll"):
    #             bot = Bot('', '')
    #             bot.api = Mock()
    #             bot.api.messages.send = send_mock
    #
    #             bot.on_event(event)
    #
    #     send_mock.assert_called_once_with(message=self.RAW_EVENT['object']['message']['text'],
    #                                       random_id=ANY,
    #                                       peer_id=self.RAW_EVENT['object']['message']['peer_id'])

    INPUTS = [
        'Привет',
        'А когда',
        'Где будет проходить конференция?',
        'Зарегистируй меня',
        'Вениамин',
        'мой адрес email@email',
        'email@email.ru',
    ]

    EXPECTED_OUTPUTS = [
        settings.DEFAULT_ANSWER,
        settings.INTENTS[0]['answer'],
        settings.INTENTS[1]['answer'],
        settings.SCENARIOS['registration']['steps']['step1']['text'],
        settings.SCENARIOS['registration']['steps']['step2']['text'],
        settings.SCENARIOS['registration']['steps']['step2']['failure_text'],
        settings.SCENARIOS['registration']['steps']['step3']['text'].format(name='Вениамин', email='email@email.ru'),
    ]

    def test_run_ok(self):
        send_mock = Mock()
        api_mock = Mock()
        api_mock.messages.send = send_mock

        events = []
        for input_text in self.INPUTS:
            event = deepcopy(self.RAW_EVENT)
            event['object']['message']['text'] = input_text
            events.append(VkBotEvent(event))

        long_poller_mock = Mock()
        long_poller_mock.listen = Mock(return_value=events)

        with patch("bot.VkBotLongPoll", return_value=long_poller_mock):
            bot = Bot('', '')
            bot.api = api_mock
            bot.run()

        assert send_mock.call_count == len(self.INPUTS)

        real_outputs = []
        for call in send_mock.call_args_list:
            args, kwargs = call
            real_outputs.append(kwargs['message'])
        assert real_outputs == self.EXPECTED_OUTPUTS
