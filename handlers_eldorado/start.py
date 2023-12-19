from creat_bot import dp, bot
from aiogram import types, Dispatcher
from Button.key_start import key_start1, key_eldorado_menu




# @dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
        await  bot.send_message(message.from_user.id, f'Привет {message.from_user.full_name} 👋 \nЯ \U0001F916 , который найдет для вас '
                                                      f'все скидки в магазинах электроники.\nЖми кнопки внизу 👇 и выбери магазин,'
                                                      f' и узнай скидки которые сейчас есть ', reply_markup=key_start1)

# @dp.message_handler(commands=['Эльдорадо'])
async def mes_eldorado(message: types.Message):
    await  bot.send_message(message.from_user.id, f'Отлично! 👍 Теперь выбери категорию и узнай какие сейчас есть скидки 💰', reply_markup=key_eldorado_menu)

# @dp.message_handler(commands=['Назад_Магазины'])
async def mes_back_el(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.full_name} 👋 \nЯ \U0001F916 который найдет для вас '
                                                      f'все скидки в магазинах электроники.\nЖми кнопки внизу 👇 и выбери магазин,'
                                                      f' и узнай скидки которые сейчас есть ', reply_markup=key_start1)


def register_handlers_start(dp : Dispatcher):
    dp.register_message_handler(mes_start, commands=['start'])
    dp.register_message_handler(mes_eldorado, commands=['Эльдорадо'])
    dp.register_message_handler(mes_back_el, commands=['Назад_Магазины'])

