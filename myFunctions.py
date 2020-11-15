#!/usr/bin/python
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import csv


def document_initialised(driver):
    return driver.execute_script("return initialised")

def cls():
    os.system("reset")

def createUrl(channelTypeSearched, orderBy):
    return 'https://www.youtube.com/results?search_query=' + channelTypeSearched +'&sp=CAISAhAC' + orderBy 


def scroll(driver, timeout):
    scroll_pause_time = timeout

    # Get scroll height
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    count = 1
    while True:
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


def agreeCookiesPopUp(driver):
    driver.switch_to.frame("iframe")
    driver.find_element_by_xpath('//*[@id="introAgreeButton"]/span/span').click()
    driver.switch_to.default_content()  


def nVidsInteger(nVidsAux):
    nVids = 0
    if (len(nVidsAux) == 7):
        nVids = int(nVidsAux[:-6])
    elif(len(nVidsAux) > 7):
            nVids = int(nVidsAux[:-7].replace('.',''))
    return nVids

def nSubsInteger(nSubsAux):
    nSubs = 0
    if (len(nSubsAux) == 12):
        # Convert "1 suscriptor" string to "1" integer
        nSubs = int(nSubsAux[:-11])
    elif(len(nSubsAux) >= 14):
        if nSubsAux.find("M") != -1:
            if nSubsAux.find(",") != -1:
                commaIndex = nSubsAux.find(",")
                spaceIndex = nSubsAux.find(" M")
                zerosToAdd = 6 - ((spaceIndex - 1) - commaIndex)
                zeros = zerosToAdd*'0'
                # Convert "1,1 M suscriptores" string to "1100000 suscriptores" string          
                nSubsAux = nSubsAux.replace(',','')
                nSubsAux = nSubsAux.replace(' M', zeros)
            else:
                # Convert "1 M suscriptores" string to "1100000 suscriptores" string          
                nSubsAux = nSubsAux.replace(' M','000000')  
        # Convert "x suscriptores" string to "x" integer             
        nSubs = int(nSubsAux[:-13].replace('.',''))
    return nSubs      

class Channel:
    def __init__ (self, name, link, subs, vids):
        self.name = name
        self.link = link
        self.nSubs = subs
        self.nVids = vids

def getNsubsAndNvids(element):
    nSubsAux = element.find_element(By.ID, 'metadata').find_element(By.ID, 'subscribers').text # need to delete the tail 'suscriptores' -13 characters.
    nVidsAux = element.find_element(By.ID, 'metadata').find_element(By.ID, 'video-count').text    
    
    nSubs = nSubsInteger(nSubsAux)
    nVids = nVidsInteger(nVidsAux)

    return nSubs, nVids

def getNsubs(element):
    nSubsAux = element.find_element(By.ID, 'metadata').find_element(By.ID, 'subscribers').text # need to delete the tail 'suscriptores' -13 characters.    
    nSubs = nSubsInteger(nSubsAux)
    return nSubs

def getNvids(element):
    nVidsAux = element.find_element(By.ID, 'metadata').find_element(By.ID, 'video-count').text       
    nVids = nVidsInteger(nVidsAux)
    return nVids

def getLink(element):
    return element.get_attribute('href')

def returnChannel(element): #Returns a formatted Channel
    channel = Channel(element.find_element(By.TAG_NAME , 'ytd-channel-name').text,
    getLink(element),
    getNsubs(element),
    getNvids(element))

    return channel

def printChannels(channels):
    for c in channels:
        print (c.name)
        print ("Subs: " + str(c.nSubs) + " | " + "Vids: " + str(c.nVids))    
        print ("------------")