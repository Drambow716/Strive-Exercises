import calendar
import time
from datetime import date, datetime
import selenium
from selenium import webdriver
import pandas as pd

url = "https://weather.com/weather/tenday/l/San+Francisco+CA?canonicalCityId=dfdaba8cbe3a4d12a8796e1f7b1ccc7174b4b0a2d5ddb1c8566ae9f154fa638c"

chrome = webdriver.Chrome("chromedriver.exe")

chrome.get(url)
time.sleep(5)

for i in range(1,11):
    chrome.find_element_by_xpath("/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[" + str(i) + "]").click()

    Day_date = chrome.find_element_by_xpath(
        "/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[1]/div/div[1]/h3/span").text.split()
        
    Days = {"Mon": "Monday",
            "Tue": "Tuesday",
            "Wed": "Wednesday",
            "Thu": "Thursday",
            "Fri": "Friday",
            "Sat": "Saturday",
            "Sun": "Sunday",
            }
    Day = Days[Day_date[0]]

    Date = Day_date[1] + "/07/2021"
    Temp_Day = (int(chrome.find_element_by_xpath(
        "/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[1]/div/div[1]/div/div[1]/span").text.replace(
        "°", ""))-32)*5/9
    Temp_Night = (int(chrome.find_element_by_xpath(
        "/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[1]/div/div[2]/div/div[1]/span").text.replace(
        "°", ""))-32)*5/9

    short_description_Day = chrome.find_element_by_xpath(
        "/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[1]/div/div[1]/p").text
    short_description_Night = chrome.find_element_by_xpath(
        "/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[1]/div/div[1]/p").text

    print(Day)
    print(Date)
    print(Temp_Day)
    print(Temp_Night)
    print(short_description_Day)
    print(short_description_Night)
    Scroll = chrome.execute_script("window.scrollBy(0,500)")
    time.sleep(3)

