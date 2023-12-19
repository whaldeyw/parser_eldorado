from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from time import sleep
from creat_bot import dp, bot, Dispatcher
from aiogram import types

async def comp(message: types.Message):
    await bot.send_message(message.from_user.id, 'Начинаю загрузку...')

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
    url = f"https://www.eldorado.ru/promo/podarki-so-skidkami-office/"
    driver.get(url)



    sleep(4)

    all = driver.find_elements(By.CLASS_NAME, 'eld-card-info')
    for i in all:
        name = i.find_element(By.CLASS_NAME, 'eld-card-title').text
        old_price = i.find_element(By.CLASS_NAME, 'eld-card-price-old-value').text
        new_price = i.find_element(By.CLASS_NAME, 'eld-card-price-actual-value').text
        summ_sale = i.find_element(By.CLASS_NAME, 'eld-card-price-difference').text
        href = i.find_element(By.TAG_NAME, 'a').get_attribute('href')

        sleep(1)


        await bot.send_message(message.from_user.id, f'{name}\nСтарая цена: {old_price} / Новая цена: {new_price}\n'
                                                 f'Сумма скидки: {summ_sale}\n{href}')

def register_handlers_comp(dp: Dispatcher):
    dp.register_message_handler(comp, commands=['Компы_Ноутбуки_Мониторы_и_тд'])