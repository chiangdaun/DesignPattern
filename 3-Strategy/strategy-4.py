# -*- coding: utf-8 -*-
"""
Author:duan
Date: 2020/12/4 21:36
"""
import abc


class PaySuper(object):

    @abc.abstractmethod
    def pay_money(self, money):
        pass


class NormalPay(PaySuper):
    def pay_money(self, money):
        return money


class SilverVipPay(PaySuper):
    def __init__(self, reduce):
        self.reduce = reduce

    def pay_money(self, money):
        return money - self.reduce


class GoldVipPay(PaySuper):
    def __init__(self, discount=float(1)):
        self.discount = discount

    def pay_money(self, money):
        return money * self.discount


class PlatinumVipPay(PaySuper):
    def __init__(self, reduce, discount=float(1), ):
        self.discount = discount
        self.reduce = reduce

    def pay_money(self, money):
        return money * self.discount - self.reduce


class Context(object):
    def __init__(self, pay_super):
        self.pay_super = pay_super

    def get_money(self, money):
        return self.pay_super.pay_money(money)


if __name__ == '__main__':
    money = input("应付款：")
    strategy = {1: Context(NormalPay()), 2: Context(SilverVipPay(50)), 3: GoldVipPay(0.8), 4: PlatinumVipPay(0.7, 50)}
    mode = int(input("选择会员类型：\b1.普通会员 \b2."))
