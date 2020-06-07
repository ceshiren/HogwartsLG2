#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
写一个 Bicycle (自行车)类，有run （骑行）方法，调用时显示骑行里程km(骑行里程为传入的数字)
再写一个电动自行车类EBicycle继承Bicycle，添加电池电量 battery_level 属性通过参数传入，
同时有两个方法：
    1、fill_charge(vol)  用来充电， vol为电量
    2、run(km) 方法用于骑行，每骑行10km消耗电量1度，当电量耗尽时调用Bicycle的run方法骑行，
    通过传入的骑行里程数，显示骑行结果（就是当电量耗尽，需要你真正骑的里程数）。
"""

# 创建 自行车类
import yaml


class Bycycle:
    def run(self, km):
        print(f"骑行的里程数为：{km} km ")


# 创建电动车类
class EBicycle(Bycycle):
    def __init__(self, battery_level):
        self.battery_level = battery_level

    def fill_charge(self, vol):
        print(f"充电：{vol}")

    def run(self, km):
        # 每骑行 10km 消耗电量1度， 假如 有10度电，最多电量能骑行 10*10=100 km
        max_mile = self.battery_level * 10
        leave_mile = km - max_mile

        if leave_mile > 0:
            print(f"已经使用电量骑行的里数：{max_mile} km ")
            super().run(leave_mile)

        else:
            print(f"骑行的里程数：{km} km ")


if __name__ == '__main__':
    with open("bycicle_data.yml") as f:
        datas = yaml.safe_load(f)

    # print(datas)
    my1 = datas['default']
    my_battery = my1['batter_level']
    my_km = my1['km']
    myebycicle = EBicycle(my_battery)
    myebycicle.run(my_km)

#
# myebycicle = EBicycle(10)
# myebycicle.run(100)
#
# myebycicle1 = EBicycle(20)
# myebycicle1.run(300)
