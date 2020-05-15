import random

import vk_api.bot_longpoll
from _token import token1


group_id = 195353899

class Bot:
    def __init__(self, group_id, _token1):
        self.group_id = group_id
        self.token = token1
        self.vk = vk_api.VkApi(token=token1)
        self.long_poller = vk_api.bot_longpoll.VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()


    def run(self):
        for event in self.long_poller.listen():
            print ('получено событие')
            try:
                self.on_event(event)
            except Exception as err:
                print(err)

    def on_event(self, event):
        if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:
            print("Новое сообщение:", event.object.message['text'])
            peer_id = event.object.message['peer_id']
            self.api.messages.send(message="Привет! Я пока тупой, но я учусь",
                                   random_id=random.randint(0, 2**20),
                                   peer_id=peer_id)
        else:
            print('мы пока не умеем обрабатывать событие такого типа', event.type)

    pass


if __name__ == '__main__':
    bot = Bot(group_id, token1)
    bot.run()