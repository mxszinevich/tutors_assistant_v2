from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.handler import CancelHandler

from bot.db_api import has_student
from bot.keyboards import base_meny_keyboard
from bot.loader import dp
from bot.standard_bot_answers import MAIN_MENU_TITLE


@dp.message_handler(Command("menu"), state="*")
async def show_menu(message: types.Message):
    """
    Отображение базового меню
    """
    if await dp.current_state().get_state():
        await dp.current_state().reset_state(with_data=True)

    if not (await has_student(telegram_id=message.from_user.id)):
        raise CancelHandler()

    await message.answer(MAIN_MENU_TITLE, reply_markup=base_meny_keyboard)
