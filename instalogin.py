from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

class InstagramBot:

    def __init__(self,username="",password=""):
        self.username = username
        self.password = password
        self.setUserNameAndPass()

    def setUserNameAndPass(self):
        filepath = 'config.json'
        with open(filepath, "r") as config:
            configJson = json.load(config)
            self.username, self.password = configJson['login']['username'], configJson['login']['password']
    
    def setDriver(self):
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
        self.driver = webdriver.Firefox(firefox_profile=firefox_profile)

    def login(self):
        driver = self.driver
        # open instagram
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        # open login page
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        # enter username
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        # enter password
        pass_elem = driver.find_element_by_xpath("//input[@name='password']")
        pass_elem.clear()
        pass_elem.send_keys(self.password)
        # press enter to login
        pass_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def follow(self,profile):
        driver = self.driver
        # open profile of desired user
        url = "https://www.instagram.com/" + profile + "/"
        driver.get(url)
        time.sleep(2)
        # click on the follow button
        buttons = driver.find_element_by_xpath("//button[contains(.,'Follow')]")
        buttons.click()
        time.sleep(2)

    def likePhoto(self,profile):
        driver = self.driver
        # open profile of desired user
        url = "https://www.instagram.com/" + profile + "/"
        driver.get(url)
        time.sleep(2)
        # find all the photos and videos link
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs if '/p/' in href]
        #try and like all the pics and video
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            try:
                driver.find_element_by_xpath("//span[@aria-label='Like']").click()
                time.sleep(5)
            except Exception as e:
                time.sleep(2)

    def closeBrowser(self):
        self.driver.close()


# steps to follow:
# Update username and password in config.json
# create a InstagramBot object            
bot = InstagramBot()

# initialize the driver
bot.setDriver()

# login as the bot
bot.login()

# either follow any profile giving only the user id which is part of: 
# profile url: https://www.instagram.com/rahulshaw274/
# userid: rahulshaw274
profileToFollow = 'rahulshaw274'
bot.follow(profileToFollow)

# or like every photo of a pofile
profileToLike = 'rahulshaw274'
bot.likePhoto(profileToLike)


