import calendar
import time
from datetime import date, datetime
import selenium
from selenium import webdriver
import pandas as pd

months_dict = {"Jan":"1","Feb":"2","Mar":"3","Apr":"4","May":"7","Jun":"6","Jul":7,"Aug":"8","Sep":"7","Oct":"10","Nov":"11","Dec":"12"}

chrome = webdriver.Chrome("chromedriver.exe")

chrome.get("https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.YOWOT-gzaMo")
time.sleep(10)

Date = chrome.find_element_by_xpath("/html/body/main/div/div[4]/div[2]/div[2]/table/tbody/tr[6]/td[2]").text.strip().split()

Day = Date[0]
Year = date.today().year
Month = months_dict[Date[1]]

Day_of_the_week = chrome.find_element_by_xpath("/html/body/main/div/div[6]/div[1]/div[1]/div[2]/div[13]/div[1]/b").text.strip()

Full_date = str(Day) + "\\" + str(months_dict[Date[1]]) + "\\"+ str(Year)

conditions = chrome.find_element_by_xpath("/html/body/main/div/div[6]/div[1]/div[1]/div[2]/div[1]/div[2]").text.strip()

Temp_Low = int(((int(chrome.find_element_by_xpath("/html/body/main/div/div[5]/div[2]/div/ul/li[1]/div/p[4]").text.replace("°F","").replace("High: ","").strip())-32) *5/9))

Temp_High = int(((int(chrome.find_element_by_xpath("/html/body/main/div/div[5]/div[2]/div/ul/li[2]/div/p[4]").text.replace("°F","").replace("Low: ","").strip())-32) *5/9))

df = pd.DataFrame(data ={'Day_of_the_week': Day_of_the_week, 'Date': Full_date,'Conditions_sum':conditions, 'Temp_low': Temp_Low, 'Temp_High': Temp_High},index=[0])

print(df)





