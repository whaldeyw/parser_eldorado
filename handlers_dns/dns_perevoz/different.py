from  bs4 import  BeautifulSoup
import json
import pickle
from selenium import webdriver
from selenium_stealth import stealth
from time import sleep
from creat_bot import dp, bot, Dispatcher
from aiogram import types

async def different(message: types.Message):

        await bot.send_message(message.from_user.id, 'Начинаю загрузку...🚀')
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("--headless")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(options=options)

        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        # url = "https://www.dns-shop.ru/catalog/actions/?stock=now&category=17a8a01d16404e77&action=tovarysoskidkoj&p"
        # driver.get(url)
        # sleep(15)
        # pickle.dump(driver.get_cookies(), open('session', 'wb'))
        # print('куки загружены')

        url = f"https://www.dns-shop.ru/catalog/actions/?stock=now-today-tomorrow&category=d910c1f939147fd7-17a9a71416404e77-17a8c90516404e77-17a8cc6516404e77-17a8c89d16404e77-17a8d5ad16404e77-17a8c9a416404e77-17a8ccd016404e77-17a8cd3716404e77-c0deef7739157fd7-17a8face16404e77-c01df46f39137fd7-17a8cadf16404e77-17a897ed16404e77&action=rassrockailivygoda-tovarysoskidkoj"
        driver.get(url)
        for cookies in pickle.load(open('session', 'rb')):
                driver.add_cookie(cookies)
        driver.refresh()
        sleep(2)
        PageSourse = driver.page_source
        soup = BeautifulSoup(PageSourse, 'lxml')
        try:
                page = soup.find_all('a', class_='pagination-widget__page-link')[-3].text
        except:
                page = 1
        await bot.send_message(message.from_user.id, f'Найдено(а) {str(page)} страница(ы) 🗒 с товаром\nОтберу для вас только лучшее предложение')
        for i in range(int(page)):

                url = f"https://www.dns-shop.ru/catalog/actions/?stock=now-today-tomorrow&category=d910c1f939147fd7-17a9a71416404e77-17a8c90516404e77-17a8cc6516404e77-17a8c89d16404e77-17a8d5ad16404e77-17a8c9a416404e77-17a8ccd016404e77-17a8cd3716404e77-c0deef7739157fd7-17a8face16404e77-c01df46f39137fd7-17a8cadf16404e77-17a897ed16404e77&action=rassrockailivygoda-tovarysoskidkoj&p={i}"
                driver.get(url)

                sleep(1)
                PageSourse = driver.page_source
                soup = BeautifulSoup(PageSourse, 'lxml')
                all = soup.find_all(class_='catalog-product ui-button-widget')
                sleep(4)

                for items in all:
                        try:
                                proc = items.find('span', 'catalog-product__discount-vobler w-product-discount-voblers').text.replace('-','').replace('%', '')
                                if int(proc) > 10:

                                        name = items.find('a', class_='catalog-product__name ui-link ui-link_black').text
                                        new_pric = items.find('div', class_='product-buy__price product-buy__price_active').text.split()
                                        a = new_pric[0]
                                        b = new_pric[1]
                                        c = f'{a}{b}'
                                        new_price = f'Новая цена: {c} руб'
                                        old_pric = items.find('span', class_='product-buy__prev').text
                                        t = old_pric.split()
                                        e = t[0]
                                        f = t[1]
                                        g = f'{e}{f}'
                                        sum = int(c)- int(g)
                                        summ = f'Скидка составила: {sum} руб'
                                        old_price = f'Старая цена: {old_pric}'
                                        pro = items.find('span', 'catalog-product__discount-vobler w-product-discount-voblers').text
                                        procent = f'Процент скидки: {pro}'
                                        lin = items.find('a', class_='catalog-product__name ui-link ui-link_black').get('href')
                                        link = f'https://www.dns-shop.ru{lin}'

                                        # print(f'{name}\n{new_price}\n{old_price}\n{summ}\n{procent}\n{link}')
                                        sleep(0.5)

                                        await bot.send_message(message.from_user.id, f'{name}\n{new_price}\n{old_price}\n{summ}\n{procent}\n{link}')

                        except:
                              continue

def register_handlers_different(dp: Dispatcher):
    dp.register_message_handler(different, commands=['Разное'])


