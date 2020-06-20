from test_selenium.test_wework.page.base_page import BasePage
from test_selenium.test_wework.page.contact_page import Contact
from selenium.webdriver.common.by import By


class AddMember(BasePage):
    _username = "username"


    def add_member(self):
        """
        添加成员
        :return:
        """
        self.find(By.ID, self._username).send_keys("维恩1")
        self.find(By.ID, "memberAdd_acctid").send_keys("1112221")
        self.find(By.ID, "memberAdd_phone").send_keys("13199991233")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return Contact(self.driver)

    def add_member_fail(self):
        """
        添加成员
        :return:
        """
        self.find(By.ID, self._username).send_keys("维恩2")
        self.find(By.ID, "memberAdd_acctid").send_keys("1112221")
        self.find(By.ID, "memberAdd_phone").send_keys("13199991239")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        self.find(By.CSS_SELECTOR, ".js_btn_cancel").click()
        return Contact(self.driver)
