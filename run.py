import asyncio

from aiogram import Bot,Dispatcher

from handlers import router
from rec_command import router as rec_router



bot = Bot(token="8489572705:AAFmvaqCX39x72_zjH9wRNyr5iRScpNA9yE")
dp = Dispatcher()



async def main():
    dp.include_routers(router,rec_router)
    await dp.start_polling(bot)




if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot shutdown")

