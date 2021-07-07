import time
from selenium import webdriver
import pandas as pd

url = "https://weather.com/weather/tenday/l/San+Francisco+CA?canonicalCityId=dfdaba8cbe3a4d12a8796e1f7b1ccc7174b4b0a2d5ddb1c8566ae9f154fa638c"

chrome = webdriver.Chrome("chromedriver.exe")

chrome.get(url)
time.sleep(5)

Day_list = []
Date_list = []
Temp_Day_list = []
Temp_Night_list = []
short_description_Day_list = []
short_description_Night_list = []

for i in range(1,11):
    chrome.find_element_by_xpath("/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[" + str(i) + "]").click()

    Day_date = chrome.find_element_by_xpath(
        "/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[" + str(i) + "]/div/div[1]/h3/span").text.split()

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
    Temp_Day = int((int(chrome.find_element_by_xpath(
        "/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[" + str(i) + "]/div/div[1]/div/div[1]/span").text.replace(
        "°", ""))-32)*5/9)

    Temp_Night = int((int(chrome.find_element_by_xpath(
        "/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[" + str(i) + "]/div/div[2]/div/div[1]/span").text.replace(
        "°", ""))-32)*5/9)

    short_description_Day = chrome.find_element_by_xpath(
        "/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[" + str(i) + "]/div/div[1]/p").text
    short_description_Night = chrome.find_element_by_xpath(
        "/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[" + str(i) + "]/div/div[1]/p").text

    print("Day of the Week: " + Day)
    print("Date: " + Date)
    print("Maxiumum Degrees in C°: " + str(Temp_Day))
    print("Minimum Degrees in C°: " + str(Temp_Night))
    print("Description of the weather during the day: " + short_description_Day)
    print("Description of the weather during the day: "  + short_description_Night)

    print("\n\n\n")

    Day_list.append(Day)
    Date_list.append(Date)
    Temp_Day_list.append(Temp_Day)
    Temp_Night_list.append(Temp_Night)
    short_description_Day_list.append(short_description_Day)
    short_description_Night_list.append(short_description_Night)

    Scroll = chrome.execute_script("window.scrollBy(0,300)")
    time.sleep(3)

df = pd.DataFrame(data ={'Day_of_the_week': Day_list,
                         'Date': Date_list,
                         'Max temperature':Temp_Day_list,
                         'Min temperature':Temp_Night_list,
                         'Weather Day Description': short_description_Day_list,
                         'Weather Night Description': short_description_Night_list,
                         },
                        index=list(range(1,11)))
print(df)
