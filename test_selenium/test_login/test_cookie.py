import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCookie():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")

    def test_get_cookie(self):
        time.sleep(15)
        # 一定要在扫码，登录成功之后执行
        cookies = self.driver.get_cookies()
        with open("cookie.json", "w") as f:
            json.dump(cookies, f)

    def test_cookie_login(self):
        cookies = json.load(open("cookie.json"))
        for cookie in cookies:
            # 添加一个dict的cookie信息，把cookie键值对，一个一个的塞入浏览器中
            self.driver.add_cookie(cookie)
        # 如果代码没有问题，但是还是没有成功，多加等待时间
        # time.sleep(10)
        #刷新\

        while True:
            self.driver.refresh()
            res = WebDriverWait(self.driver, 10).\
                until(expected_conditions.element_to_be_clickable((By.ID, "menu_index")))
            if res is not None:
                break
        # expected_conditions.xx 都需要传入的是一个元祖
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable
                    ((By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)")))
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "js_upload_file_input")))
        # sendkeys需要使用绝对路径
        self.find(By.ID, "js_upload_file_input").\
            send_keys("/Users/lixu/project/hogwarts/HogwartsLG2/test_selenium/data/workbook.xlsx")

        assert_ele = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "upload_file_name"))).text

        # assert_ele = self.find(By.ID, "upload_file_name").text
        print(assert_ele)
        assert assert_ele == "workbook.xlsx"



    def teardown(self):
        self.driver.quit()