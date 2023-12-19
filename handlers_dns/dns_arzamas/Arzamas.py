from creat_bot import dp, bot
from aiogram import types, Dispatcher
from Button.key_dns_perevoz import  key_dns_region
from Button.key_dns_arzamas import key_dns_arzamas

async def menu_arzamas(message: types.Message):
    await  bot.send_message(message.from_user.id, f'\U0001F916 подобрал для вас скидки по категориям ниже 👇\n',
                                                                                reply_markup=key_dns_arzamas)


async def back_region(message: types.Message):
    await  bot.send_message(message.from_user.id, f'Отлично! 👍 Теперь выбери населенный пункт со скидками 🏙 '
                                                  f'Количество населенных пунктов будет увеличиваться 📈 \n'
                                                  f'Если открыть ссылку на товар то в пункте: В наличии '
                                                  f'можно посмотреть есть ли такой товар рядом с вами или соседнем городе 🛰'
                                                    , reply_markup=key_dns_region)

def register_handlers_arzamas(dp : Dispatcher):
    dp.register_message_handler(menu_arzamas, commands=['Арзамас'])
    dp.register_message_handler(back_region, commands=['Назад_Регион'])