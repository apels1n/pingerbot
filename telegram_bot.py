import telebot

class TelegramBot():
    def __init__(self, token, chat_id):
        self._token = token
        self._chat_id = chat_id
        self._bot = telebot.TeleBot(token)

    def sendMessage(self, text):
        self._bot.send_message(chat_id=self._chat_id, text=text, )
