from aiogram.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import KeyboardBuilder

def main_menu():
    kb_menu = KeyboardBuilder()
    
    btn_warm_up = InlineKeyboardButton(text="Разминка", callback_data="warm_up")
    btn_tdt_tech = InlineKeyboardButton(text="Техники тдт", callback_data="tdt_tech")
    btn_music = InlineKeyboardButton(text="Музыка для расслабления", callback_data="music")
    btn_breathing = InlineKeyboardButton(text="Дыхание", callback_data="breathing")
    btn_contacts = InlineKeyboardButton(text="Контакты центров тдт", callback_data="contacts")
    
    kb_menu.add(btn_warm_up, btn_tdt_tech, btn_music, btn_breathing, btn_contacts)
    kb_menu.adjust(1)
    
    return kb_menu
    
def exercises(flag: bool = None):
    kb_exercises = KeyboardBuilder()
    
    btn_ex_1 = InlineKeyboardButton(text="Упр_ие №1", callback_data="ex_1")
    btn_ex_2 = InlineKeyboardButton(text="Упр_ие №2", callback_data="ex_2")
    btn_ex_3 = InlineKeyboardButton(text="Упр_ие №3", callback_data="ex_3")
    btn_ex_4 = InlineKeyboardButton(text="Упр_ие №4", callback_data="ex_4")
    btn_ex_5 = InlineKeyboardButton(text="Упр_ие №5", callback_data="ex_5")

    kb_exercises.add(btn_ex_1, btn_ex_2, btn_ex_3, btn_ex_4, btn_ex_5)
    kb_exercises.adjust(1)
    
    return kb_exercises


