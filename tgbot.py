import telebot
from telebot import types
import webbrowser

TOKEN = "6901035613:AAGtNxj7M5mVnTJhU_R0xWpvqRz-hXo8XI0"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["hello"])
def hello(message):
    bot.send_message(message.chat.id, "Привет! Я бот Mary! Поддержу тебя и помогу подготовить к математике!")

@bot.message_handler(commands=["photo"])
def photo(message):
    markup = types.ReplyKeyboardMarkup()
    file = open("photo.jpg", "rb")
    bot.send_photo(message.chat.id, file, reply_markup=markup)


@bot.message_handler(content_types=["photo"])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("У меня тоже много чего есть для тебя! Посмотри смешные видео с котами!", "https://www.youtube.com/channel/UC3rPDWW-3HFRsl0wW6mgaMA"))
    bot.reply_to(message,"Прекрасная фотография!", reply_markup=markup)

@bot.message_handler(commands=["site", "website"])
def site(message):
     webbrowser.open("https://fipi.ru/oge/otkrytyy-bank-zadaniy-oge#!/tab/173942232-2")

@bot.message_handler(commands=["start"])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Хочу потренировать задачи!")
    btn2 = types.KeyboardButton("Где найти больше задач?")
    btn3 = types.KeyboardButton("Мотивационное сообщение")
    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, f'''Привет, {message.from_user.first_name}! 
                                        Я бот <b>{bot.get_me().first_name},</b>''',
                     parse_mode="html", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def pars_text(message):
    if message.text == "Хочу потренировать задачи!":
        inline = types.InlineKeyboardMarkup()
        button_1 = types.InlineKeyboardButton("Задача 8", callback_data="one")
        button_2 = types.InlineKeyboardButton("Задача 10", callback_data="two")
        button_3 = types.InlineKeyboardButton("Задача 15", callback_data="three")
        button_4 = types.InlineKeyboardButton("Задача 19", callback_data="four")
        inline.add(button_1, button_2, button_3, button_4)

        bot.send_message(message.chat.id, "Укажи номер задачи", reply_markup=inline)

    elif message.text == "Где найти больше задач?":
        bot.send_message(message.chat.id,"Напиши: /site. Там задачки из банка ФИПИ")
    elif message.text == "Мотивационное сообщение":

        inline = types.InlineKeyboardMarkup()
        button_1 = types.InlineKeyboardButton("Мне нужна поддержка", callback_data="support")
        button_2 = types.InlineKeyboardButton("Любви!!! ", callback_data="photo")

        inline.add(button_1, button_2)

        bot.send_message(message.chat.id,"Чего ты хочешь?", reply_markup=inline)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "support":
        bot.send_message(call.message.chat.id, "Ты солнышко!У тебя все получится!Я в тебя верю!")

    elif call.data == "photo":
        bot.send_message(call.message.chat.id, "А я тебя люблю :) !!")
    elif call.data == "one":
        bot.send_photo(call.message.chat.id, open("photo8.png", "rb"), caption="После выполнеения, отправь на проверку Марии")
    elif call.data == "two":
        bot.send_photo(call.message.chat.id, open("photo10.png", "rb"),
                       caption="После выполнеения, отправь на проверку Марии")

    elif call.data == "three":
        bot.send_photo(call.message.chat.id, open("photo15.png", "rb"),
                       caption="После выполнеения, отправь на проверку Марии")
    elif call.data == "four":
        bot.send_photo(call.message.chat.id, open("photo19.png", "rb"),
                       caption="После выполнеения, отправь на проверку Марии")



bot.polling(non_stop=True)
