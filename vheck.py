import telebot
import config
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = telebot.TeleBot(config.key)

def check(user_id):
    statuses = ['member', 'administrator', 'creator']
    member = bot.get_chat_member(chat_id='@tesstssst', user_id=user_id)
    x1 = member.status in statuses
    member = bot.get_chat_member(chat_id='@tesstssst', user_id=user_id)
    x2 = member.status in statuses
    member = bot.get_chat_member(chat_id='@tesstssst', user_id=user_id)
    x3 = member.status in statuses

    print(member.status)
    print(user_id)
    if x1 and x2 and x3:
        return True
    else:
        return False
    