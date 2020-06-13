#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

import pytest
import yaml

from pythoncode.cal import Calculator


# 类外面的def 定义的叫做函数， 类里面def 定义的叫做方法
def test_a():
    print("testa")


# def setup_module():
#     print("setup module")
#
#
# def teardown_module():
#     print("teardown module")

def getdata():
    with open("datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    return datas


class TestCal:
    def setup(self):
        self.cal = Calculator()
        print("setup")

    def teardown(self):
        print("teardown")

    # def setup_class(self):
    #     self.cal = Calculator()
    #     print("setup class")
    #
    # def teardown_class(self):
    #     print("teardown class")

    # @pytest.mark.parametrize('a',pytest.param([1,2,3],id='int'))
    # @pytest.mark.parametrize('b',pytest.param(['a','b','c'],id='str'))
    # def test_zadd0(self,a,b):
    #     print(f"a = {a}  b = {b}")

    @pytest.mark.parametrize('a,b,result', getdata()
        , ids=[
            "整数", "浮点数", "bignum", 'minus', 'float+int'])
    def test_add(self, a, b, result):
        print("测试 相加1")
        # sleep(1)
        assert result == self.cal.add(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("datas/calc.yml")))
    def test_add1(self, a, b, result):
        print("测试 相加1")
        assert result == self.cal.add(a, b)

    def test_div(self):
        print("测试 相除1")
        assert 1 == self.cal.div(1, 1)

    def test_div1(self):
        print("测试 相除1")
        assert 1 == self.cal.div(1, 0)
