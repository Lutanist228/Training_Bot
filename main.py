from aiogram import Bot, Dispatcher
import aiogram
import asyncio as asy
from aiogram.fsm.storage.memory import MemoryStorage

from config import API_TOKEN

dp = Dispatcher(storage=MemoryStorage())
bot = Bot(token=API_TOKEN)

async def on_startup():
    print("Бот запущен!")
    
async def main():
    import message_handlers, callback_handlers
    await bot.delete_webhook(drop_pending_updates=True)
    
    dp.include_router(message_handlers.msg_router, callback_handlers.cb_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asy.run(main())