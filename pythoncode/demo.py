#!/usr/bin/env python
# -*- coding: utf-8 -*-

name = 'tome'
a = 1


def fun():
    global name
    name = 'jerry'
    print(f"func {name}")


print(name)
fun()
