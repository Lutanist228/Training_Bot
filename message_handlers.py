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
    await bot.send_message(chat_id=message.from_user.id, text="Главное меню", reply_markup=main_menu().as_markup())      
    
@msg_router.message()
async def id_revealing(message: Message):
    print("id данного видео: ", message.video.file_id)
    print("id данного аудио: ", message.audio.file_id)
