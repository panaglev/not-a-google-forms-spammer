import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from russian_names import RussianNames
from mimesis import Generic
from faker import Faker

GROUPS = [201-1, 201-2, 211, 221-1, 221-2, 231-1, 231-2, 200,
210, 220, 230-1, 230-2, 230-3, 230-4, 209, 219-1, 110, 120-2,
140-1, 112, 129, 128, 142-3, 400-1, 421-1, 421-3, 432-1, 440-1,
409-1, 311-1, 341, 351-1, 611, 610-1, 712-1, 762-1, 762-2, 738-1,
748, 862-1, 861-1, 870-1, 889-2]
FORMAT = ['онлайн', 'офлайн']
PROGRAM_NAME = ['Intensive course of English (Elementary level)', 'Intensive course of English (Pre-Intermediate level)',
'Intensive course of English (Intermediate level- Upper-Intermediate level)']
DOMAINS=['@mail.ru','@yandex.ru','@list.ru','@gmail.com','@bk.ru']
TIMES = ['11:00', "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"]
CODES = ['983', '906', '913', '961', '901', '996', '999', '905', '900', '958', '995']

def generate_phone_number(number):
    phone_number = "7"
    phone_number += str(CODES[number%len(CODES)])
    phone_number += str(random.randint(1000000, 9999999))
    return phone_number

s=Service('/opt/homebrew/bin/chromedriver')
driver = webdriver.Chrome(service=s)


url = str(input("Enter google forms url: "))

driver.get(url)

def fill_form(fio, format, group_name, prog_name, phone, email, good_time):
    list_xpaths = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input',
                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input',
                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input',
                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input',
                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input',
                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input']

    time.sleep(1)
    inputs_1 = driver.find_element_by_xpath(list_xpaths[0]).send_keys(fio)
    inputs_2 = driver.find_element_by_xpath(list_xpaths[1]).send_keys(format)
    inputs_3 = driver.find_element_by_xpath(list_xpaths[2]).send_keys(group_name)
    inputs_4 = driver.find_element_by_xpath(list_xpaths[3]).send_keys(prog_name)
    inputs_5 = driver.find_element_by_xpath(list_xpaths[4]).send_keys(phone)
    inputs_6 = driver.find_element_by_xpath(list_xpaths[5]).send_keys(email)
    inputs_7 = driver.find_element_by_xpath(list_xpaths[6]).send_keys(good_time)
    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

def main():
    numbers = []
    for i in range(7):
        numbers.append(random.randint(0, 100))
    generic = Generic('ru')
    fake = Faker()
    res = fake.email()
    new_res = res.split("@")
    fill_form(RussianNames().get_person(), FORMAT[numbers[1]%len(FORMAT)], GROUPS[numbers[2]%len(GROUPS)], PROGRAM_NAME[numbers[3]%len(PROGRAM_NAME)], generate_phone_number(numbers[4]), new_res[0]+DOMAINS[numbers[5]%len(DOMAINS)], TIMES[numbers[6]%len(TIMES)])
    subm = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

if __name__ == "__main__":
    i = 0
    while True:
        i += 1
		if i % 5 == 0:
        	print(i)
        main()
