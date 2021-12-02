import csv
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

l1=[]

def test_launch_browser():
    global chromebrowser
    app_url = 'https://www.calculator.net/'
    chromebrowser = webdriver.Chrome(executable_path='chromedriver.exe')
    chromebrowser.get(app_url)
    chromebrowser.maximize_window()

def test_csv_reader():
    global csv_reader
    row = 1
    with open('Sample_Test_Cases.csv', 'r') as f:
        csv_reader = csv.reader(f)
        for item in csv_reader:
            l1.append(item)


def test_multiplication():
    x = int(l1[0][2])
    chromebrowser.find_element(By.XPATH, '/html/body').send_keys(l1[0][0])
    time.sleep(3)
    chromebrowser.find_element(By.XPATH, '//div/div[3]/span[4][@class="sciop"]').click()
    time.sleep(3)
    chromebrowser.find_element(By.XPATH, '/html/body').send_keys(l1[0][1])
    time.sleep(3)
    chromebrowser.find_element(By.XPATH, '//div/div[5]/span[4][@class="scieq"]').click()
    time.sleep(3)
    webelement = chromebrowser.find_element(By.XPATH,'//div[contains(@id,"sciOutPut")]').text
    r = int(webelement)
    assert x == r
    print(r)
    chromebrowser.find_element(By.XPATH, '//div/div[5]/span[3][@class="scieq"]').click()
    time.sleep(3)

def test_division():
    x = int(l1[1][2])
    chromebrowser.find_element(By.XPATH, '/html/body').send_keys(l1[1][0])
    time.sleep(3)
    chromebrowser.find_element(By.XPATH, '//div/div[4]/span[4][@class="sciop"]').click()
    time.sleep(3)
    chromebrowser.find_element(By.XPATH, '/html/body').send_keys(l1[1][1])
    time.sleep(3)
    chromebrowser.find_element(By.XPATH, '//div/div[5]/span[4][@class="scieq"]').click()
    time.sleep(3)
    webelement = chromebrowser.find_element(By.XPATH,'//div[contains(@id,"sciOutPut")]').text
    r = int(webelement)
    assert x == r
    print(r)
    chromebrowser.find_element(By.XPATH, '//div/div[5]/span[3][@class="scieq"]').click()
    time.sleep(5)


def test_addition():
    x = int(l1[2][2])
    chromebrowser.find_element(By.XPATH, '/html/body').send_keys(l1[2][0])
    time.sleep(3)
    chromebrowser.find_element(By.XPATH, '//div/div[1]/span[4][@class="sciop"]').click()
    time.sleep(3)
    chromebrowser.find_element(By.XPATH, '/html/body').send_keys(l1[2][1])
    time.sleep(3)
    chromebrowser.find_element(By.XPATH, '//div/div[5]/span[4][@class="scieq"]').click()
    time.sleep(3)
    webelement = chromebrowser.find_element(By.XPATH,'//div[contains(@id,"sciOutPut")]').text
    r = int(webelement)
    assert x == r
    print(r)
    chromebrowser.find_element(By.XPATH, '//div/div[5]/span[3][@class="scieq"]').click()
    time.sleep(5)


def test_subtraction():
    x = int(l1[3][2])
    chromebrowser.find_element(By.XPATH, '/html/body').send_keys(l1[3][0])
    time.sleep(3)
    chromebrowser.find_element(By.XPATH, '//div/div[2]/span[4][@class="sciop"]').click()
    time.sleep(3)
    chromebrowser.find_element(By.XPATH, '/html/body').send_keys(l1[3][1])
    time.sleep(3)
    chromebrowser.find_element(By.XPATH, '//div/div[5]/span[4][@class="scieq"]').click()
    time.sleep(3)
    webelement = chromebrowser.find_element(By.XPATH,'//div[contains(@id,"sciOutPut")]').text
    r = int(webelement)
    assert x == r
    print(r)
    chromebrowser.find_element(By.XPATH, '//div/div[5]/span[3][@class="scieq"]').click()
    time.sleep(5)

## Kindly run command : 'pytest --html = FinalReport.html' in terminal by activating the environment



