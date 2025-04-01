from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from googletrans import Translator
from keyboards.inline import Lang_keys
from aiogram.dispatcher import FSMContext


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\nTarjimon botiga hush kelibsiz")
    await message.answer("Menga so'z yuboring. Men esa sizga tarjima qilaman.")


@dp.message_handler(state=None)
async def bot_echo(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text)
    await message.answer("Tilni tanlang.", reply_markup=Lang_keys)


async def translate_text(text, dest):
    translator = Translator()  # No async with
    result = translator.translate(text, dest=dest)
    return result.text  # Extract text only


@dp.callback_query_handler(text=["uz", "ru", "en"])
async def lang_translate(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data.get("text", "No data found")

    if text != "No data found":
        translated = await translate_text(text, callback_query.data)
        await callback_query.message.answer(translated)
