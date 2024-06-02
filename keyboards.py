from aiogram.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_menu(back_to_menu: bool = False):
    kb_menu = InlineKeyboardBuilder()
    
    btn_warm_up = InlineKeyboardButton(text="Разминка", callback_data="warm_up")
    btn_tdt_tech = InlineKeyboardButton(text="Техники тдт", callback_data="tdt_tech")
    btn_music = InlineKeyboardButton(text="Музыка для расслабления", callback_data="music")
    # btn_breathing = InlineKeyboardButton(text="Дыхание", callback_data="breathing")
    btn_contacts = InlineKeyboardButton(text="Контакты центров тдт", callback_data="contacts")
    btn_back = InlineKeyboardButton(text="Назад", callback_data="back")
    
    if back_to_menu == False:
        kb_menu.add(btn_warm_up, btn_tdt_tech, btn_music, btn_contacts)
    else:
        kb_menu.add(btn_back)
        
    kb_menu.adjust(1)
    
    return kb_menu
    
def exercises(*exercises, end_of_block: bool = False):
    kb_exercises = InlineKeyboardBuilder()
    btn_back = InlineKeyboardButton(text="Назад", callback_data="back")
    btn_find_out = InlineKeyboardButton(text="Узнать больше", callback_data="find_out")
    
    temp_list = []
    
    for num, item in enumerate(exercises):
        temp_list.append(InlineKeyboardButton(text=f"{item}", callback_data=f"ex_{num + 1}"))

    if end_of_block == False:
        kb_exercises.add(*temp_list, btn_back)
    else:
        kb_exercises.add(btn_find_out)
        
    kb_exercises.adjust(1)
    
    return kb_exercises
    
