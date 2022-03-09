from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import base, InlineKeyboardButton, InlineKeyboardMarkup
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Следующий",
                                         callback_data="button_call_1")
    markup.add(button_call_1)
    question1 = 'Каков правильный синтаксис для вывода "Привет Мир" в Python?'
    answer1 = ['echo("Привет Мир");', 'echo"Привет Мир"', 'p("Привет Мир")', 'print("Привет Мир")']
    await bot.send_poll(message.chat.id,
                        question= question1,
                        options=answer1,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=3,
                        explanation='output function',
                        reply_markup=markup)


@dp.callback_query_handler(lambda func: func.data =="button_call_1")
async def quiz2 (call:types.callback_query):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("Следующий",
                                         callback_data="button_call_2")
    markup.add(button_call_2)
    question2 = 'Как вы вставляете комментарии в код Python?'
    answer2 = ['#Это комментарий', '/*Это комментарий*/', '//Это комментарий', 'Это комментарий#']
    await bot.send_poll(call.message.chat.id,
                        question= question2,
                        options=answer2,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=0,
                        explanation='output function',
                        reply_markup=markup)


@dp.callback_query_handler(lambda func: func.data =="button_call_2")
async def quiz3 (call:types.callback_query):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("Следующий",
                                         callback_data="button_call_3")
    markup.add(button_call_3)
    question3 = 'Какое из них не является законным именем переменной?'
    answer3 = ['_Myvar', 'my-var', 'my_var', '_myvar']
    await bot.send_poll(call.message.chat.id,
                        question= question3,
                        options=answer3,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=1,
                        explanation='output function')


@dp.callback_query_handler(lambda func: func.data =="button_call_3")
async def quiz3 (call:types.callback_query):
    question4 =  'Дан список list2 =[8, 12, 45, 67, 89, 45]' \
      ' Выберите правильный вариант решения чтобы результат был таким: ' \
      'list2 =[8, 12, 45, 67, 89, 45, 8, 12, 45, 67, 89, 45]'
    await bot.send_poll(call.message.chat.id,
                        question= question4,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=1,
                        explanation='output function')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)