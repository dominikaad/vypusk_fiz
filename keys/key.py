from aiogram import types

kb_start = [
    types.KeyboardButton(text='Мои данные'),
    types.KeyboardButton(text='Меню')
]

kb_choise = [
    types.KeyboardButton(text='Выбрать раздел физики'),
    types.KeyboardButton(text='Тест')
]

kb_razdel_fiz = [
    types.InlineKeyboardButton(text='Механика', callback_data='meh_1'),
    types.InlineKeyboardButton(text='Молекулярная физика', callback_data='mol_2'),
    types.InlineKeyboardButton(text='Электродинамика', callback_data='el_dyn_3'),
    types.InlineKeyboardButton(text='Колебания и волны', callback_data='kol_voln_4'),
    types.InlineKeyboardButton(text='Оптика', callback_data='opt_5'),
    types.InlineKeyboardButton(text='Назад', callback_data='exit_res')
]

kb_redaktir = [
    types.InlineKeyboardButton(text='Изменить имя', callback_data='name_zamena'),
    types.InlineKeyboardButton(text='Изменить класс', callback_data='class_zamena'),
    types.InlineKeyboardButton(text='Назад', callback_data='exit_res')
]

kb_mech = [
    types.KeyboardButton(text='Тест по теме "Механика"'),
    types.KeyboardButton(text='Нет')
]

kb_molek = [
    types.KeyboardButton(text='Тест по теме "Молекулярная физика"'),
    types.KeyboardButton(text='Нет')
]

kb_elekdyn = [
    types.KeyboardButton(text='Тест по теме "Электродинамика"'),
    types.KeyboardButton(text='Нет')
]

kb_optyka = [
    types.KeyboardButton(text='Тест по теме "Оптика"'),
    types.KeyboardButton(text='Нет')
]

kb_koleb = [
    types.KeyboardButton(text='Тест по теме "Колебания и волны"'),
    types.KeyboardButton(text='Нет')
]