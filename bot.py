import telebot
import config
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import ai
import ai_web
import vheck
bot = telebot.TeleBot(config.key)

flag = False
work = False

@bot.message_handler(commands=['start','stop'])
def send_welcome(message):
    print(message)
    global flag,work
    work = False
    flag = False
    keyboard = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text="✅Работа", callback_data="btn1")
    btn2 = InlineKeyboardButton(text="✅ОГЭ/ЕГЭ", callback_data="btn2")
    btn3 = InlineKeyboardButton(text="✅Премиум версия", callback_data="btn3")
    btn4 = InlineKeyboardButton(text="✅Институты", callback_data="btn3")
    keyboard.row_width = 1
    keyboard.add(btn1,btn2,btn3,btn4)
    bot.reply_to(message, '''
Привет, это бот который помогает подросткам , найти легкий путь во взрослую жизнь

1.Хочешь найти работу , стажировку или понять кем ты хочешь быть , то нажимай на кнопку ✅Работа 

2.Есть желание подготовится к ОГЭ/ЕГЭ , порешать варианты ближайшего прошедшего года или найти репетитора, то тебе сюда ✅ОГЭ/ЕГЭ 

3.Премимум версия дает тебе множиство полезных роликах о том как : 'доработать свое резюме','как вести себя на собеседование' или же просто как выбрать универ.
И все это только за подписку на несколько каналов если заинтересовало то жми на ✅Премиум версия


4. Найти универ после профорентации , пройти демо вступительных твоего универа то жми на ✅Институты''', reply_markup=keyboard)



@bot.callback_query_handler()
def callback(callback):
    id_user = callback.from_user.id
    global flag,work
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
        if vheck.check(id_user) == False:
            btn3_1 = InlineKeyboardButton(text="Первый канал", url="https://t.me/tesstssst")
            btn3_2 = InlineKeyboardButton(text="Второй канал", callback_data="btn3_2")
            btn3_3 = InlineKeyboardButton(text="Третий канал", callback_data="btn3_3")
            btn3_4 = InlineKeyboardButton(text="Проверить", callback_data="btn3_4")
            keyboard.add(btn3_1,btn3_2,btn3_3,btn3_4)
            bot.send_message(callback.message.chat.id,"Подпишись на каналы чтобы получить доступ", reply_markup=keyboard)
        else:
            bot.reply_to(callback.message, '''Получилось!!!''')
    elif callback.data == "btn4":
        keyboard = InlineKeyboardMarkup()
        btn4_1 = InlineKeyboardButton(text="Найти Универ", callback_data="btn1_1")
        btn4_2 = InlineKeyboardButton(text='Демо версии', callback_data="btn1_2")
        keyboard.add(btn4_1,btn4_2)
        bot.send_message(callback.message.chat.id,"Твой путь в универ в этих 2 кнопках", reply_markup=keyboard)
    elif callback.data == "btn1_2":
        keyboard = InlineKeyboardMarkup()
        flag = True
        bot.send_message(callback.message.chat.id,"Чтоб начать тест, напиши в чат привет , чтоб остановить напиши /stop", reply_markup=keyboard)
    elif callback.data == "btn1_1":
        keyboard = InlineKeyboardMarkup()
        bot.send_message(callback.message.chat.id,"Чтоб найти работу, напиши в чат критерии работы, чтоб остановить напиши /stop", reply_markup=keyboard)
        work = True
    elif callback.data == "btn3_4":
        if vheck.check(id_user) == True:
            bot.reply_to(callback.message, '''Получилось!!!''')


@bot.message_handler(content_types=['text'])
def echo_all(message):
    global flag, work
    if work:
        text_ai = message.text
        bot.send_chat_action(message.chat.id, "typing")
        result = ai_web.web_ai(text_ai)
        bot.reply_to(message, result or "Не получилось обработать запрос. Попробуй написать профессию, город и желаемый формат работы.")

    if flag:
        bot.reply_to(message, ai.gpt (message.text,message.from_user.id))


bot.polling()
