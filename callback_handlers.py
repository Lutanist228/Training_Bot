from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest
from aiogram.types.input_media_audio import InputMediaAudio

from states import *
from keyboards import *
from main import bot
from additional_functions import message_delition

cb_router = Router()

@cb_router.callback_query(General_States.warm_up)
async def warm_up_proc(callback: CallbackQuery, state: FSMContext):
    from config import AUDIO_IDS, VIDEO_IDS
    
    data = await state.get_data()
    
    try:
        await message_delition(data["msg_buffer"])
    except (KeyError, TelegramBadRequest):
        pass
    
    match callback.data:
        case "ex_1":
            message_one = await bot.send_video(chat_id=callback.from_user.id, video=VIDEO_IDS["warm_up"]["body_jazz"])
            message_two = await bot.send_audio(chat_id=callback.from_user.id, audio=AUDIO_IDS["warm_up"]["body_jazz"], 
            caption="Основная идея данного упражнения в выделении «центров движения».В определенный момент времени ваше движение должно исходить от одного из этих центров: \n- голова-шея\n- плечи\n- локти\n- кисти\n- бедра (таз)\n- колени \n- ступни\n\n Важно: последовательность обращения к центрам может быть прямой (от головы к ступням), или обратной (от ступней до головы).\n\nВо время выполнения упражнения, вы можете сделать акцент на поиске новых, непривычных для вашего тела движений. Или на отделении/связанности центров с другими частями тела. Также можно менять амплитуду движения, ритм и его скорость.\n\nПродолжительность – 10-15 минут ")
            await state.update_data(msg_buffer=(message_one,message_two))
        case "ex_2":
            message_one = await bot.send_video(chat_id=callback.from_user.id, video=VIDEO_IDS["warm_up"]["vibro_dance"])
            media_group = [InputMediaAudio(media=elem) for elem in AUDIO_IDS["warm_up"]["vibro_dance"]]
            message_two = await bot.send_message(chat_id=callback.from_user.id, text="1) Встаньте и закройте глаза, под музыку начинайте искать вибрацию, мелкую тряску. Она начинается от пола, идет по ногам и проходит через все тело, постепенно подключая колени, таз, плечи, руки и голову.\n2) Через пару минут начинайте увеличивать амплитуду движения, при этом сохраняйте тот же образ движения.\n3) Далее вибрация постепенно становится волной, которая проходит через все тело.\n4)Замедлите свои движенияи постепенно открывайте глаза.\n\nПродолжительность – 10-15 минут ")
            message_three = await bot.send_media_group(chat_id=callback.from_user.id, media=media_group)
            await state.update_data(msg_buffer=(message_one, message_two, message_three))
        case "ex_3":
            message_one = await bot.send_video(chat_id=callback.from_user.id, video=VIDEO_IDS["warm_up"]["shake_stratch"])
            media_group = [InputMediaAudio(media=elem) for elem in AUDIO_IDS["warm_up"]["shake_stratch"]]
            message_two = await bot.send_message(chat_id=callback.from_user.id, text="1) Встаньте и закройте глаза, под музыку начинайте искать мелкую тряску. Она начинается от пола, идет по ногам и проходит через все тело, постепенно увеличиваясь и подключая колени, таз, плечи, руки и голову.\n2) Через несколько минут тряска прекращается и начинается растяжка:нужно тянуться всеми пятью конечностями, включая голову. \nВажно: растяжка происходит не за счет растягивания мышц, а за счет «растягивания» тела в целом, ощущения должны быть как при потягиваниях. Растягивайтесь также пару минут. Цикл нужно повторить несколько раз.\n\nПродолжительность – 10-15 минут")
            message_three = await bot.send_media_group(chat_id=callback.from_user.id, media=media_group)
            await state.update_data(msg_buffer=(message_one, message_two, message_three))
        case "ex_4":
            message_one = await bot.send_message(chat_id=callback.from_user.id, text="1) Идите по кругу, в какой-то момент напрягите левую руку, правую, ноги, поясницу. Cначала напряжение должно быть слабым, потом оно постепенно возрастает и доходит до предела. \n2) В состоянии предельного напряжения нужно идти 15-20 секунд.\n3) Потом сбрасывайте напряжение: полностью расслабьте напряженный участок тела. \n4) Прислушайтесь к своим ощущениям, продолжая идти, вспомните свои обычные «зажимы» (места, где вы чувствуете напряжение в течение дня). Попробуйте также напрячь тело в этом месте, доводя зажим до предела, сбросьте и расслабьтесьчерез 15-20 секунд.\n5) Напрягите по такой же схеме любой другой участок тела: руки, ноги, поясницу, всё тело. Обратите внимание на то, что происходит с вашими зажимами.\n6) Повторите это упражнение со своими зажимами несколько раз.")
            await state.update_data(msg_buffer=(message_one,))
        case "back": 
            await state.clear()
            await callback.message.edit_text(text="Главное меню", reply_markup=main_menu().as_markup())      
    
