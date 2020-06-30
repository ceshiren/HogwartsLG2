from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#BasePage的定义是，它是一个其他page的公共方法的封装，它是一个底层使用的框架
from selenium.webdriver.remote.webdriver import WebDriver



class BasePage():
    _base_url = ""
    def __init__(self , driver_basepage:WebDriver = None):
        if driver_basepage == None:
            # 实例化options
            option = Options()
            # Google\ Chrome - -remote - debugging - port = 9222
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver = driver_basepage
        if self._base_url != "":
            self.driver.get(self._base_url)
        self.driver.implicitly_wait(3)

    def find(self, by, value):
        return self.driver.find_element(by= by, value=value)

    def finds(self, by , value):
        return self.driver.find_elements(by= by, value=value)

    def quit(self):
        return self.driver.quit()