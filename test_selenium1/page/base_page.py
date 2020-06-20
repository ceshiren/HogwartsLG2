from selenium import webdriver
from selenium.webdriver.common.by import By



class BasePage():
    url = ""

    def __init__(self, driver:webdriver.Chrome()=None):
        if driver == None:
            self.driver = webdriver.Chrome()
        else:
            self.driver = driver
        if self.url == "":
            self.driver.get("")


    def find(self,by,value):
        return self.find(by=by, value=value)




