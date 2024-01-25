import os
import time
from telegram_bot import TelegramBot
from pinger import Pinger

flag = False
host_ip = str(os.getenv("host_ip"))
timeout = int(os.getenv("timeout"))
host_title = os.getenv("host_title")
token = os.getenv("token")
chat_id = os.getenv("chat_id")
host_up_msg = str(os.getenv("host_up_msg"))
host_down_msg = str(os.getenv("host_down_msg"))

def main():
    global flag

    pinger = Pinger(host)
    tgbot = TelegramBot(token, chat_id)

    while True:
        result = pinger.checkHost()

        if result == True and flag == False:
            print(host_up_msg)
            tgbot.sendMessage(host_up_msg)
            flag = True
        elif result == False and flag == True:
            print(host_down_msg)
            tgbot.sendMessage(host_down_msg)
            flag = False

        time.sleep(timeout)

if __name__ == '__main__':
    main()