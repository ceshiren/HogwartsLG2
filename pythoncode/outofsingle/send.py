#!/usr/bin/env python
# -*- coding: utf-8 -*-
import girl
# import girl   它是导入girl.py 模块， 导入的模块里的变量的内存地址。
from girl import have_girl


# from ... import ...    导入girl.py 里面的 have_girl 这个变量，复制了一份，放在本地

def send():
    print("发女朋友啦..")
    # global have_girl
    # girl.have_girl = True
    have_girl = True
    # print(f"have_girl  ={have_girl}")
