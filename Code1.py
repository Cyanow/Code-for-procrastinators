from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

browser = webdriver.Chrome(options = options)
browser.get("https://YouTube.com")

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


browser.maximize_window()
browser.implicitly_wait(10)

shorts = browser.find_element("xpath",'/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-entry-renderer[2]/a/tp-yt-paper-item/yt-formatted-string')
shorts.click()

title = browser.find_element("xpath",'//*[@id="overlay"]/ytd-reel-player-header-renderer/h2/yt-formatted-string')
print(title)
print(title.text)

youtubeTitle = open("youtubeTitle.txt","a") 

import time

for i in range(1,69):
    #title = browser.find_element("jspath",'//*[@id="overlay"]/ytd-reel-player-header-renderer/h2/yt-formatted-string')
    #print(title)
    #print(title.text)
    
    time.sleep(60)

    arrowDown = ActionChains(browser)
    arrowDown.send_keys(Keys.ARROW_DOWN)
    arrowDown.perform()
    
    