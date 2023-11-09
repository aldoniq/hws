import telebot
import os
from PIL import ImageGrab
from datetime import datetime

bot = telebot.TeleBot("token", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Получить скриншот")
    print(message)
    bot.reply_to(message, "👋 Привеееет", reply_markup=markup)


@bot.message_handler(regexp='получить скриншот')
def screenshot(message):
    path =os.getcwd()+ '/screenshot.png'
    screenshot = ImageGrab.grab()
    screenshot.save(path, 'PNG')
    print("screenshot saved")

    photo = open(path,'rb')
    bot.reply_to(message, f"Taking screenshot {datetime.now()}")
    bot.send_photo(message.chat.id,photo)

	
bot.infinity_polling()

