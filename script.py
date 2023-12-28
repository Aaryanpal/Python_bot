import requests
import os
import telebot
from utils import get_newspaper
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'))

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['daily_newsletter'])
def sign_handler(message):
    text = "This is your Newspaper"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    print(f"000000 for the fetch_newspaper")
    horoscope = get_newspaper(os.getenv('DAILY_NEWSLETTER_API'))
    convey_message = "Daily Newsletter Generating\n"
    method = "sendDocument"
    url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/{method}"
    data = {'chat_id': message.chat.id}
    for date, link in horoscope.items():
        files = {'document': open(link, 'rb')}
        response = requests.post(url, files=files, data=data)
        print(f"000000 for the sign_handler",response.json())

    print(f"This is the response {convey_message}")
    bot.send_message(message.chat.id, convey_message)

@bot.message_handler(commands=['weekly_newsletter'])
def weekly_letter_handler(message):
    bot.send_message(message.chat.id,"Weekly NewsLetter Generating\n")
    print(f"111111 for the fetch_newsletter")
    horoscope = get_newspaper(os.getenv('WEEKLY_NEWSLETTER_API'))
    convey_message = "Weekly Newsletter\n"
    method = "sendDocument"
    url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/{method}"
    data = {'chat_id': message.chat.id}
    for date, link in horoscope.items():
        files = {'document': open(link, 'rb')}
        response = requests.post(url, files=files, data=data)
        print(f"000000 for the sign_handler",response.json())

    print(f"This is the response {convey_message}")
    bot.send_message(message.chat.id, convey_message)

@bot.message_handler(commands=['research_report'])
def research_handler(message):
    bot.send_message(message.chat.id,"Research Report Generating\n")
    horoscope = get_newspaper(os.getenv('RESEARCH_REPORT_API'))
    convey_message = "Research Report\n"
    method = "sendDocument"
    url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/{method}"
    data = {'chat_id': message.chat.id}
    for date, link in horoscope.items():
        files = {'document': open(link, 'rb')}
        response = requests.post(url, files=files, data=data)
        print(f"000000 for the sign_handler",response.json())

    print(f"This is the response {convey_message}")
    bot.send_message(message.chat.id, convey_message)


@bot.message_handler(commands=['weekly_newspaper'])
def weekly_paper_handler(message):
    bot.send_message(message.chat.id,"Weekly Newspaper Generating\n")
    horoscope = get_newspaper(os.getenv('WEEKLY_NEWSPAPER_API'))
    convey_message = "Weekly Newspaper\n"
    method = "sendDocument"
    url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/{method}"
    data = {'chat_id': message.chat.id}
    for date, link in horoscope.items():
        files = {'document': open(link, 'rb')}
        response = requests.post(url, files=files, data=data)
        print(f"000000 for the sign_handler",response.json())

    print(f"This is the response {convey_message}")
    bot.send_message(message.chat.id, convey_message)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