@cb_router.callback_query(General_States.tdt)
async def tdt_proc(callback: CallbackQuery, state: FSMContext):
    from config import AUDIO_IDS, VIDEO_IDS
    
    data = await state.get_data()
    
    try:
        await message_delition(data["msg_buffer"])
    except (KeyError, TelegramBadRequest):
        pass
    
    match callback.data:
        case "ex_1":
            message_one = await bot.send_video(chat_id=callback.from_user.id, video=VIDEO_IDS["tdt"]["five_rhytms"])
            media_group = [InputMediaAudio(media=elem) for elem in AUDIO_IDS["tdt"]["five_rhytms"]]
            message_two = await bot.send_message(chat_id=callback.from_user.id, 
            text="Пять ритмов (волна) Габриэлы Рот – это 5 первичных ритмов движения, которые, по ее мнению, представляют энергии, с которыми человек встречается во внутренней и внешней реальностях. \nВпервые этот процесс рекомендуют проходить с закрытыми глазами для максимальной фокусировки на своих чувствах.Встаньте закройте глаза и протанцуйте все 5 состояний, плавно перетекая из одного в другое, также обратите внимание на дыхание. \n\n1) Текучесть (flowing) – движения «женской» энергии: плавные, мягкие, непрерывные и текучие.Дыхание медленное, глубокое и непрерывное.\n2) Прерывистость (staccato) – движения «мужской»энергии: сильные, четкие, энергичные, направленные во вне.Дыхание отрывистое с акцентом на выдох (со звуком).\n3) Хаос (chaos) – хаотические, постоянно меняющиеся движения, «бурлящая лава». Дыхание хаотичное, постоянно меняющиеся.\n4) Лиричность (lyrical)– тонкие, легкие изящные движения, «падающие листья». Дыхание легкое, сфокусированное на легкий выдох.\n5)	Неподвижность (stillness)– постепенное замедление, медленное движение, «пульсирующая статуя».Дыхание медленное, поверхностное с акцентом на вдохе, внимание постепенно переходит в глубь тела.\n\nПродолжительность – 25 минут (один ритм длится около 5 минут).", reply_markup=exercises(end_of_block=True).as_markup())
            message_three = await bot.send_media_group(chat_id=callback.from_user.id, media=media_group)
            await state.update_data(msg_buffer=(message_one, message_two, message_three))
        case "ex_2":
            message_one = await bot.send_video(chat_id=callback.from_user.id, video=VIDEO_IDS["tdt"]["polarity"])
            message_two = await bot.send_audio(chat_id=callback.from_user.id, audio=AUDIO_IDS["tdt"]["polarity"], 
            caption="В данном упражнении вам нужно поработать со своими противоположными качествами. \nВстаньте и начните исследовать в танце различные полярности, переходите постепенно от одной к другой и от полярности к полярности. \nУ вас должен получиться собственный танец, под конец попробуйте объединить разные качества.\n\n	Медленное – быстрое\n	    Напряжение – расслабление \n	    Вверх – низ \n	    Большое – маленькое\n	    Мягкое – жесткое \n	    Хаос – порядок\n	    Открытое – закрытое \n	    Внутрь – вовне \n	    Тянуть – толкать \n	    Кривое – прямое и т.д\n\nПротивоположности часто встречаются в жизни.В движении, когда одна мышца сокращается, другая всегда растягивается. Полярности – это разные точки одного спектра, данное упражнение направлено на гармонизацию и осознанию связи между различными состояниями. \n\nПродолжительность – 15 минут")
            await state.update_data(msg_buffer=(message_one,message_two))
        case "ex_3":
            message_one = await bot.send_audio(chat_id=callback.from_user.id, audio=AUDIO_IDS["tdt"]["small_dance"], 
            caption="Данное упражнение помогает найти центр своего веса. Даже когда мы стоим вес нашего тела все равно немного перемещается. \n1)	Встаньте с закрытыми глазами и стойте, старайтесь задействовать минимум энергии. \n2)	Наблюдайте за небольшими перемещениями вашего веса, который удерживает вас в равновесии, сконцентрируйтесь на нем. \n3)	Прочувствуйте как вес вашего тела передается через кости в пол, заметить, как ваше тело немного покачивается вперед и назад. Когда привыкните попробуйте усиливать это покачивание.\n4)	Медленно останавливайте покачивание и возвращайтесь в состояние покоя.")
            await state.update_data(msg_buffer=(message_one,))
        case "back": 
            await state.clear()
            await callback.message.edit_text(text="Главное меню", reply_markup=main_menu().as_markup())  
        case "find_out":
            message_one = await bot.send_message(chat_id=callback.from_user.id, text="Суть данного процесса в распознании какие ритмы для нас привычны, а какие вызывают отторжение. Именно на эти отторгаемые движения и стоит обратить внимание.\nПример: женщинам часто не нравятся «мужские» движения прерывистости, однако многие из них жалуются на невозможность выражать свои чувства и состояние жертвы. В процессе работы выясняется, что именно четкое выражение своих желаний помогает им изменить ситуацию.Ваши силы там, куда вам страшно и непривычно идти.\n\nТакже после этой практики следует задать себе пару вопросов и самостоятельно проанализировать ответы: \nКакой ритм показался вам знакомым, а какой новым?\nЧто вызвало у вас больше всего энергии? От чего больше всего устали? \nКакой ритм вызывал больше чувств? \nГде у вас получалось занять больше пространства движениями? \nЧто еще важного вы почувствовали в каждом из ритмов?")
            await state.update_data(msg_buffer=(message_one,))
            
