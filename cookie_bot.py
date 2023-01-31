from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

###############################################################

chrome_driver_path = "E:/desenvolveaqui/chromedriver.exe"
url = "https://orteil.dashnet.org/experiments/cookie/"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url)

###############################################################

prices = {}
my_money = 0
buy = False
next_buy = 0

###############################################################
cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')
while True:

    # Count THE MONEY
    try:
        my_money = float(driver.find_element(By.XPATH, '//*[@id="money"]').text)

        # Click on the cookie
        cookie.click()
    except:
        pass
    # Look at the store
    buy = False
    try:
        for item in driver.find_elements(By.CSS_SELECTOR, 'div#store b'):
            word = ''
            try:
                for i in item.text:
                    if i.isdigit():
                        word += i
            finally:

                # Updating the prices' dict
                try:
                    prices[float(word)] = item
                except:
                    pass

                # Checking the possibility to buy
                else:
                    if my_money >= float(word):
                        next_buy = float(word)
                        buy = True

        # Time to buy!!!
        if buy:
            try:
                prices[next_buy].click()
            except:
                pass
    except:
        pass
