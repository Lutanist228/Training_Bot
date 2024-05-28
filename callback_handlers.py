from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from states import *
from keyboards import *

cb_router = Router()

@cb_router.callback_query(warm_up)
async def warm_up_proc(callback: CallbackQuery, state: FSMContext):
    match callback.data:
        case "ex_1": pass
        case "ex_2": pass
    
@cb_router.callback_query(tdt)
async def warm_up_proc(callback: CallbackQuery, state: FSMContext):
    match callback.data:
        case "ex_1": pass
        case "ex_2": pass
    
@cb_router.callback_query()
async def global_cb_proc(callback: CallbackQuery, state: FSMContext):
    if callback.data == "warm_up":
        await state.set_state(warm_up)
        await callback.message.edit_text(text="Упражнения Разминки", reply_markup=exercises().as_markup())
    elif callback.data == "tdt_tech":
        await state.set_state(tdt)
        await callback.message.edit_text(text="Упражнения ТДТ", reply_markup=exercises().as_markup())
    elif callback.data == "breathing": pass
    elif callback.data == "contacts": pass