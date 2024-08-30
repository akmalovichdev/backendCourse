from bot import *
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler, SkipHandler
from data import db

class SimpleMiddleware(BaseMiddleware):

    async def on_pre_process_message(self, message: types.Message, data: dict):
        if message.chat.type == 'private':
            if db.exist.blockedUser(message.from_user.id):
                await bot.send_message(message.from_user.id, 'Вам нельзя пользоваться ботом!')
                raise CancelHandler()
            
            if not db.exist.user(message.from_user.id):
                db.add.user(message.from_user.id, message.from_user.full_name)
        else:
            raise SkipHandler()
            
dp.middleware.setup(SimpleMiddleware())
