
import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)








# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
#
# # options.add_argument("--headless")
#
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# driver = webdriver.Chrome(options=options)
#
# stealth(driver,
#         languages=["en-US", "en"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#         )
# url = f"https://www.eldorado.ru/promo/podarki-so-skidkami-home/"
# driver.get(url)
#
# sleep(4)
#
# all = driver.find_elements(By.CLASS_NAME,'eld-card-info')
# for i in all:
#         name =i.find_element(By.CLASS_NAME, 'eld-card-title').text
#         old_price = i.find_element(By.CLASS_NAME, 'eld-card-price-old-value').text
#         new_price = i.find_element(By.CLASS_NAME, 'eld-card-price-actual-value').text
#         summ_sale = i.find_element(By.CLASS_NAME, 'eld-card-price-difference').text
#         href = i.find_element(By.TAG_NAME, 'a' ).get_attribute('href')
#         print(f'{name}\nСтарая цена: {old_price} / Новая цена: {new_price}\n'
#               f'Сумма скидки: {summ_sale}\n{href}')
#         sleep(1)






# all = driver.find_elements(By.CLASS_NAME, 'lj')
# for i in all:
#         dict = []
#         name = i.find_elements(By.CLASS_NAME, 'yj')
#         for item in name:
#                 name2 = item.get_attribute('title')
#                 dict.append(name2)
#                 sleep(1)
#         dict2 = []
#         all_href = i.find_elements(By.CLASS_NAME,'lj')
#         for item in all_href:
#                 hre = item.find_elements(By.TAG_NAME, 'a')
#                 for items in hre:
#                         href = items.get_attribute('href')
#                         dict2.append(href)
#                         sleep(1)
#
#                         print(f'{dict} {dict2}')



# with open("us.json", 'r', encoding='utf-8') as f_o:
#         data_from_json = json.load(f_o)




# all_name = driver.find_elements(By.CLASS_NAME, 'lj')
# for i in all_name:
#         name = i.get_attribute('title')
#         sleep(1)
#         print(name)


# all_href = driver.find_elements(By.CLASS_NAME, 'lj')
# for i in all_href:
#         href = i.find_elements(By.TAG_NAME, 'a')
#         for item in href:
#                 href2 = item.get_attribute('href')
#
#                 sleep(1)



# sleep(1)
# driver.quit()

