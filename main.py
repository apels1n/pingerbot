import os
import time
from telegram_bot import TelegramBot
from pinger import Pinger

flag = False
host = str(os.getenv("host"))
timeout = int(os.getenv("timeout"))
host_title = os.getenv("host_title")
token = os.getenv("token")
chat_id = os.getenv("chat_id")
text_variants = [f"✅ Хост {host_title} ({host}) Доступен",
                 f"❌ Хост {host_title} ({host}) Не доступен"]
def main():
    global flag

    pinger = Pinger(host)
    tgbot = TelegramBot(token, chat_id)

    while True:
        result = pinger.checkHost()

        if result == True and flag == False:
            print(text_variants[0])
            tgbot.sendMessage(text_variants[0])
            flag = True
        elif result == False and flag == True:
            print(text_variants[1])
            tgbot.sendMessage(text_variants[1])
            flag = False

        time.sleep(timeout)

if __name__ == '__main__':
    main()