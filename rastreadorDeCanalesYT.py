#!/usr/bin/python

from myFunctions import *

cls()
channels = []
channelsDriver = []
minSubs = 19
minVids = 5
SCROLL_PAUSE_TIME = 3

url = 'https://www.youtube.com/results?search_query=tecnologia&sp=CAISAhAC' #fecha
#url = 'https://www.youtube.com/results?search_query=tecnologia&sp=CAASAhAC' #relevancia
#cambiar 'tecnologia' por búsqueda
#cambiar 'CAISAhAC' por tipo de búsqueda
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)

agreeCookiesPopUp(driver)

scroll(driver, 5)

channelsDriver = driver.find_elements(By.ID, 'main-link') 

for channelD in channelsDriver:
    nSubs, nVids = getNsubsAndNvids(channelD)

    if nSubs >= minSubs and nVids >= minVids:
        c = returnChannel(channelD)
        channels.append(c)




driver.quit()
printChannels(channels)
nCanales = len(channels)
print(nCanales)
