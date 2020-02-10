import os
import csv
import pandas as pd
from selenium import webdriver

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

for add_date, chk  in zip(cur_date, wk_chk):
    if chk == 1:
        
        

    print(add_date, chk)

csv_tmp.close

# try:
#     csv_ph = "./CSV/7008_2271705_1_day_1_20200207.csv"
#     with open(csv_ph, newline='') as csvfile:
#         csv_data = csv.reader(csvfile)
#         for digi_date in csv_data:
#             print(digi_date[3])

# except FileNotFoundError:
#     print("指定された、CSVファイルが見つかりません")



#class main:

#     def csv_import:
#         try:


# driver = webdriver.Chrome("./driver/chromedriver.exe")
# driver.get("https://vsn.digisheet.com/staffLogin")
# driver.close()
# driver.quit()