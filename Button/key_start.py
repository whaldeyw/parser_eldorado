from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

key_start = KeyboardButton('/Эльдорадо')
key_start2 = KeyboardButton('/DNS')
key_eldorado = KeyboardButton('/Назад_Магазины')


key_start1 =ReplyKeyboardMarkup(resize_keyboard=True).add(key_start).add(key_start2)

key_sale_50 = KeyboardButton('/Скидки_до_50%')
key_beuty = KeyboardButton('/Красота_и_Здоровье')
key_comp = KeyboardButton('/Компы_Ноутбуки_Мониторы_и_тд')
key_dadgest = KeyboardButton('/Гаджеты')
key_home_el = KeyboardButton('/Техника_для_дома')
key_kitchen = KeyboardButton('/Кухня')
key_service = KeyboardButton('/Аксессуары_и_сервисы')
key_smartphone = KeyboardButton('/Смартфоны')
key_tv = KeyboardButton('/Телевизоры,Аудиотехника')





key_eldorado_menu =ReplyKeyboardMarkup(resize_keyboard=True).row(key_sale_50, key_smartphone,  key_dadgest)\
    .add(key_home_el,  key_comp,).row(key_kitchen,key_service,key_beuty).add(key_eldorado)


