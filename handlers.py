from aiogram import Router
from aiogram.filters import CommandStart,Command
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def start(message : Message):
    await message.answer(f"""
Добро пожаловать {message.chat.first_name} {message.chat.last_name}
Этот бот поможет тебе эффективно вылечится и не заболеть

Отправь /rec чтобы получить рекомендации по болезни
    """)
@router.message(Command("help"))
async def help(message : Message):
    await message.answer("""
Меню помощи

/help -- вызывает меню помощи
/rec -- даёт рекомендации по болезни
""")