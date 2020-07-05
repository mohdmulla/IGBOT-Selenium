from selenium import webdriver
from secrets import pw
import time

username='mullamohd'
class instabot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username

        self.driver.get("https://www.instagram.com")
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type=\"submit\"]')\
            .click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
            .click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
            .click()
        time.sleep(5)

    def get_unfollowers(self):
        #self.driver.get(F"https://www.instagram.com/{username}")
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/ul/li[3]/a")\
            .click()
        sugs = self.driver.find_element_by_xpath('//h4[contains(text(),Suggestions)]');
        self.driver.execute_script('arguments[0].scrollIntoView()',sugs)
        time.sleep(1)
        #scroll_box = self.driver.find_element_by_xpath("")
        last_ht , ht = 0, 1
        while last_ht   != ht:
            last_ht=ht
            sleep(1)
            ht = self.driver.execute("""
            arguments[0].scrollTo(0,arguments[0].scrollHieghts);
            return arguments[0].scrollHeight;
            """ , scroll_box)

mybot = instabot(username,pw)
mybot.get_unfollowers()
