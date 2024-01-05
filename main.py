import telebot

bot = telebot.TeleBot('6888123864:AAGmaTR-nJA3wZdT3THLrnKUUkfBOlCgINg')

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Hello! Welcome to the bot.')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()