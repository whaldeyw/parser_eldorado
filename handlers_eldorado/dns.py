import csv
import json

from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from time import sleep



from creat_bot import dp, bot, Dispatcher
from aiogram import types
# from Button.key_eldorado import key_back_eldorado


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
url = f"https://www.dns-shop.ru/catalog/actions/?category=17a8ae4916404e77&mode=simple"
driver.get(url)


sleep(4)

with open('e.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(
                (
                        'Дата',
                        'Город',

                )
        )


        # all = driver.find_elements(By.TAG_NAME, 'a')
        # for i in all:
        #         name = i.find_elements(By.TAG_NAME, 'span')
        #         if name == []:
        #                 continue
        #         else:
        #                 name = i.find_element(By.TAG_NAME, 'span')
        #
        #         link =i.get_attribute('href')
        #         if link == None:
        #                 continue
        #         elif link == 'javascript:':
        #                 continue
        #         else:
        #                 link = i.get_attribute('href')

                        # print(f'{name.text}\n{link}')


        dict1 = []
        price_all = driver.find_element(By.CLASS_NAME, 'products-list ').find_element(By.TAG_NAME, 'div')
        nav = price_all.find_elements(By.TAG_NAME, 'span')
        for n in nav:
                ne = n.text

                with open('e.csv', 'a', encoding='utf-8') as file:
                        writer = csv.writer(file)

                        writer.writerow(
                                (
                                        ne,


                                )
                        )


        href = driver.find_element(By.CLASS_NAME, 'products-list ').find_element(By.TAG_NAME, 'div').find_elements(By.TAG_NAME, 'a')

        for i in href:
                link = i.get_attribute('href')
                if link == None:
                        continue
                elif link == 'javascript:':
                        continue
                else:
                        link = i.get_attribute('href')

                        with open('e.csv', 'a', encoding='utf-8') as file:
                                writer = csv.writer(file)

                                writer.writerow(
                                        (

                                                link,


                                        )
                                )

