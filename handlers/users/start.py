from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from pyexpat.errors import messages
from keys.key import kb_start
from loader import router, cursor, con
from aiogram import F
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

class Form_reg(StatesGroup):
    name = State()
    clas = State()

@router.message(Command('start'))
async def reg_start(message: Message, state: FSMContext):
    id_user = message.chat.id
    builder = ReplyKeyboardBuilder()
    for button in kb_start:
        builder.add(button)
    builder.adjust(1)
    await message.answer(text='Йоу бро',
                         reply_markup=builder.as_markup(resize_keyboard=True))
    cursor.execute("SELECT * FROM users WHERE id_user = (?)",[id_user])
    a = cursor.fetchall()
    if a:
        cursor.execute("SELECT user_name FROM users WHERE id = (?)", [id_user])
        b = cursor.fetchall()
        await message.answer(text=f'mnjboh {b[0]}')
    elif not a:
        await state.set_state(Form_reg.name)
        await message.answer('Для начала введите name', reply_markup=types.ReplyKeyboardRemove())

@router.message(Form_reg.name)
async def get_fio(message: Message, state: FSMContext):
    a = await state.get_state()
    await state.update_data(name=message.text)
    await state.set_state(Form_reg.clas)
    await message.answer('А теперь введите свой class')

@router.message(Form_reg.clas)
async def get_fio(message: Message, state: FSMContext):
    a = await state.get_state()
    await state.update_data(clas=message.text)
    data = await state.get_data()
    score_first = 0
    name = data['name']
    clas = data['clas']
    id_user = message.chat.id
    await state.clear()
    cursor.execute(
        "INSERT INTO users (id_user, user_name, class, score) VALUES (?, ?, ?, ?)",
        [id_user, name, clas, score_first])
    con.commit()
    await message.answer('Регистрация успешно завершена')