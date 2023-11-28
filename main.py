import telebot

bot = telebot.TeleBot('6765528406:AAGDmr541OjewSqfreGj_Pv18le_Gvs4Bww')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Приветик, спасибо что зашел!', parse_mode='Markdown')


@bot.message_handler(commands=['ask questions'])
def main(message):
    bot.send_message(message.chat.id, ' ЙОУ! Как жизнь? Что нового? \nКакая погода на улице?', parse_mode='Markdown')


bot.infinity_polling()