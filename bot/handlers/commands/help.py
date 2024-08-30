from bot import *

@dp.message_handler(commands='help')
async def helpHandler(message: types.Message):
    await message.answer('Kanaqa yordam berolaman?')