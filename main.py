from telebot import TeleBot

bot = TeleBot('7528997663:AAHUEL8q67FmsUqbxdj_4z6_458idKzWrb8')


@bot.message_handler(commands=['start'])
def botic(message):
    bot.send_message(message.chat.id, 'Привет, Жми команду /go')


@bot.message_handler(commands=['go'])
def boc(message):
    bot.send_message(message.chat.id, 'Теперь жми команду /echo')


@bot.message_handler(commands=['ssylka'])
def ssylky(message):
    bot.send_message(message.chat.id, 'https://anekdoty.ru/')


@bot.message_handler(commands=['echo'])
def echo(message):
    bot.send_message(message.chat.id, 'Больше ничего не умею. Я только учусь. Жми poca')


@bot.message_handler(commands=['poca'])
def poca(message):
    bot.send_message(message.chat.id, 'Пока, до новых встреч!')


@bot.message_handler(commands=['commands'])
def com(message):
    bot.send_message(message.chat.id, 'Привет, я умею делать всего 5 команд.')
    bot.send_message(message.chat.id, 'Список команд:')
    bot.send_message(message.chat.id, '/start')
    bot.send_message(message.chat.id, '/go')
    bot.send_message(message.chat.id, '/echo')
    bot.send_message(message.chat.id, '/poca')
    bot.send_message(message.chat.id, '/ssylka')


bot.infinity_polling()