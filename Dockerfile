FROM python:3.10
LABEL authors="apels1n"

RUN mkdir /pingerBot
WORKDIR /pingerBot
COPY main.py /pingerBot/main.py
COPY pinger.py /pingerBot/cuspi.py
COPY telegram_bot.py /pingerBot/teleslave.py
COPY requirements.txt /pingerBot/requirements.txt
RUN apt-get update -y
RUN apt-get install -y iputils-ping
RUN pip install -r /pingerBot/requirements.txt

CMD ["python", "/pingerBot/main.py"]