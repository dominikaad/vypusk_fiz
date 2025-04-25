from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.key import kb_mech, kb_elekdyn, kb_koleb, kb_molek, kb_optyka
from loader import router
from aiogram import F
import sqlite3
from aiogram import Bot, Dispatcher, Router
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loader import router, cursor, con
from aiogram.types import FSInputFile


@router.callback_query(F.data.startswith('meh'))
async def mechanika_teor(callback: types.CallbackQuery, bot: Bot):
    cursor.execute("SELECT image FROM teory WHERE rozdel = 'mech'")
    a = cursor.fetchall()
    fot1 = f'{a[0][0]}.webp'
    task_image1 = FSInputFile(fot1)
    await callback.message.answer(text='Теория по теме "Механика"')
    await callback.message.answer_photo(photo=task_image1)
    builder = ReplyKeyboardBuilder()
    for button in kb_mech:
        builder.add(button)
    builder.adjust(1)
    await callback.message.answer(text='Хотите пройти тест по данной теме?',
                                  reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(F.data.startswith('mol'))
async def mechanika_teor(callback: types.CallbackQuery, bot: Bot):
    cursor.execute("SELECT image FROM teory WHERE rozdel = 'molek'")
    a = cursor.fetchall()
    fot1 = f'{a[0][0]}.webp'
    task_image1 = FSInputFile(fot1)
    await callback.message.answer(text='Теория по теме "Молекулярная физика"')
    await callback.message.answer_photo(photo=task_image1)
    builder = ReplyKeyboardBuilder()
    for button in kb_molek:
        builder.add(button)
    builder.adjust(1)
    await callback.message.answer(text='Хотите пройти тест по данной теме?',
                                  reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(F.data.startswith('el_dyn'))
async def mechanika_teor(callback: types.CallbackQuery, bot: Bot):
    cursor.execute("SELECT image FROM teory WHERE rozdel = 'elekdyn'")
    a = cursor.fetchall()
    print(a)
    fot1 = f'{a[0][0]}.webp'
    fot2 = f'{a[1][0]}.webp'
    task_image1 = FSInputFile(fot1)
    task_image2 = FSInputFile(fot2)
    await callback.message.answer(text='Теория по теме "Электродинамика"')
    await callback.message.answer_photo(photo=task_image1)
    await callback.message.answer_photo(photo=task_image2)
    builder = ReplyKeyboardBuilder()
    for button in kb_elekdyn:
        builder.add(button)
    builder.adjust(1)
    await callback.message.answer(text='Хотите пройти тест по данной теме?',
                                  reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(F.data.startswith('kol_voln'))
async def mechanika_teor(callback: types.CallbackQuery, bot: Bot):
    cursor.execute("SELECT image FROM teory WHERE rozdel = 'koleb'")
    a = cursor.fetchall()
    fot1 = f'{a[0][0]}.webp'
    fot2 = f'{a[1][0]}.webp'
    task_image1 = FSInputFile(fot1)
    task_image2 = FSInputFile(fot2)
    await callback.message.answer(text='Теория по теме "Колебания и волны"')
    await callback.message.answer_photo(photo=task_image1)
    await callback.message.answer_photo(photo=task_image2)
    builder = ReplyKeyboardBuilder()
    for button in kb_koleb:
        builder.add(button)
    builder.adjust(1)
    await callback.message.answer(text='Хотите пройти тест по данной теме?',
                                  reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(F.data.startswith('opt'))
async def mechanika_teor(callback: types.CallbackQuery, bot: Bot):
    cursor.execute("SELECT image FROM teory WHERE rozdel = 'optyka'")
    a = cursor.fetchall()
    fot1 = f'{a[0][0]}.webp'
    task_image1 = FSInputFile(fot1)
    await callback.message.answer(text='Теория по теме "Оптика"')
    await callback.message.answer_photo(photo=task_image1)
    builder = ReplyKeyboardBuilder()
    for button in kb_optyka:
        builder.add(button)
    builder.adjust(1)
    await callback.message.answer(text='Хотите пройти тест по данной теме?',
                                  reply_markup=builder.as_markup(resize_keyboard=True))