from bot import *

@dp.message_handler(commands='start')
async def startHandler(message: types.Message):
    await message.answer(f'Salom <b>{message.from_user.full_name}</b>')