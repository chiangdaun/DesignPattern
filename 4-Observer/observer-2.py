# -*- coding: utf-8 -*-
"""
Author:duan
Date: 2021/1/30 18:36
"""


class WaterHeater(object):
    """热水器：战胜寒冬的有利武器"""

    def __init__(self):
        super(WaterHeater, self).__init__()
        self.__observers = []
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("current temperature is:", self.__temperature)
        self.notifyObservers()

    def addObserver(self, observer):
        self.__observers.append(observer)

    def notifyObservers(self):
        for o in self.__observers:
            o.update(self)


class WashingMode(object):
    """该模式用于洗澡用"""

    def update(self, observable, object=None):
        if isinstance(observable,
                      WaterHeater) and 50 <= observable.getTemperature() < 70:
            print("水已烧好，温度正好！可以用来洗澡了。")


class DrinkingMode(object):
    """该模式用于饮用"""

    def update(self, observable, object=None):
        if isinstance(observable, WaterHeater) \
                and observable.getTemperature() >= 100:
            print("水已烧开！可以用来饮用了。")


if __name__ == '__main__':
    heater = WaterHeater()
    washingObser = WashingMode()
    drinkingObser = DrinkingMode()
    heater.addObserver(washingObser)
    heater.addObserver(drinkingObser)
    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(100)
