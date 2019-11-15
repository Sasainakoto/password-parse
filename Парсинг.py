import requests
import urllib.request
from bs4 import BeautifulSoup
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import csv
def init():
    driver = webdriver.Firefox(executable_path=r'D:\Питон(Змеюка)\geckodriver.exe')
    driver.wait = WebDriverWait(driver, 5)
    return driver
   
def get_page_data(driver):
    driver.get("https://lowe.github.io/tryzxcvbn")
    f_elem = driver.find_element_by_id('search-bar')
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    number = 50
    length = random.randint(5,15)
    f = csv.writer(open('passwords.csv', 'w'))
    f.writerow(['password', '100 / hour', '10 / seconds','10k / second','10B / second'])
    for n in range(number):
        password =''
        for i in range(length):
           password += random.choice(chars)
        f_elem.send_keys(password)
        f_elem.send_keys(Keys.RETURN)
        try:
            myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'result')))
            print ("Page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")
        main_page = driver.page_source
        #print(main_page)
        soup=BeautifulSoup(main_page)
        td=soup.find_all('td')
        i=0
        j=0
        m=20
        passw=''
        hund=''
        ten=''
        tenk=''
        tenb=''
        #here must be the generator 

        for tag in soup.find_all('td'):
            if (i<=20):
                    if   i==1:
                        print(tag.text)
                        passw = tag.text
                    elif i==10:
                        print(tag.text)
                        hund = tag.text
                    elif i==13:
                        print(tag.text)
                        ten = tag.text
                    elif i==16:
                        print(tag.text)
                        tenk = tag.text
                    elif i==19:
                        print(tag.text)
                        tenb = tag.text
                   
            i=i+1
        
        else:
            print("fifnished")
        f.writerow([passw, hund, ten, tenk, tenb])
        password =''
        driver.find_element_by_id('search-bar').clear()


if __name__ == '__main__':
        driver = init()
        get_page_data(driver)
        driver.quit()