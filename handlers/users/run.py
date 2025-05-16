from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.key import kb_razdel_fiz, kb_redaktir, kb_choise
from loader import router
from aiogram import F
import sqlite3
from aiogram import Bot, Dispatcher, Router
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loader import router, cursor, con
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from openai import OpenAI

class Form_reg(StatesGroup):
    name_2 = State()
    clas_2 = State()
    quest = State()

@router.message(Command('question'))
async def fun_text(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Form_reg.quest)
    await message.answer(text='Задайте вопрос', reply_markup=types.ReplyKeyboardRemove())

@router.message(Form_reg.quest)
async def get_fio(message: Message, state: FSMContext):
    a = await state.get_state()
    await state.update_data(quest=message.text)
    data = await state.get_data()
    quest = data['quest']
    await state.clear()
    client = OpenAI(
           api_key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjI2YzIzN2MwLWJmZmMtNGNiZC1hYTVhLTAwZDQ2OWUyZDZmZCIsImlzRGV2ZWxvcGVyIjp0cnVlLCJpYXQiOjE3NDc0MDkzNTgsImV4cCI6MjA2Mjk4NTM1OH0.UMERPpHlEwrx7K5Vv25I7GIIAtn2a5-HMkya_FXDp3A',
           base_url='https://bothub.chat/api/v2/openai/v1'
       )

    chat_completion = client.chat.completions.create(
           messages=[
               {
                   'role': 'user',
                   'content': f'Ты учитель, ответь макимально понячтно для школьника на вопрос:{quest}'
               }
           ],
           model='o3-mini-high',
       )

    result = chat_completion.choices[0].message.content
    await message.answer(text=f'Ответ на ваш вопрос:\n{result}')
    await message.answer(
        text='Для того, чтобы вернуться в меню, введите команду /menu\nДля того, чтобы ыернуться в начало,введите команду /start')


@router.message(F.text == 'Мои данные')
async def fun_text(message: Message):
    id_user = message.chat.id
    cursor.execute("SELECT * FROM users WHERE id_user = (?)", [id_user])
    a = cursor.fetchall()
    builder = InlineKeyboardBuilder()
    for button in kb_redaktir:
        builder.add(button)
    builder.adjust(1)
    await message.answer(text=f'Ваше имя: {a[0][1]}\nВаш класс: {a[0][2]}\nКоличество решённых задач: {a[0][3]}', reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(F.data.startswith('name'))
async def exit(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Form_reg.name_2)
    await callback.message.answer('Введите новое имя', reply_markup=types.ReplyKeyboardRemove())

@router.message(Form_reg.name_2)
async def get_fio(message: Message, state: FSMContext):
    a = await state.get_state()
    await state.update_data(name_2=message.text)
    data = await state.get_data()
    name_2 = data['name_2']
    id_user = message.chat.id
    await state.clear()
    cursor.execute("UPDATE users SET user_name = (?) WHERE id_user = (?)", [name_2, id_user])
    con.commit()
    builder = InlineKeyboardBuilder()
    cursor.execute("SELECT * FROM users WHERE id_user = (?)", [id_user])
    a = cursor.fetchall()
    for button in kb_redaktir:
        builder.add(button)
    builder.adjust(1)
    await message.answer(text=f'Ваше имя: {a[0][1]}\nВаш класс: {a[0][2]}\nКоличество решённых задач: {a[0][3]}', reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(F.data.startswith('class'))
async def exit(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Form_reg.clas_2)
    await callback.message.answer('Введите новый класс', reply_markup=types.ReplyKeyboardRemove())

@router.message(Form_reg.clas_2)
async def get_fio(message: Message, state: FSMContext):
    a = await state.get_state()
    await state.update_data(class_2=message.text)
    data = await state.get_data()
    class_2 = data['class_2']
    id_user = message.chat.id
    await state.clear()
    cursor.execute("UPDATE users SET class = (?) WHERE id_user = (?)", [class_2, id_user])
    con.commit()
    builder = InlineKeyboardBuilder()
    cursor.execute("SELECT * FROM users WHERE id_user = (?)", [id_user])
    a = cursor.fetchall()
    for button in kb_redaktir:
        builder.add(button)
    builder.adjust(1)
    await message.answer(text=f'Ваше имя: {a[0][1]}\nВаш класс: {a[0][2]}\nКоличество решённых задач: {a[0][3]}', reply_markup=builder.as_markup(resize_keyboard=True))


@router.message(F.text == 'Меню')
@router.message(F.text == 'Нет')
@router.message(Command('menu'))
async def fun_text(message: Message, state: FSMContext):
    await state.clear()
    builder = ReplyKeyboardBuilder()
    for button in kb_choise:
        builder.add(button)
    builder.adjust(1)
    await message.answer(text='Вы можете выбрать: пройти общий тест или выбрать раздел физики',
                                  reply_markup=builder.as_markup(resize_keyboard=True))

@router.message(F.text == 'Выбрать раздел физики')
async def fun_text(message: Message):
    builder = InlineKeyboardBuilder()
    for button in kb_razdel_fiz:
        builder.add(button)
    builder.adjust(1)
    await message.answer(text='Выбери раздел физики, про который хочешь узнать информацию',reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(F.data.startswith('exit'))
async def exit(callback: types.CallbackQuery, bot: Bot):
    await callback.message.answer(text='Для того, чтобы вернуться в меню, введите команду /menu\nДля того, чтобы ыернуться в начало,введите команду /start')