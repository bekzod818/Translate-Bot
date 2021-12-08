import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from config import TOKEN, text_to_speech
from buttons import menu, voice
from states import Translate
from googletrans import Translator
from aiogram.types import CallbackQuery

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    user = message.from_user.first_name
    await message.answer(f"Assalomu aleykum {user}😊\nTarjima turini tanlang", reply_markup=menu)
    await Translate.lang.set()


@dp.message_handler(state=Translate.lang)
async def which_lang(message: types.Message, state: FSMContext):
    lang = message.text
    await state.update_data(
        {"lang": lang},
    )
    await message.answer(f"Tarjima qilinuvchi matnni kiriting")
    await Translate.next()
    # await Translate.trans.set()

@dp.message_handler(state=Translate.trans)
async def translate_text(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    lang = data.get("lang")
    tarjimon = Translator()
    if lang == "🇺🇿 Uzb - 🇬🇧 Eng":
        tarjima = tarjimon.translate(text, dest="en")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="en")
    elif lang == "🇬🇧 Eng - 🇺🇿 Uzb":
        tarjima = tarjimon.translate(text, dest="uz")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="tr")
    elif lang == "🇺🇿 Uzb - 🇷🇺 Rus":
        tarjima = tarjimon.translate(text, dest="ru")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="ru")
    elif lang == "🇷🇺 Rus - 🇺🇿 Uzb":
        tarjima = tarjimon.translate(text, dest="uz")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="tr")
    await Translate.audio.set()
    # await state.finish()

@dp.callback_query_handler(text='voice', state=Translate.audio)
async def send_audio(call: CallbackQuery):
    await call.message.answer_audio(open("audio.mp3", 'rb'), reply_markup=menu)
    os.remove("audio.mp3")
    await Translate.lang.set()
    # if os.path.exists('/media/bekzod/Hard Disk7/Python Code/python_darslar/Python/audio.mp3'):
    #     await call.message.answer_audio(open('/media/bekzod/Hard Disk7/Python Code/python_darslar/Python/audio.mp3', 'rb'), reply_markup=menu)
    #     os.remove("/media/bekzod/Hard Disk7/Python Code/python_darslar/Python/audio.mp3")
    # else:
    #     await call.message.answer("Uzur keyinroq urinib ko'ring", reply_markup=menu)
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)