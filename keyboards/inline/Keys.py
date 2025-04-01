from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton

Lang_keys=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="uz"),
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="ru"),
        ],
        [
            InlineKeyboardButton(text="🇺🇸 English", callback_data="en"),
        ],
    ]
)