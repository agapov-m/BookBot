from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON

router = Router()

@router.message()
async def response_to_invalid_commands(message: Message):
    await message.answer(text=LEXICON['invalid_command'])