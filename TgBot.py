import re
import telebot
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
        try:
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
            while True:
                if len(driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/table/tbody/tr[2]/td/p[2]/a')) > 0:
                    driver.quit()
                    break
                # time.sleep(10000)
                quest_text = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[1]/td/div/div').text
                quest_num = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[1]/td/div/a/h2[2]').text

                id = 1
                complete = 0
                ex_id = 0

                if len(driver.find_elements(By.ID, 'r1')) > 0:
                    quest_1 = driver.find_element(By.ID, 'r1')
                    if quest_1.get_attribute('value') != '0' and complete == 0:
                        # quest_otvet_1 = driver.find_element('//*[@id="r1"]').text
                        quest_otvet_1 = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div').text
                        bot.send_message(message.chat.id, f'{quest_num}\n{quest_text}\nОтвет №1: {quest_otvet_1}')
                        quest_1.click()
                        complete = 1
                        print('1')
                else:
                    ex_id += 1


                if len(driver.find_elements(By.ID, 'r2')) > 0:
                    quest_2 = driver.find_element(By.ID, 'r2')
                    if quest_2.get_attribute('value') != '0' and complete == 0:
                        quest_otvet_2 = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div').text
                        bot.send_message(message.chat.id, f'{quest_num}\n{quest_text}\nОтвет №2: {quest_otvet_2}')
                        quest_2.click()
                        complete = 1
                        print('2')
                else:
                    ex_id += 1


                if len(driver.find_elements(By.ID, 'r3')) > 0:
                    quest_3 = driver.find_element(By.ID, 'r3')
                    if quest_3.get_attribute('value') != '0' and complete == 0:
                        quest_otvet_3 = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[3]/td/div').text
                        bot.send_message(message.chat.id, f'{quest_num}\n{quest_text}\nОтвет №3: {quest_otvet_3}')
                        quest_3.click()
                        complete = 1
                        print('3')
                else:
                    ex_id += 1


                if len(driver.find_elements(By.ID, 'r4')) > 0:
                    quest_4 = driver.find_element(By.ID, 'r4')
                    if quest_4.get_attribute('value') != '0' and complete == 0:
                        quest_otvet_4 = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[4]/td/div').text
                        bot.send_message(message.chat.id, f'{quest_num}\n{quest_text}\nОтвет №4: {quest_otvet_4}')
                        quest_4.click()
                        complete = 1
                        print('4')
                else:
                    ex_id += 1


                if len(driver.find_elements(By.ID, 'r5')) > 0:
                    quest_5 = driver.find_element(By.ID, 'r5')
                    if quest_5.get_attribute('value') != '0' and complete == 0:
                        quest_otvet_5 = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[5]/td/div').text
                        bot.send_message(message.chat.id, f'{quest_num}\n{quest_text}\nОтвет №5: {quest_otvet_5}')
                        quest_5.click()
                        complete = 1
                        print('5')
                else:
                    ex_id += 1


                if len(driver.find_elements(By.ID, 'r6')) > 0:
                    quest_6 = driver.find_element(By.ID, 'r6')
                    if quest_6.get_attribute('value') != '0' and complete == 0:
                        quest_otvet_6 = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[6]/td/div').text
                        bot.send_message(message.chat.id, f'{quest_num}\n{quest_text}\nОтвет №6: {quest_otvet_6}')
                        quest_6.click()
                        complete = 1
                        print('6')
                else:
                    ex_id += 1


                if len(driver.find_elements(By.ID, 'r7')) > 0:
                    quest_7 = driver.find_element(By.ID, 'r7')
                    if quest_7.get_attribute('value') != '0' and complete == 0:
                        quest_otvet_7 = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[7]/td/div').text
                        bot.send_message(message.chat.id, f'{quest_num}\n{quest_text}\nОтвет №7: {quest_otvet_7}')
                        quest_7.click()
                        complete = 1
                        print('7')
                else:
                    ex_id += 1

                if len(driver.find_elements(By.ID, 'r8')) > 0:
                    quest_8 = driver.find_element(By.ID, 'r8')
                    if quest_8.get_attribute('value') != '0' and complete == 0:
                        quest_otvet_8 = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[8]/td/div').text
                        bot.send_message(message.chat.id, f'{quest_num}\n{quest_text}\nОтвет №8: {quest_otvet_8}')
                        quest_8.click()
                        complete = 1
                        print('8')
                else:
                    ex_id += 1

                if len(driver.find_elements(By.ID, 'r9')) > 0:
                    quest_9 = driver.find_element(By.ID, 'r9')
                    if quest_9.get_attribute('value') != '0' and complete == 0:
                        quest_otvet_9 = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[9]/td/div').text
                        bot.send_message(message.chat.id, f'{quest_num}\n{quest_text}\nОтвет №9: {quest_otvet_9}')
                        quest_9.click()
                        complete = 1
                        print('9')
                else:
                    ex_id += 1

                if len(driver.find_elements(By.ID, 'r10')) > 0:
                    quest_10 = driver.find_element(By.ID, 'r10')
                    if quest_10.get_attribute('value') != '0' and complete == 0:
                        quest_otvet_10 = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[10]/td/div').text
                        bot.send_message(message.chat.id, f'{quest_num}\n{quest_text}\nОтвет №10: {quest_otvet_10}')
                        quest_10.click()
                        complete = 1
                        print('10')
                else:
                    ex_id += 1

                if complete == 0 or ex_id == 3:
                    random_quest_otvet = driver.find_element(By.XPATH, '//*[@id="gooo"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div').text
                    bot.send_message(message.chat.id, f'{quest_num}\n{quest_text}\nОтвет №2: {random_quest_otvet}')
                    driver.find_element(By.XPATH, '//*[@id="r2"]').click()
        except:
            bot.send_message(message.chat.id, 'Критическая ошибка')

bot.polling(none_stop=True)