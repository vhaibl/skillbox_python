from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch, Mock

from pony.orm import db_session, rollback
from vk_api.bot_longpoll import VkBotEvent

import handlers
import settings
from bot import Bot
from generate_ticket import generate_ticket


def isolate_db(test_func):
    def wrapper(*args, **kwargs):
        with db_session:
            test_func(*args, **kwargs)
            rollback()

    return wrapper


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
                bot.send_image = Mock()
                bot.run()

                bot.on_event.assert_called()
                bot.on_event.assert_any_call(obj)
                assert bot.on_event.call_count == count

    INPUTS = [
        'Привет',
        '\\ticket',
        'из масквы',
        'из москвы',
        'ландон',
        'лондон',
        '11-01-2020',
        '11-01-2021',
        'asd',
        '666',
        '6',
        '3',
        'коммент',
        '8989',
        'да',
        'email@email.ru',
        '89253263240',
        '23',
        'Василий',
    ]

    @isolate_db
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
            bot.send_image = Mock()

            bot.run()
            EXPECTED_OUTPUTS = [
                settings.DEFAULT_ANSWER,
                settings.SCENARIOS['registration']['steps']['step1']['text'],
                settings.SCENARIOS['registration']['steps']['step1']['failure_text'],
                settings.SCENARIOS['registration']['steps']['step2']['text'],

                settings.SCENARIOS['registration']['steps']['step2']['failure_text'],
                settings.SCENARIOS['registration']['steps']['step3']['text'],
                settings.SCENARIOS['registration']['steps']['step3']['failure_text'],
                settings.SCENARIOS['registration']['steps']['step4']['text'].format(city_from='Москва',
                                                                                    city_to='Лондон',
                                                                                    input_date='11-01-2021',
                                                                                    list=handlers.check_flights(
                                                                                        'Москва', 'Лондон')),
                settings.SCENARIOS['registration']['steps']['step4']['failure_text'],
                settings.SCENARIOS['registration']['steps']['step5']['text'].format(city_from='Москва',
                                                                                    city_to='Лондон',
                                                                                    flight_date='13-12-9666',
                                                                                    flight='666'),
                settings.SCENARIOS['registration']['steps']['step5']['failure_text'],
                settings.SCENARIOS['registration']['steps']['step6']['text'].format(quantity='3'),
                settings.SCENARIOS['registration']['steps']['step7']['text'].format(city_from='Москва',
                                                                                    city_to='Лондон',
                                                                                    flight_date='13-12-9666',
                                                                                    flight='666', quantity='3',
                                                                                    comment='коммент'),
                settings.SCENARIOS['registration']['steps']['step7']['failure_text'],
                settings.SCENARIOS['registration']['steps']['step8']['text'],
                settings.SCENARIOS['registration']['steps']['step8']['failure_text'],
                settings.SCENARIOS['registration']['steps']['step9']['text'],
                settings.SCENARIOS['registration']['steps']['step9']['failure_text'],
                settings.SCENARIOS['registration']['steps']['step10']['text'].format(city_from='Москва',
                                                                                     city_to='Лондон',
                                                                                     flight_date='13-12-9666',
                                                                                     quantity='3', phone='89253263240',
                                                                                     name='Василий'),
            ]

        assert send_mock.call_count == len(self.INPUTS)

        real_outputs = []
        for call in send_mock.call_args_list:
            args, kwargs = call
            real_outputs.append(kwargs['message'])
        assert str(real_outputs) == str(EXPECTED_OUTPUTS)

    def test_image_generation(self):
        with open('files/test_avatar.png', 'rb') as test_avatar:
            avatar_mock = Mock()
            avatar_mock.content = test_avatar.read()

        with patch('requests.get', return_value=avatar_mock):
            ticket_file = generate_ticket('Москва', 'Лондон', 'test', '22-06-2020', 'Василий')
        with open('files/ticket_example.png', 'rb') as expected_file:
            expected_bytes = expected_file.read()
        assert ticket_file.read() == expected_bytes
