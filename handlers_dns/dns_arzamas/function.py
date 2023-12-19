from  bs4 import  BeautifulSoup
import pickle
from selenium import webdriver
from selenium_stealth import stealth
from time import sleep

def get_data():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    #options.add_argument("--headless")
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

    url = f"https://www.dns-shop.ru/catalog/actions/?stock=now-today-tomorrow&category=d910c1f939147fd7-17a9a71416404e77-17a8c90516404e77-17a8cc6516404e77-17a8c89d16404e77-17a8d5ad16404e77-17a8c9a416404e77-17a8ccd016404e77-17a8cd3716404e77-c0deef7739157fd7-17a8face16404e77-c01df46f39137fd7-17a8cadf16404e77-17a897ed16404e77&action=rassrockailivygoda-tovarysoskidkoj"
    return driver.get(url)

def cookies():

    for cookies in pickle.load(open('cookie_arzamas', 'rb')):

        driver.add_cookie(cookies)
    driver.refresh()
    sleep(2)


if __name__=="__main__":
    get_data()