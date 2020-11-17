#!/usr/bin/python
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import urlparse
import time
import os
import csv


class Channel:
    def __init__ (self, name, link, subs, vids):
        self.name = name
        self.link = link
        self.number_of_subs = subs
        self.number_of_vids = vids
    

def create_url(type_of_channel_searched, orderBy):
    url = ('https://www.youtube.com/results?search_query=' 
            + type_of_channel_searched 
            + '&sp=' 
            + orderBy)
    url = urlparse(url).geturl()
    return url


def reset_screen():
    os.system("reset")


def document_initialised(driver):
    return driver.execute_script("return initialised")


def scroll(driver, timeout):
    scroll_pause_time = timeout

    # Get scroll height
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    count = 1
    for i in range(1):
    #while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

        # Wait to load page
        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        print("Read Screen nº  --> " + str(count))
        count = count + 1
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height 


def agree_cookies_pop_up(driver):
    driver.switch_to.frame("iframe")
    driver.find_element_by_xpath('//*[@id="introAgreeButton"]/span/span').click()
    driver.switch_to.default_content()  


def number_of_vids_to_integer(number_of_vids_in_string):
    number_of_vids = 0
    if (len(number_of_vids_in_string) == 7):
        number_of_vids = int(number_of_vids_in_string[:-6])
    elif(len(number_of_vids_in_string) > 7):
            number_of_vids = int(number_of_vids_in_string[:-7].replace('.',''))
    return number_of_vids

def number_of_subs_to_integer(number_of_subs_in_string):
    number_of_subs = 0
    if (len(number_of_subs_in_string) == 12):
        # Convert "1 suscriptor" string to "1" integer
        number_of_subs = int(number_of_subs_in_string[:-11])
    elif(len(number_of_subs_in_string) >= 14):
        if number_of_subs_in_string.find("M") != -1:
            if number_of_subs_in_string.find(",") != -1:
                commaIndex = number_of_subs_in_string.find(",")
                spaceIndex = number_of_subs_in_string.find(" M")
                zerosToAdd = 6 - ((spaceIndex - 1) - commaIndex)
                zeros = zerosToAdd*'0'
                # Convert "1,1 M suscriptores" string to "1100000 suscriptores" string          
                number_of_subs_in_string = number_of_subs_in_string.replace(',','')
                number_of_subs_in_string = number_of_subs_in_string.replace(' M', zeros)
            else:
                # Convert "1 M suscriptores" string to "1100000 suscriptores" string          
                number_of_subs_in_string = number_of_subs_in_string.replace(' M','000000')  
        # Convert "x suscriptores" string to "x" integer             
        number_of_subs = int(number_of_subs_in_string[:-13].replace('.',''))
    return number_of_subs      

def get_number_of_subs(element):
    number_of_subs_in_string = element.find_element(By.ID, 'metadata').find_element(By.ID, 'subscribers').text # need to delete the tail 'suscriptores' -13 characters.    
    number_of_subs = number_of_subs_to_integer(number_of_subs_in_string)
    return number_of_subs

def get_number_of_vids(element):
    number_of_vids_in_string = element.find_element(By.ID, 'metadata').find_element(By.ID, 'video-count').text       
    number_of_vids = number_of_vids_to_integer(number_of_vids_in_string)
    return number_of_vids

def getLink(element):
    return element.get_attribute('href')

def returnChannel(element): #Returns a formatted Channel
    channel = Channel(element.find_element(By.TAG_NAME , 'ytd-channel-name').text,
                    getLink(element),
                    get_number_of_subs(element),
                    get_number_of_vids(element))

    return channel

def printChannels(channels):
    for c in channels:
        print (c.name)
        print ("Subs: " + str(c.number_of_subs) + " | " + "Vids: " + str(c.number_of_vids))    
        print ("------------")