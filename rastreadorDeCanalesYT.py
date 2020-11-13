#!/usr/bin/python

from myFunctions import *

cls()
channels = []
channelsDriver = []
minSubs = 15
minVids = 5

url = 'https://www.youtube.com/results?search_query=tecnologia&sp=CAISAhAC' #fecha
#url = 'https://www.youtube.com/results?search_query=tecnologia&sp=CAASAhAC' #relevancia
#cambiar 'tecnologia' por búsqueda
#cambiar 'CAISAhAC' por tipo de búsqueda
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)

agreeCookiesPopUp(driver)

while len(channels) < 10:
    channelsDriver += driver.find_elements(By.ID, 'main-link') 

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    
    for channelD in channelsDriver:
        nSubs, nVids = getNsubsAndNvids(channelD)

        if nSubs >= minSubs and nVids >= minVids:
            c = returnChannel(channelD)
            channels.append(c)


driver.quit()
printChannels(channels)