@cb_router.callback_query(lambda x: x)
async def global_cb_proc(callback: CallbackQuery, state: FSMContext):
    from config import AUDIO_IDS
    
    data = await state.get_data()
    
    try:
        await message_delition(data["msg_buffer"])
    except (KeyError, TelegramBadRequest):
        pass
    
    if callback.data == "warm_up":
        await state.set_state(General_States.warm_up)
        await callback.message.edit_text(text="Упражнения Разминки", 
        reply_markup=exercises("Body Jazz", "Вибрация-танец", "Тряска-растяжка", "Зажимы по кругу").as_markup())
    elif callback.data == "tdt_tech":
        await state.set_state(General_States.tdt)
        await callback.message.edit_text(text="Упражнения ТДТ", 
        reply_markup=exercises("5 ритмов", "Полярности", '"Маленький" танец').as_markup())
    elif callback.data == "music":
        media_group = [InputMediaAudio(media=elem) for elem in AUDIO_IDS["relax_music"]]
        message_one = await bot.send_message(chat_id=callback.from_user.id, text="Музыкальная составляющая терапии очень важна. Предлагаю вам послушать эти мелодии и найти те, которые смогут вызывать у вас наибольший эмоциональный отклик.")
        message_two = await bot.send_media_group(chat_id=callback.from_user.id, media=media_group)
        await state.update_data(msg_buffer=(message_one,message_two))
    elif callback.data == "contacts": 
        await callback.message.edit_text(text="Если у вас появится желание узнать больше о танцевально-двигательной терапии, вы можете найти информацию на официальных сайтах:\n- https://vk.com/atdt_rus официальный сайт ВКонтакте \n- https://www.atdt.ru официальный сайт Ассоциации Танцевально-Двигательной терапии", reply_markup=main_menu(True).as_markup())
    elif callback.data == "back":
            await callback.message.edit_text(text="Главное меню", reply_markup=main_menu().as_markup())      
