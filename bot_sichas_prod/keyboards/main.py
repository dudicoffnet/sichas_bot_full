from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔍 Найти рядом"), KeyboardButton(text="📝 Моя анкета")],
        [KeyboardButton(text="⚙️ Настройки"), KeyboardButton(text="💖 Помочь проекту")]
    ],
    resize_keyboard=True
)
