import re
import telebot
import random

from selenium.webdriver.common.by import By
import undetected_chromedriver.v2 as uc

token = '5283783694:AAH21JOHdTjOUmikzDxLWhnhxp3G6pZTek8'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f'Привет, отправь мне ID или ссылку на тест')

@bot.message_handler()
def com(message):
    if message.text != 'Получить ID':
        options = uc.ChromeOptions()
        options.add_argument('--no-first-run')
        options.add_argument('--no-service-autorun')
        options.add_argument('--password-store=basic')
        driver = uc.Chrome(
            options=options
        )

        test_id = re.split('=|,', f'{message.text}')[-1]
        driver.get(f'https://www.testwizard.ru/test.php?id={test_id}')
        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/table/tbody/tr[3]/td/form/a').click()
        id = 0
        complete = 0
        quest_num = 1
        while True:
            if len(driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/table/tbody/tr[2]/td/p[2]/a')) > 0:
                driver.quit()
                break
            # time.sleep(10000)
            quest_text = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[1]/td/div/div').text

            id = 0
            complete = 0
            ex_id = 0
            try:
                quest_1 = driver.find_element(By.ID, 'r1')
                if quest_1.get_attribute('value') != '0' and complete == 0:
                    # quest_otvet_1 = driver.find_element('//*[@id="r1"]').text
                    quest_otvet_1 = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div').text
                    quest_1.click()
                    bot.send_message(message.chat.id, f'Вопрос №{quest_num}\n{quest_text}\nОтвет №1: {quest_otvet_1}')
                    complete = 1
                    quest_num += 1
                    print('1')
                id += 1
            except Exception as ex:
                print(ex)
                ex_id += 1
                continue

            try:
                quest_2 = driver.find_element(By.ID, 'r2')
                if quest_2.get_attribute('value') != '0' and complete == 0:
                    quest_otvet_2 = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div').text
                    quest_2.click()
                    bot.send_message(message.chat.id, f'Вопрос №{quest_num}\n{quest_text}\nОтвет №2: {quest_otvet_2}')
                    complete = 1
                    quest_num += 1
                    print('2')
                id += 1
            except Exception as ex:
                print(ex)
                ex_id += 1
                continue

            try:
                quest_3 = driver.find_element(By.ID, 'r3')
                if quest_3.get_attribute('value') != '0' and complete == 0:
                    quest_otvet_3 = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[3]/td/div').text
                    quest_3.click()
                    bot.send_message(message.chat.id, f'Вопрос №{quest_num}\n{quest_text}\nОтвет №3: {quest_otvet_3}')
                    complete = 1
                    quest_num += 1
                    print('3')
                id += 1
            except Exception as ex:
                print(ex)
                ex_id += 1
                continue

            try:
                quest_4 = driver.find_element(By.ID, 'r4')
                if quest_4.get_attribute('value') != '0' and complete == 0:
                    quest_otvet_4 = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[4]/td/div').text
                    quest_4.click()
                    bot.send_message(message.chat.id, f'Вопрос №{quest_num}\n{quest_text}\nОтвет №4: {quest_otvet_4}')
                    complete = 1
                    quest_num += 1
                    print('4')
                id += 1
            except Exception as ex:
                print(ex)
                ex_id += 1
                continue

            # try:
            #     quest_5 = driver.find_element(By.ID, 'r5')
            #     if quest_5.get_attribute('value') != '0' and complete == 0:
            #         quest_otvet_5 = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[5]/td/div').text
            #         quest_5.click()
            #         bot.send_message(message.chat.id, f'Вопрос №{quest_num}\n{quest_text}\nОтвет №5: {quest_otvet_5}')
            #         complete = 1
            #         quest_num += 1
            #         print('5')
            #     id += 1
            # except Exception as ex:
            #     print(ex)
            #     ex_id += 1
            #     continue
            #
            # try:
            #     quest_6 = driver.find_element(By.ID, 'r6')
            #     if quest_6.get_attribute('value') != '0' and complete == 0:
            #         quest_otvet_6 = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[6]/td/div').text
            #         quest_6.click()
            #         bot.send_message(message.chat.id, f'Вопрос №{quest_num}\n{quest_text}\nОтвет №6: {quest_otvet_6}')
            #         complete = 1
            #         quest_num += 1
            #         print('6')
            #     id += 1
            # except Exception as ex:
            #     print(ex)
            #     ex_id += 1
            #     continue
            #
            # try:
            #     quest_7 = driver.find_element(By.ID, 'r7')
            #     if quest_7.get_attribute('value') != '0' and complete == 0:
            #         quest_otvet_7 = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[7]/td/div').text
            #         quest_7.click()
            #         bot.send_message(message.chat.id, f'Вопрос №{quest_num}\n{quest_text}\nОтвет №7: {quest_otvet_7}')
            #         complete = 1
            #         quest_num += 1
            #         print('7')
            #     id += 1
            # except Exception as ex:
            #     print(ex)
            #     ex_id += 1
            #     continue
            #
            # try:
            #     quest_8 = driver.find_element(By.ID, 'r8')
            #     if quest_8.get_attribute('value') != '0' and complete == 0:
            #         quest_otvet_8 = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/div').text
            #         quest_8.click()
            #         bot.send_message(message.chat.id, f'Вопрос №{quest_num}\n{quest_text}\nОтвет №8: {quest_otvet_8}')
            #         complete = 1
            #         quest_num += 1
            #         print('8')
            #     id += 1
            # except Exception as ex:
            #     print(ex)
            #     ex_id += 1
            #     continue
            #
            # try:
            #     quest_9 = driver.find_element(By.ID, 'r9')
            #     if quest_9.get_attribute('value') != '0' and complete == 0:
            #         quest_otvet_9 = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[9]/td/div').text
            #         quest_9.click()
            #         bot.send_message(message.chat.id, f'Вопрос №{quest_num}\n{quest_text}\nОтвет №9: {quest_otvet_9}')
            #         complete = 1
            #         quest_num += 1
            #         print('9')
            #     id += 1
            # except Exception as ex:
            #     print(ex)
            #     ex_id += 1
            #     continue
            #
            # try:
            #     quest_10 = driver.find_element(By.ID, 'r10')
            #     if quest_10.get_attribute('value') != '0' and complete == 0:
            #         quest_otvet_10 = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[10]/td/div').text
            #         quest_10.click()
            #         bot.send_message(message.chat.id, f'Вопрос №{quest_num}\n{quest_text}\nОтвет №10: {quest_otvet_10}')
            #         complete = 1
            #         quest_num += 1
            #         print('10')
            #     id += 1
            # except Exception as ex:
            #     print(ex)
            #     ex_id += 1
            #     continue

            if complete == 0 or ex_id == 4:
                driver.find_element(By.XPATH, f'//*[@id="r{random.randint(1, 4)}"]').click()
                random_quest_otvet = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div').text
                bot.send_message(message.chat.id, f'Вопрос №{quest_num}\n{quest_text}\nОтвет №2: {random_quest_otvet}')
                quest_num += 1

bot.polling(none_stop=True)