import telebot

API_TOKEN = '7500598082:AAFvPOUJwU2q6CTT1uowfikE8ZvuKYTVIvw'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я працюю!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
