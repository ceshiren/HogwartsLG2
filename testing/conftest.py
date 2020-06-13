#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

import pytest

# 自定义的hook函数，pytest_collection_modifyitems 可以将收集上来的测试用例进行改写，
# 控制用例的执行顺序，自动添加标签，解决测试用例的编码问题
import yaml


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # items 就是所有的测试用例列表，item 代表每个测试用例对象
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)


def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")  # group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',
                      dest='env',
                      help='set your run env'
                      )


@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        print("获取测试数据")
        with open("datas/testdatas/test/test.yml") as f:
            datas = yaml.safe_load(f)
    elif myenv == 'dev':
        print("获取dev数据")
        with open("datas/testdatas/dev/dev.yml") as f:
            datas = yaml.safe_load(f)
    return datas
