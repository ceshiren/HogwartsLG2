#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Father:
    def __init__(self):
        print("father init")


class Son(Father):

    def b(self):
        print("b")


son = Son()
