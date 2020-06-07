#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
创建一个Person 类
    属性：姓名，性别，年龄，存款金额
    方法: 吃，睡，跑，赚钱
创建 FunnyMan类( 喜剧 演员)
    继承父类Person的所有属性和方法
    新增一个方法，fun()搞笑
创建 SingerMan 类（歌手演员）
    继承父类Person的所有属性和方法，
    覆写方法，赚钱，传参（monkey）
"""


def a():
    print("aaa")


class Person:
    name: str = "default"
    gender: str = "default"
    age: int = 20
    __money: float = 1000

    def __init__(self, name, gender, age, money):
        self.name = name
        self.gender = gender
        self.age = age
        self.__money = money

    @classmethod
    def clasmethod(cls):
        pass

    def get_money(self):
        print(f"获取私有属性 monkey的值 {self.__money}")
        return self.__money

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name}is sleeping")

    def run(self):
        print(f"{self.name}is running")

    def make_money(self):
        print(f"{self.name}could make money")


class FunnyMan(Person):
    def fun(self):
        print(f"{self.name} is very funny")


class SingerMan(Person):
    def make_money(self, moneynum: str = None):
        print(f"{self.name} could make monkey {moneynum} ")


class ChenXuYuan(Person):

    def write_code(self):
        print(f"{self.name} could write code")

    @classmethod
    def zhengshu(cls):
        print("我有证书")

    @staticmethod
    def jingtai():
        print("这是一个静态方法")


gezishan = ChenXuYuan('tom', '男', 30, 100000)
# ChenXuYuan.write_code()
ChenXuYuan.zhengshu()
# gezishan.zhengshu()
# ChenXuYuan.zhengshu()
ChenXuYuan.jingtai()

# singer = SingerMan('jerry', '男', 28, 1000)
# singer.make_money("10W")

# funnyman = FunnyMan('st', '男', 30, 20000)
# print(funnyman.name)
# funnyman.eat()
# funnyman.fun()
#
# #
# #
# p = Person("lili", '女',18, 10000)
# print(p.name)
# p.eat()
# # p.make_monkey()
# print(p.get_money())
#
# print(dir(p))
# p._Person__make_monkey()
# print(p._Person__money)
# # p1 = Person()
# # print(p1.name)
