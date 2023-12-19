import pickle
from selenium import webdriver
from selenium_stealth import stealth
from time import sleep



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
url = "https://www.dns-shop.ru/catalog/actions/?stock=now&category=17a8a01d16404e77&action=tovarysoskidkoj&p"
driver.get(url)
sleep(15)
pickle.dump(driver.get_cookies(), open('cookie_arzamas', 'wb'))
print('куки загружены')