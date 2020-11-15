#!/usr/bin/python

from myFunctions import *

cls()
channels = []
channelsDriver = []
minSubs = 19
minVids = 5
SCROLL_PAUSE_TIME = 3
fields = ['Channel Name', 'Subscribers', 'Videos', 'Channel Link']
filename = "youtubeChannels.csv"
orderBy = {'relevance':'CAASAhAC', 'uploadDate':'CAISAhAC', 'numberOfDisplays':'CAMSAhAC', 'score':'CAESAhAC'}
channelTypeSearched = 'tecnologia'

driver = webdriver.Chrome()
driver.implicitly_wait(10)
url = createUrl(channelTypeSearched, orderBy['uploadDate'])
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

file = open(filename, 'w')
file.write("Channel Name;Subscribers;Videos;Channel Link;\n")
for c in channels:
    file.write(c.name +";"+ str(c.nSubs) +";"+ str(c.nVids) +";"+ c.link +";"+ "\n")

file.close()

print("Channels found: " + str(len(channels)))
