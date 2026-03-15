import telebot
import config
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import ai

bot = telebot.TeleBot(config.key)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text="✅Работа", callback_data="btn1")
    btn2 = InlineKeyboardButton(text="✅ОГЭ/ЕГЭ", callback_data="btn2")
    btn3 = InlineKeyboardButton(text="✅Премиум версия", callback_data="btn3")
    keyboard.row_width = 1
    keyboard.add(btn1,btn2,btn3)
    bot.reply_to(message, '''
Привет, это бот который помогает подросткам , найти легкий путь во взрослую жизнь

1.Хочешь найти работу , стажировку или понять кем ты хочешь быть , то нажимай на кнопку ✅Работа 

2.Есть желание подготовится к ОГЭ/ЕГЭ , порешать варианты ближайшего прошедшего года или найти репетитора, то тебе сюда ✅ОГЭ/ЕГЭ 

3.Премимум версия дает тебе множиство полезных роликах о том как : 'доработать свое резюме','как вести себя на собеседование' или же просто как выбрать универ.
И все это только за подписку на несколько каналов если заинтересовало то жми на ✅Премиум версия ''', reply_markup=keyboard)



@bot.callback_query_handler()
def callback(callback):
    if callback.data == "btn1":
        keyboard = InlineKeyboardMarkup()
        btn1_1 = InlineKeyboardButton(text="Найти работу/стажировку", callback_data="btn1_1")
        btn1_2 = InlineKeyboardButton(text='Тест профоринтация', callback_data="btn1_2")
        keyboard.add(btn1_1,btn1_2)
        bot.send_message(callback.message.chat.id,"Выбери нужный вариант чтобы попасть в мир Работы и Стажировок", reply_markup=keyboard)
    elif callback.data == "btn2":
        keyboard = InlineKeyboardMarkup()
        btn2_1 = InlineKeyboardButton(text="Вариант работы ОГЭ/ЕГЭ", callback_data="btn2_1")
        btn2_2 = InlineKeyboardButton(text="Найти репетитора ОГЭ/ЕГЭ", callback_data="btn2_2")
        keyboard.add(btn2_1,btn2_2)
        bot.send_message(callback.message.chat.id,"Выбери нужный вариант чтобы подготовится и сдать экзамен на максимум", reply_markup=keyboard)
    elif callback.data == "btn3":
        keyboard = InlineKeyboardMarkup()
        btn3_1 = InlineKeyboardButton(text="Первый канал", callback_data="btn3_1")
        btn3_2 = InlineKeyboardButton(text="Второй канал", callback_data="btn3_2")
        btn3_3 = InlineKeyboardButton(text="Третий канал", callback_data="btn3_3")
        btn3_4 = InlineKeyboardButton(text="Четвертый канал", callback_data="btn3_4")
        keyboard.add(btn3_1,btn3_2,btn3_3,btn3_4)
        bot.send_message(callback.message.chat.id,"Подпишись на каналы чтобы получить доступ", reply_markup=keyboard)
    elif callback.data == "btn1_2":
        keyboard = InlineKeyboardMarkup()
        bot.send_message(callback.message.chat.id,"Чтоб начать тест, напиши в чат привет", reply_markup=keyboard)
        @bot.message_handler(func=lambda message: True)
        def echo_all(message):
            bot.reply_to(message, ai.gpt (message.text))

bot.polling()