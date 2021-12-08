from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇺🇿 Uzb - 🇬🇧 Eng"), KeyboardButton(text="🇬🇧 Eng - 🇺🇿 Uzb")],
        [KeyboardButton(text="🇺🇿 Uzb - 🇷🇺 Rus"), KeyboardButton(text="🇷🇺 Rus - 🇺🇿 Uzb")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

voice = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🎙 Audio tinglash", callback_data="voice"),
    ]
    ]
)
