import os
import csv
import dateutils
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as Ec
from selenium.common.exceptions import TimeoutException

cur_date = []
wk_chk = []
start_time = []
stop_time = []

try:
    csv_ph = "./CSV/7008_2271705_1_day_1_20200207.csv"
    csv_tmp = open(csv_ph, newline='')
    csv_data = csv.reader(csv_tmp)
    for digi_date in csv_data:
        cur_date.append(digi_date[8])
        wk_chk.append(digi_date[9])
        start_time.append(digi_date[15])
        stop_time.append(digi_date[17])
#            print(digi_date[8] + ":" + str(digi_date[9]))

except FileNotFoundError:
    print("指定された、CSVファイルが見つかりません")

driver = webdriver.Chrome("./driver/chromedriver.exe")
driver.get("https://vsn.digisheet.com/staffLogin")

driver.find_element_by_name("HC").send_keys("7008")
driver.find_element_by_name("UI").send_keys("2271705")
driver.find_element_by_name("Pw").send_keys("2271705Utagawa")
driver.find_element_by_name("loginButton").click()
WebDriverWait(driver, 60).until(Ec.presence_of_all_elements_located)

driver.switch_to.frame("menu") 

haken_digi = Select(driver.find_element_by_name("Cr"))
haken_digi.select_by_index(1)
WebDriverWait(driver, 60).until(Ec.presence_of_all_elements_located)

driver.switch_to.default_content()
driver.switch_to.frame("main") 
time.sleep(5)

driver.find_element_by_xpath("//a[contains(text(), '3')]").click()
WebDriverWait(driver, 60).until(Ec.presence_of_all_elements_located)

hst_time = Select(driver.find_element_by_name("HourStart"))
hst_time.select_by_index(10)
WebDriverWait(driver, 60).until(Ec.presence_of_all_elements_located)

mst_time = Select(driver.find_element_by_name("MinuteStart"))
mst_time.select_by_index(0)
WebDriverWait(driver, 60).until(Ec.presence_of_all_elements_located)

he_time = Select(driver.find_element_by_name("HourEnd"))
he_time.select_by_index(18)
WebDriverWait(driver, 60).until(Ec.presence_of_all_elements_located)

me_time = Select(driver.find_element_by_name("MinuteEnd"))
me_time.select_by_index(6)
WebDriverWait(driver, 60).until(Ec.presence_of_all_elements_located)


driver.find_element_by_name("RegistButton").click()