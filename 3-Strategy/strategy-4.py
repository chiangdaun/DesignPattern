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
    u"""普通会员收费模式"""

    def pay_money(self, money):
        return money


class SilverVipPay(PaySuper):
    u"""白银会员收费模式"""

    def __init__(self, reduce):
        self.reduce = reduce

    def pay_money(self, money):
        if money - self.reduce > 0:
            return money - self.reduce
        return money


class GoldVipPay(PaySuper):
    u"""黄金会员收费模式"""

    def __init__(self, discount=float(1)):
        self.discount = discount

    def pay_money(self, money):
        return money * self.discount


class PlatinumVipPay(PaySuper):
    u"""白金会员收费模式"""

    def __init__(self, reduce, discount=float(1), ):
        self.discount = discount
        self.reduce = reduce

    def pay_money(self, money):
        if money * self.discount - self.reduce > 0:
            return money * self.discount - self.reduce
        return money


class Context(object):
    def __init__(self, pay_super):
        self.pay_super = pay_super

    def get_money(self, money):
        return self.pay_super.pay_money(money)


def get_pay_mode(money, mode):
    strategy = {1: Context(NormalPay()), 2: Context(SilverVipPay(50)), 3: GoldVipPay(0.8), 4: PlatinumVipPay(0.7, 50)}
    if money > 1000 and mode in strategy:
        pay_mode = strategy[mode]
    else:
        pay_mode = strategy[1]
    return pay_mode


if __name__ == '__main__':
    money = input("应付款：")
    mode = int(input("选择会员类型：\b1.普通会员 \b2.白银会员 \b3.黄金会员 \b4.白金会员"))
    pay_mode = get_pay_mode(money, mode)
    print("需要支付：", pay_mode.pay_money(money))
