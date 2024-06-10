from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from keyboards import *
from main import bot

msg_router = Router()

@msg_router.message(Command("start"))
async def starting_menu(message: Message, state: FSMContext):
    await state.clear()
    await bot.send_message(chat_id=message.from_user.id, text="Для того, чтобы танцевать необязательно идеально слышать музыку, обладать спортивным телосложением, садиться на шпагат и иметь какой-то танцевальный опыт. Заниматься танцевальной терапией может абсолютно каждый! Тут нет правильного или неправильного исполнения, любые движения будут правильными. Cамое главное – это твои внутренние ощущения.", reply_markup=main_menu().as_markup())      
    
@msg_router.message()
async def id_revealing(message: Message):
    try:
        print("id данного видео: ", message.video.file_id)
    except AttributeError:
        print("id данного аудио: ", message.audio.file_id)