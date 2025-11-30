from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

import keyboard
import json_reader

router = Router()

class DiseaseInputState(StatesGroup):
    disease  = State()
    page : int


@router.message(Command("rec"))
async  def rec(message : Message,state : FSMContext):
    await state.set_state(DiseaseInputState.disease)
    DiseaseInputState.page = 0
    await message.answer(
        "Отлично выбери свою болезнь из списка",
        reply_markup= await keyboard.add_keyboard(DiseaseInputState.page))



@router.message(DiseaseInputState.disease)
async def select(message : Message,state : FSMContext):
    all_list = await json_reader.get_all_diseases()

    if message.text == ">>>":
        if DiseaseInputState.page >= (len(all_list) // 10) :
            return
        DiseaseInputState.page+=1
        await message.answer("Следующая страница", reply_markup=await keyboard.add_keyboard(DiseaseInputState.page))
        return 0
    elif message.text == "<<<":
        if DiseaseInputState.page <= 0:
            return 0
        DiseaseInputState.page-=1
        await message.answer("Предыдущая страница", reply_markup=await keyboard.add_keyboard(DiseaseInputState.page))
        return 0



    name = None
    for key,value in all_list.items():
        if str(value).lower() == message.text.lower():
            name = key
            print("Found "+name)
            break

        else:
            print("Not found")


    if name is not None:
        await state.clear()

        await message.answer(f"""
                Рекомендации по {message.text} ({name}):

                """, reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer("Болезнь не найдена")








