from test_selenium.test_demo.page.login_page import LoginPage
from test_selenium.test_demo.page.register_page import RegisterPage


class IndexPage:

    def goto_login(self):
        """
        跳转到登录页面
        :return: LoginPage的一个实例化
        """
        return LoginPage()

    def goto_register(self):
        """
        跳转到登录页面
        :return: RegisterPage的一个实例化
        """
        return RegisterPage()