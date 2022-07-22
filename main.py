from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from aiogram.utils import executor
from config import dp
import logging
from aiogram import types, Dispatcher
from config import bot
from handler import extra

@dp.message_handler(commands=['start'])
async def  start(message: types.Message):
    await bot.send_message(message.from_user.id,f"Салам {message.from_user.full_name}")

dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Сколько лет в году?"
    answers = [
        "шаурма",
        "кукумбер",

    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=0,
        explanation="вопросы по Астраномии",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,

    )

@dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(call: types.CallbackQuery):

    question = "Как завут Максима?"
    answers = [
        "Годичный звёздный параллакс",
        "пожалуйста поставьте 5,на 4 месяце я выучу Django на отлично",

    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=1,
        explanation="вопросы по Астраномии",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )


@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open("media/index.png",'rb')
    photo2 = open("media/загружено.jfif", 'rb')
    await bot.send_photo(message.chat.id,photo=photo)
    await bot.send_photo(message.chat.id, photo=photo2)


extra.register_handlers_extra(dp)





if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)





