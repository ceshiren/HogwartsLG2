#!/usr/bin/env python
# -*- coding: utf-8 -*-
a = 1


def func():
    global a
    a = 2
    print(f"a = {a}")


print(a)
func()
