from aiogram import executor
from creat_bot import dp


async def on_startup(_):
    print('Бот вышел онлайн')


from handlers_eldorado import home_el, sale_50, kitchen, tv, smartphone, gadgets, beauty, service, comp, start

start.register_handlers_start(dp)
home_el.register_handlers_home(dp)
sale_50.register_handlers_sale_50(dp)
kitchen.register_handlers_kitchen(dp)
tv.register_handlers_tv(dp)
smartphone.register_handlers_smartphone(dp)
gadgets.register_handlers_gadgets(dp)
comp.register_handlers_comp(dp)
beauty.register_handlers_beauty(dp)
service.register_handlers_service(dp)

from handlers_dns.dns_perevoz import perevoz, smartfone_perevoz, tv_monitor_perevoz, note_book, holod_chai, different

perevoz.register_handlers_dns(dp)
smartfone_perevoz.register_handlers_smart_per(dp)
tv_monitor_perevoz.register_handlers_tv_per(dp)
note_book.register_handlers_note_book(dp)
holod_chai.register_handlers_cholod_chai(dp)
different.register_handlers_different(dp)

from handlers_dns.dns_arzamas import tv_monitors_arzamas, Arzamas, holod_chai_arz, note_book_arzamas, smartphone_arzamas, different_arzamas

tv_monitors_arzamas.register_handlers_tv_arz(dp)
Arzamas.register_handlers_arzamas(dp)
holod_chai_arz.register_handlers_cholod_chai_arz(dp)
note_book_arzamas.register_handlers_note_book_arz(dp)
smartphone_arzamas.register_handlers_smart_arz(dp)
different_arzamas.register_handlers_different_arz(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
