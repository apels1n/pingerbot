import telebot

class TelegramBot():
    def __init__(self, token, chat_id):
        self.__token = token
        self.__chat_id = chat_id
        self.__bot = telebot.TeleBot(self.__token)

    def sendMessage(self, text):
        self.__bot.send_message(chat_id=self.__chat_id, text=text, )
