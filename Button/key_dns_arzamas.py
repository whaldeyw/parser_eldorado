from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

key_smartphone = KeyboardButton('/Смартфоны_Арзамас')
key_tv = KeyboardButton('/Телевизоры_и_мониторы_Арзамас')
key_note_book = KeyboardButton('/Ноутбуки_Арзамас')
key_holod_chai = KeyboardButton('/Холодильники_и_чайники_Арзамас')
key_different = KeyboardButton('/Разное_Арзамас')
back_key_region = KeyboardButton('/Назад_Регион')

key_dns_arzamas =ReplyKeyboardMarkup(resize_keyboard=True).row(key_smartphone, key_tv , key_note_book).row(key_holod_chai, key_different).add(back_key_region)