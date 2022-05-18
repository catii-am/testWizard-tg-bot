import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver.v2 as uc

def wait_element(path, timeout=20):
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, path))
    )

options = uc.ChromeOptions()
options.add_argument('--no-first-run')
options.add_argument('--no-service-autorun')
options.add_argument('--password-store=basic')
driver = uc.Chrome(
    options=options
)
test_id = '14850'
driver.get(f'https://www.testwizard.ru/test.php?id={test_id}')
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/table/tbody/tr[3]/td/form/a').click()
id = 0
complete = 0
while True:

    if len(driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/table/tbody/tr[2]/td/p[2]/a')) > 0:
        break

    # time.sleep(5)
    id = 0
    complete = 0
    try:
        quest_1 = driver.find_element(By.ID, 'r1')
        if quest_1.get_attribute('value') != '0' and complete == 0:
            quest_1.click()
            complete = 1
            print('1')
        id += 1
    except Exception as ex:
        print(ex)
        continue

    try:
        quest_2 = driver.find_element(By.ID, 'r2')
        if quest_2.get_attribute('value') != '0' and complete == 0:
            quest_2.click()
            complete = 1
            print('2')
        id += 1
    except Exception as ex:
        print(ex)
        continue

    try:
        quest_3 = driver.find_element(By.ID, 'r3')
        if quest_3.get_attribute('value') != '0' and complete == 0:
            quest_3.click()
            complete = 1
            print('3')
        id += 1
    except Exception as ex:
        print(ex)
        continue

    try:
        quest_4 = driver.find_element(By.ID, 'r4')
        if quest_4.get_attribute('value') != '0' and complete == 0:
            quest_4.click()
            complete = 1
            print('4')
        id += 1
    except Exception as ex:
        print(ex)
        continue

    # try:
    #     quest_5 = driver.find_element(By.ID, 'r5')
    #     if quest_5.get_attribute('value') != '0' and complete == 0:
    #         quest_5.click()
    #         complete = 1
    #     id += 1
    # except Exception as ex:
    #     print(ex)
    #     continue
    #
    # try:
    #     quest_6 = driver.find_element(By.ID, 'r6')
    #     if quest_6.get_attribute('value') != '0' and complete == 0:
    #         quest_6.click()
    #         complete = 1
    #     id += 1
    # except Exception as ex:
    #     print(ex)
    #     continue

    if complete == 0:
        driver.find_element(By.XPATH, f'//*[@id="r{random.randint(1, id)}"]').click()