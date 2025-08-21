from aiogram import Router, types
from aiogram.filters import Command
from keyboards.main import main_kb
from states.anketa import Anketa
from aiogram.fsm.context import FSMContext

router = Router()

def register_handlers(dp):
    dp.include_router(router)

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 Привет! Это бот 'Сейчас'.\nЗаполни анкету и находи людей рядом.",
        reply_markup=main_kb
    )

@router.message(lambda m: m.text == "📝 Моя анкета")
async def my_profile(message: types.Message, state: FSMContext):
    await message.answer("Введите своё имя:")
    await state.set_state(Anketa.name)
