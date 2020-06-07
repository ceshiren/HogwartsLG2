#!/usr/bin/env python
# -*- coding: utf-8 -*-
import girl


def show():
    print(id(girl.have_girl))
    if girl.have_girl == True:
        print("有女朋友，好开心 ~~")
    else:
        print("单身贵族 *_*")
