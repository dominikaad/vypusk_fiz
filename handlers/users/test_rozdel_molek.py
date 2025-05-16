from aiogram.types import Message
from aiogram import F
from aiogram import types
from loader import router, cursor, con
from aiogram.types import FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

class Form_mol(StatesGroup):
    otv1_molek = State()
    otv2_molek = State()
    otv3_molek = State()

@router.message(F.text == 'Тест по теме "Молекулярная физика"')
async def test_mech(message: Message, state: FSMContext):
    cursor.execute("SELECT number FROM test_molek")
    num = cursor.fetchall()
    cursor.execute("SELECT uslov FROM test_molek")
    uslov = cursor.fetchall()
    await message.answer(f'Задача №{num[0][0]}\nВведите только число, округленное до целого по математическим правилам')
    fot1 = f'{uslov[0][0]}.pdf'
    task_image1 = FSInputFile(fot1)
    await state.set_state(Form_mol.otv1_molek)
    await message.answer_photo(photo=task_image1, reply_markup=types.ReplyKeyboardRemove())

@router.message(Form_mol.otv1_molek)
async def get_fio(message: Message, state: FSMContext):
    id_user = message.chat.id
    cursor.execute("SELECT otvet FROM test_molek")
    cor_otv = cursor.fetchall()
    cursor.execute("SELECT foto FROM test_molek")
    foto_answ = cursor.fetchall()
    a = await state.get_state()
    await state.update_data(otvet=message.text)
    data = await state.get_data()
    otvet = data['otvet']
    print(otvet)
    print(cor_otv[0][0])
    try:
        number = int(otvet)
        await state.clear()
        if number == int(cor_otv[0][0]):
            cursor.execute("SELECT score FROM users WHERE id_user = (?)", [id_user])
            score_first = cursor.fetchall()
            score_new = score_first[0][0]+1
            print(score_new)
            cursor.execute("UPDATE users SET score = (?) WHERE id_user = (?)", [score_new, id_user])
            con.commit()
            await message.answer(text='Вы решили верно!')
        else:
            fot2 = f'{foto_answ[0][0]}.jpg'
            task_image2 = FSInputFile(fot2)
            await message.answer(text='К сожалению вы решили не верно.\nВот правильное решение:')
            await message.answer_photo(photo=task_image2, reply_markup=types.ReplyKeyboardRemove())
        cursor.execute("SELECT number FROM test_molek")
        num = cursor.fetchall()
        cursor.execute("SELECT uslov FROM test_molek")
        uslov = cursor.fetchall()
        await message.answer(f'Задача №{num[1][0]}\nВведите только число, округленное до целого по математическим правилам')
        fot1 = f'{uslov[1][0]}.pdf'
        task_image1 = FSInputFile(fot1)
        await state.set_state(Form_mol.otv2_molek)
        await message.answer_photo(photo=task_image1, reply_markup=types.ReplyKeyboardRemove())
    except ValueError:
        await message.answer(text='Округлите число до целого')
        return


@router.message(Form_mol.otv2_molek)
async def get_fio(message: Message, state: FSMContext):
    id_user = message.chat.id
    cursor.execute("SELECT otvet FROM test_molek")
    cor_otv = cursor.fetchall()
    cursor.execute("SELECT foto FROM test_molek")
    foto_answ = cursor.fetchall()
    a = await state.get_state()
    await state.update_data(otvet2=message.text)
    data = await state.get_data()
    otvet = data['otvet2']
    print(otvet)
    print(cor_otv[1][0])
    try:
        number = int(otvet)
        await state.clear()
        if number == int(cor_otv[1][0]):
            cursor.execute("SELECT score FROM users WHERE id_user = (?)", [id_user])
            score_first = cursor.fetchall()
            score_new = score_first[0][0]+1
            print(score_new)
            cursor.execute("UPDATE users SET score = (?) WHERE id_user = (?)", [score_new, id_user])
            con.commit()
            await message.answer(text='Вы решили верно!')
        else:
            fot2 = f'{foto_answ[1][0]}.jpg'
            task_image2 = FSInputFile(fot2)
            await message.answer(text='К сожалению вы решили не верно.\nВот правильное решение:')
            await message.answer_photo(photo=task_image2, reply_markup=types.ReplyKeyboardRemove())
        cursor.execute("SELECT number FROM test_molek")
        num = cursor.fetchall()
        cursor.execute("SELECT uslov FROM test_molek")
        uslov = cursor.fetchall()
        await message.answer(f'Задача №{num[2][0]}\nВведите только число, округленное до целого по математическим правилам')
        fot1 = f'{uslov[2][0]}.pdf'
        task_image1 = FSInputFile(fot1)
        await state.set_state(Form_mol.otv3_molek)
        await message.answer_photo(photo=task_image1, reply_markup=types.ReplyKeyboardRemove())
    except ValueError:
        await message.answer(text='Округлите число до целого')
        return

@router.message(Form_mol.otv3_molek)
async def get_fio(message: Message, state: FSMContext):
    id_user = message.chat.id
    cursor.execute("SELECT otvet FROM test_molek")
    cor_otv = cursor.fetchall()
    cursor.execute("SELECT foto FROM test_molek")
    foto_answ = cursor.fetchall()
    a = await state.get_state()
    await state.update_data(otvet3=message.text)
    data = await state.get_data()
    otvet = data['otvet3']
    print(otvet)
    print(cor_otv[2][0])
    try:
        number = int(otvet)
        await state.clear()
        if number == int(cor_otv[2][0]):
            cursor.execute("SELECT score FROM users WHERE id_user = (?)", [id_user])
            score_first = cursor.fetchall()
            score_new = score_first[0][0] + 1
            print(score_new)
            cursor.execute("UPDATE users SET score = (?) WHERE id_user = (?)", [score_new, id_user])
            con.commit()
            await message.answer(text='Вы решили верно!')
        else:
            fot2 = f'{foto_answ[2][0]}.jpg'
            task_image2 = FSInputFile(fot2)
            await message.answer(text='К сожалению вы решили не верно.\nВот правильное решение:')
            await message.answer_photo(photo=task_image2, reply_markup=types.ReplyKeyboardRemove())
        await message.answer(text='Для того, чтобы вернуться в меню, введите команду /menu\nДля того, чтобы вернуться в начало,введите команду /start')
    except ValueError:
        await message.answer(text='Округлите число до целого')
        return