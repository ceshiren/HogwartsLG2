from selenium.webdriver.common.by import By

from test_selenium.test_wework.page.add_member_page import AddMember
from test_selenium.test_wework.page.base_page import BasePage
from test_selenium.test_wework.page.contact_page import Contact


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_add_member(self):
        # 跳转，函数名可以命名为goto_xxx
        #click
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMember(self.driver)

    def goto_contact(self):
        return Contact(self.driver)

    def goto_import_contact(self):
        pass


