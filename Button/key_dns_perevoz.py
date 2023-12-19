from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

key_perevoz = KeyboardButton('/Перевоз')
key_arzamas = KeyboardButton('/Арзамас')
key_back_shop = KeyboardButton('/Назад_Магазины')
key_dns_region = ReplyKeyboardMarkup(resize_keyboard=True).row(key_perevoz, key_arzamas).add(key_back_shop)


key_smartphone = KeyboardButton('/Смартфоны_Перевоз')
key_tv = KeyboardButton('/Телевизоры_и_мониторы')
key_note_book = KeyboardButton('/Ноутбуки')
key_holod_chai = KeyboardButton('/Холодильники_и_чайники')
key_different = KeyboardButton('/Разное')
back_key_region = KeyboardButton('/Назад_Регион')


key_dns_perevoz =ReplyKeyboardMarkup(resize_keyboard=True).row(key_smartphone, key_tv , key_note_book).row(key_holod_chai, key_different).add(back_key_region)
