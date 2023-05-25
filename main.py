import time

import telebot

TOKEN = "5678089959:AAFCg7wHG1JGPDeBo_ImzoYSULVn-RYW0rg"

bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, message.text)


@bot.message_handler(commands=['hi'])
def start_message(message):
    bot.reply_to(message, "Топассын ба?")


bot.polling(non_stop=True)
