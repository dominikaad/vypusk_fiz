from aiogram.types import Message
from aiogram import F
from aiogram import types
from loader import router, cursor, con
from aiogram.types import FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

class Form_reg(StatesGroup):
    otv_1 = State()
    otv_2 = State()
    otv_3 = State()
    otv_4 = State()
    otv_5 = State()
    otv_6 = State()
    otv_7 = State()

@router.message(F.text == 'Тест')
async def test_mech(message: Message, state: FSMContext):
    await state.clear()
    cursor.execute("INSERT INTO test_11kl (number, uslov, otvet) VALUES (1, 'data/images/test_1', 6)")
    con.commit()
    cursor.execute("SELECT number FROM test_11kl")
    num = cursor.fetchall()
    cursor.execute("SELECT uslov FROM test_11kl")
    uslov = cursor.fetchall()
    await message.answer(f'Задача №{num[0][0]}\nВведите только число, округленное по математическим правилам')
    fot1 = f'{uslov[0][0]}.pdf'
    task_image1 = FSInputFile(fot1)
    await state.set_state(Form_reg.otv_1)
    await message.answer_photo(photo=task_image1, reply_markup=types.ReplyKeyboardRemove())

@router.message(Form_reg.otv_1)
async def get_fio(message: Message, state: FSMContext):
    id_user = message.chat.id
    cursor.execute("SELECT otvet FROM test_11kl")
    cor_otv = cursor.fetchall()
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
            await message.answer(text=f'К сожалению вы решили не верно.\nПравильный ответ:{int(cor_otv[0][0])}',reply_markup=types.ReplyKeyboardRemove())
        cursor.execute("SELECT number FROM test_11kl")
        num = cursor.fetchall()
        cursor.execute("SELECT uslov FROM test_11kl")
        uslov = cursor.fetchall()
        await message.answer(f'Задача №{num[1][0]}\nВведите только число, округленное по математическим правилам')
        fot1 = f'{uslov[1][0]}.pdf'
        task_image1 = FSInputFile(fot1)
        await state.set_state(Form_reg.otv_2)
        await message.answer_photo(photo=task_image1, reply_markup=types.ReplyKeyboardRemove())
    except ValueError:
        await message.answer(text='Округлите число до целого')
        return

@router.message(Form_reg.otv_2)
async def get_fio(message: Message, state: FSMContext):
    id_user = message.chat.id
    cursor.execute("SELECT otvet FROM test_11kl")
    cor_otv = cursor.fetchall()
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
            await message.answer(text=f'К сожалению вы решили не верно.\nПравильный ответ:{int(cor_otv[1][0])}',
                                 reply_markup=types.ReplyKeyboardRemove())
        cursor.execute("SELECT number FROM test_11kl")
        num = cursor.fetchall()
        cursor.execute("SELECT uslov FROM test_11kl")
        uslov = cursor.fetchall()
        await message.answer(f'Задача №{num[2][0]}\nВведите только число, округленное по математическим правилам')
        fot1 = f'{uslov[2][0]}.pdf'
        task_image1 = FSInputFile(fot1)
        await state.set_state(Form_reg.otv_3)
        await message.answer_photo(photo=task_image1, reply_markup=types.ReplyKeyboardRemove())
    except ValueError:
        await message.answer(text='Округлите число до целого')
        return

@router.message(Form_reg.otv_3)
async def get_fio(message: Message, state: FSMContext):
    id_user = message.chat.id
    cursor.execute("SELECT otvet FROM test_11kl")
    cor_otv = cursor.fetchall()
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
            await message.answer(text=f'К сожалению вы решили не верно.\nПравильный ответ:{int(cor_otv[2][0])}',
                                 reply_markup=types.ReplyKeyboardRemove())
        cursor.execute("SELECT number FROM test_11kl")
        num = cursor.fetchall()
        cursor.execute("SELECT uslov FROM test_11kl")
        uslov = cursor.fetchall()
        await message.answer(f'Задача №{num[3][0]}\nВведите только число, округленное по математическим правилам')
        fot1 = f'{uslov[3][0]}.pdf'
        task_image1 = FSInputFile(fot1)
        await state.set_state(Form_reg.otv_4)
        await message.answer_photo(photo=task_image1, reply_markup=types.ReplyKeyboardRemove())
    except ValueError:
        await message.answer(text='Округлите число до целого')
        return

@router.message(Form_reg.otv_4)
async def get_fio(message: Message, state: FSMContext):
    id_user = message.chat.id
    cursor.execute("SELECT otvet FROM test_11kl")
    cor_otv = cursor.fetchall()
    a = await state.get_state()
    await state.update_data(otvet4=message.text)
    data = await state.get_data()
    otvet = data['otvet4']
    print(otvet)
    print(cor_otv[3][0])
    try:
        number = int(otvet)
        await state.clear()
        if number == int(cor_otv[3][0]):
            cursor.execute("SELECT score FROM users WHERE id_user = (?)", [id_user])
            score_first = cursor.fetchall()
            score_new = score_first[0][0]+1
            print(score_new)
            cursor.execute("UPDATE users SET score = (?) WHERE id_user = (?)", [score_new, id_user])
            con.commit()
            await message.answer(text='Вы решили верно!')
        else:
            await message.answer(text=f'К сожалению вы решили не верно.\nПравильный ответ:{int(cor_otv[3][0])}',
                                 reply_markup=types.ReplyKeyboardRemove())
        cursor.execute("SELECT number FROM test_11kl")
        num = cursor.fetchall()
        cursor.execute("SELECT uslov FROM test_11kl")
        uslov = cursor.fetchall()
        await message.answer(f'Задача №{num[4][0]}\nВведите только число, округленное по математическим правилам')
        fot1 = f'{uslov[4][0]}.pdf'
        task_image1 = FSInputFile(fot1)
        await state.set_state(Form_reg.otv_5)
        await message.answer_photo(photo=task_image1, reply_markup=types.ReplyKeyboardRemove())
    except ValueError:
        await message.answer(text='Округлите число до целого')
        return

