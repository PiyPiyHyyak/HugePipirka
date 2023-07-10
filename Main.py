from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

keyboard_callback = CallbackData("menu", "choice")
ege_bt = InlineKeyboardButton("ЕГЭ", callback_data=keyboard_callback.new(choice="ЕГЭ"))
oge_bt = InlineKeyboardButton("ОГЭ", callback_data=keyboard_callback.new(choice="ОГЭ"))
keyboard = InlineKeyboardMarkup(row_width=2)
keyboard.add(ege_bt)
keyboard.add(oge_bt)

from config import TOKEN

bot = Bot(token=TOKEN)  # Создание объекта бота с использованием токена
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"], state="*")
# команда /start будет работать из любом состояния
# Обработчик команды /start для любого состояния

async def start_handler(message: types.Message):
    await message.answer(
        text="Hello, My Name is Alex! I Will Help You to Prepare for Your English Examinations. What Exam Do You Pass this Year?",
        reply_markup=keyboard
    )

    # Функция для получения меню с кнопками


@dp.callback_query_handler(keyboard_callback.filter())
async def button_handler(call: types.CallbackQuery, callback_data: dict):
    choice = callback_data["choice"]
    await call.message.answer(f"You Have Chosen {choice}! Tell Me a Word Whose Cognates (one-root words) You Would Like to Know...")
    await bot.answer_callback_query(call.id)  # убирает часики с кнопки (завершает callback)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dispatcher=dp, skip_updates=True)
