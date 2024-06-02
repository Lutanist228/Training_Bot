
async def message_delition(message_tuple: tuple):
    for msg in message_tuple:
        try:
            await msg.delete()
        except AttributeError:
            [await el.delete() for el in msg]
        
        