@router.message(Form_reg.otv_5)
async def get_fio(message: Message, state: FSMContext):
    id_user = message.chat.id
    cursor.execute("SELECT otvet FROM test_11kl")
    cor_otv = cursor.fetchall()
    a = await state.get_state()
    await state.update_data(otvet5=message.text)
    data = await state.get_data()
    otvet = data['otvet5']
    print(otvet)
    print(cor_otv[4][0])
    try:
        number = int(otvet)
        await state.clear()
        if number == int(cor_otv[4][0]):
            cursor.execute("SELECT score FROM users WHERE id_user = (?)", [id_user])
            score_first = cursor.fetchall()
            score_new = score_first[0][0]+1
            print(score_new)
            cursor.execute("UPDATE users SET score = (?) WHERE id_user = (?)", [score_new, id_user])
            con.commit()
            await message.answer(text='Вы решили верно!')
        else:
            await message.answer(text=f'К сожалению вы решили не верно.\nПравильный ответ:{int(cor_otv[4][0])}',
                                 reply_markup=types.ReplyKeyboardRemove())
        cursor.execute("SELECT number FROM test_11kl")
        num = cursor.fetchall()
        cursor.execute("SELECT uslov FROM test_11kl")
        uslov = cursor.fetchall()
        await message.answer(f'Задача №{num[5][0]}\nВведите только число, округленное по математическим правилам')
        fot1 = f'{uslov[5][0]}.pdf'
        task_image1 = FSInputFile(fot1)
        await state.set_state(Form_reg.otv_6)
        await message.answer_photo(photo=task_image1, reply_markup=types.ReplyKeyboardRemove())
    except ValueError:
        await message.answer(text='Округлите число до целого')
        return

@router.message(Form_reg.otv_6)
async def get_fio(message: Message, state: FSMContext):
    id_user = message.chat.id
    cursor.execute("SELECT otvet FROM test_11kl")
    cor_otv = cursor.fetchall()
    a = await state.get_state()
    await state.update_data(otvet6=message.text)
    data = await state.get_data()
    otvet = data['otvet6']
    print(otvet)
    print(cor_otv[5][0])
    try:
        number = int(otvet)
        await state.clear()
        if number == int(cor_otv[5][0]):
            cursor.execute("SELECT score FROM users WHERE id_user = (?)", [id_user])
            score_first = cursor.fetchall()
            score_new = score_first[0][0] + 1
            print(score_new)
            cursor.execute("UPDATE users SET score = (?) WHERE id_user = (?)", [score_new, id_user])
            con.commit()
            await message.answer(text='Вы решили верно!')
        else:
            await message.answer(text=f'К сожалению вы решили не верно.\nПравильный ответ:{int(cor_otv[5][0])}',
                                 reply_markup=types.ReplyKeyboardRemove())
        cursor.execute("SELECT number FROM test_11kl")
        num = cursor.fetchall()
        cursor.execute("SELECT uslov FROM test_11kl")
        uslov = cursor.fetchall()
        await message.answer(f'Задача №{num[6][0]}\nВведите только число, округленное по математическим правилам')
        fot1 = f'{uslov[6][0]}.pdf'
        task_image1 = FSInputFile(fot1)
        await state.set_state(Form_reg.otv_7)
        await message.answer_photo(photo=task_image1, reply_markup=types.ReplyKeyboardRemove())
    except ValueError:
        await message.answer(text='Округлите число до целого')
        return


@router.message(Form_reg.otv_7)
async def get_fio(message: Message, state: FSMContext):
    id_user = message.chat.id
    cursor.execute("SELECT otvet FROM test_11kl")
    cor_otv = cursor.fetchall()
    a = await state.get_state()
    await state.update_data(otvet7=message.text)
    data = await state.get_data()
    otvet = data['otvet7']
    print(otvet)
    print(cor_otv[6][0])
    try:
        number = int(otvet)
        await state.clear()
        if number == int(cor_otv[6][0]):
            cursor.execute("SELECT score FROM users WHERE id_user = (?)", [id_user])
            score_first = cursor.fetchall()
            score_new = score_first[0][0] + 1
            print(score_new)
            cursor.execute("UPDATE users SET score = (?) WHERE id_user = (?)", [score_new, id_user])
            con.commit()
            await message.answer(text='Вы решили верно!')
        else:
            await message.answer(text=f'К сожалению вы решили не верно.\nПравильный ответ:{int(cor_otv[6][0])}',
                                 reply_markup=types.ReplyKeyboardRemove())
        await message.answer(text='Для того, чтобы вернуться в меню, введите команду /menu\nДля того, чтобы вернуться в начало,введите команду /start')
    except ValueError:
        await message.answer(text='Округлите число до целого')
        return