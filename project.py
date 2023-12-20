import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot("6219437180:AAHxgZX-RNZ9qBMahofZlfNsjB06KvKOMTE")


@bot.message_handler(commands=["photo"])
def site(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Тыкни, будет весело)', url = 'https://itproger.com'))
    bot.reply_to(message, 'Привет ', reply_markup=markup)


# @bot.message_handler(commands=["start", "main", "привет"])
# def reperater(message):
#     bot.send_message(
#         message.chat.id,
#         f"привет, {message.from_user.first_name} {message.from_user.last_name}",
#     )


# @bot.message_handler(commands=["help"])
# def reperater(message):
#     bot.send_message(
#         message.chat.id, "I <b><u>dont</u></b> help you", parse_mode="html"
#     )


# @bot.message_handler()
# def info(message):
#     if message.text.lower() == "привет":
#         bot.send_message(
#             message.chat.id,
#             f"привет, {message.from_user.first_name} {message.from_user.last_name}",
#         )
#     elif message.text.lower() == "id":
#         bot.reply_to(message, f"ID: {message.from_user.id}")


if __name__ == "__main__":
    bot.infinity_polling()
