from aiogram import executor
from bot import dp

if __name__ == "__main__":
    from bot import middleware
    from bot import handlers
    executor.start_polling(dp, skip_updates=True)