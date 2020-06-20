from test_selenium.test_demo.page.index import IndexPage


class TestLogin():

    def test_login(self):
        index = IndexPage()
        # 1. 进入首页， 2.跳转登录页面 3.登录
        # 链式调用
        index.goto_login().login()