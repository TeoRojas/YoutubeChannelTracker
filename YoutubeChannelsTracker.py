#!/usr/bin/python

from myFunctions import *

reset_screen()
SCROLL_PAUSE_TIME = 1
MIN_SUBS = 19
MIN_VIDS = 5    

def main():
    channels = []
    driver_format_channels = []
    orderBy = {
        'relevance':'CAASAhAC', 
        'uploadDate':'CAISAhAC', 
        'numberOfDisplays':'CAMSAhAC', 
        'score':'CAESAhAC'
        }
    type_of_channel_searched = 'geek'   
    filename = (
        type_of_channel_searched 
        + '_YT_channels.csv'
        )

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    url = create_url(type_of_channel_searched, orderBy['relevance'])
    driver.get(url)

    agree_cookies_pop_up(driver)

    scroll(driver, 1)

    driver_format_channels = driver.find_elements(By.ID, 'main-link') 

    for driver_channel in driver_format_channels:
        number_of_subs = get_number_of_subs(driver_channel) 
        number_of_vids = get_number_of_vids(driver_channel)

        if number_of_subs >= MIN_SUBS and number_of_vids >= MIN_VIDS:
            channels.append(returnChannel(driver_channel))

    driver.quit()


    with open(filename, 'w') as file:
        fieldnames = [
            'Channel Name',
            'Subscribers',
            'Videos',
            'Channel Link'
            ]
        writer = csv.writer(file, delimiter=';')
        writer.writerow(fieldnames)
        for c in channels:
            writer.writerow([c.name, c.number_of_subs, c.number_of_vids, c.link]) 

    print("Channels found: " + str(len(channels)))


if __name__ == '__main__':
    main()
