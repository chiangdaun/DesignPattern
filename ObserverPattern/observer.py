# -*- coding: utf-8 -*-
"""
Author:duan
Date: 2021/1/31 20:57
"""
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法
from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """观察者的基类"""

    @abstractmethod
    def update(self, observable, object):
        pass


class Observable:
    """被观察者的基类"""

    def __init__(self):
        self._observers = []

    def addObserver(self, observer):
        self._observers.append(observer)

    def removeObserver(self, observer):
        self._observers.remove(observer)

    def notifyObservers(self, object=0):
        for o in self._observers:
            o.update(self, object)
