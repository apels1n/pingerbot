import os
import time
from telegram_bot import TelegramBot
from pinger import Pinger


host_ip = str(os.getenv("host_ip"))
timeout = int(os.getenv("timeout"))
host_title = os.getenv("host_title")
token = os.getenv("token")
chat_id = os.getenv("chat_id")
host_up_msg = str(os.getenv("host_up_msg"))
host_down_msg = str(os.getenv("host_down_msg"))


def main():
    flag = False

    pinger = Pinger(host_ip)
    tgbot = TelegramBot(token, chat_id)

    while True:
        result = pinger.checkHost()

        if result and not flag:
            print(host_up_msg)
            tgbot.sendMessage(host_up_msg)
            flag = not flag
        if not result and flag:
            print(host_down_msg)
            tgbot.sendMessage(host_down_msg)
            flag = not flag

        time.sleep(timeout)


if __name__ == '__main__':
    main()
