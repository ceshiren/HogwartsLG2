from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from test_selenium.test_wework.page.base_page import BasePage


class Contact(BasePage):


    def get_member(self):

        elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_tr .member_colRight_memberTable_td:nth-child(2)")
        name_list = [element.get_attribute("title") for element in elements]

        return name_list