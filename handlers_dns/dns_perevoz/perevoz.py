from creat_bot import dp, bot
from aiogram import types, Dispatcher
from Button.key_dns_perevoz import  key_dns_region
from Button.key_start import key_start1
from Button.key_dns_perevoz import key_dns_perevoz

async def dns(message: types.Message):
        await  bot.send_message(message.from_user.id, f'Отлично! 👍 Теперь выбери населенный пункт со скидками 🏙 '
                                                      f'Количество населенных пунктов будет увеличиваться 📈 \n'
                                                      f'Если открыть ссылку на товар то в пункте: В наличии '
                                                      f'можно посмотреть есть ли такой товар рядом с вами или соседнем городе 🛰'
                                                      , reply_markup=key_dns_region)

async def mes_back_el(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.full_name} 👋 \nЯ \U0001F916 который найдет для вас '
                                                      f'все скидки в магазинах электроники.\nЖми кнопки внизу 👇 и выбери магазин,'
                                                      f' и узнай скидки которые сейчас есть ', reply_markup=key_start1)

async def menu_perevoz(message: types.Message):
    await  bot.send_message(message.from_user.id, f'\U0001F916 подобрал для вас скидки  по  категориям ниже 👇\n',
                                                                                reply_markup=key_dns_perevoz)


async def back_region(message: types.Message):
    await  bot.send_message(message.from_user.id, f'Отлично! 👍 Теперь выбери населенный пункт со скидками 🏙 '
                                                  f'Количество населенных пунктов будет увеличиваться 📈 \n'
                                                  f'Если открыть ссылку на товар то в пункте: В наличии '
                                                  f'можно посмотреть есть ли такой товар рядом с вами или соседнем городе 🛰'
                                                    , reply_markup=key_dns_region)

def register_handlers_dns(dp : Dispatcher):
    dp.register_message_handler(dns, commands=['DNS'])
    dp.register_message_handler(mes_back_el, commands=['Назад_Магазины'])
    dp.register_message_handler(menu_perevoz, commands=['Перевоз'])
    dp.register_message_handler(back_region, commands=['Назад_Регион'])
