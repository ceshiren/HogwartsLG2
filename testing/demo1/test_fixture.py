#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(params=[1, 2, 3, 'lili'])
def login(request):
    print("登录")
    yield request.param
    print("登出操作")


def test_case0(login):
    print("testcase0 ")


class TestLogin:

    def test_case1(self, login):
        print(f"testcase 1   {login}")

    def test_case2(self, login):
        print("testcase 2")

    def test_case3(self, login):
        print("testcase 3")
