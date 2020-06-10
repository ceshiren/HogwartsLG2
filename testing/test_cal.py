#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from pythoncode.cal import Calculator


# 类外面的def 定义的叫做函数， 类里面def 定义的叫做方法
def test_a():
    print("testa")


def setup_module():
    print("setup module")


def teardown_module():
    print("teardown module")


# def setup_function():
#     print("setup function")
#
# def teardown_function():
#     print("teardown function")

class TestCal:
    # def setup(self):
    #     self.cal = Calculator()
    #     print("setup")
    #
    # def teardown(self):
    #     print("teardown")

    def setup_class(self):
        self.cal = Calculator()
        print("setup class")

    def teardown_class(self):
        print("teardown class")

    @pytest.mark.add
    def test_add(self):
        print("测试 相加1")
        assert 3 == self.cal.add(1, 2)

    @pytest.mark.add
    def test_add1(self):
        print("测试 相加2")
        assert 300 == self.cal.add(100, 200)

    def test_div(self):
        print("测试 相除1")
        assert 1 == self.cal.div(1, 1)


class TestCal1:
    # def setup(self):
    #     self.cal = Calculator()
    #     print("setup")
    #
    # def teardown(self):
    #     print("teardown")

    def setup_class(self):
        self.cal = Calculator()
        print("setup class")

    def teardown_class(self):
        print("teardown class")

    @pytest.mark.add
    def test_add(self):
        print("测试 相加1")
        assert 3 == self.cal.add(1, 2)

    def test_add1(self):
        print("测试 相加2")
        assert 300 == self.cal.add(100, 200)

    def test_div(self):
        print("测试 相除1")
        assert 1 == self.cal.div(1, 1)
