# -*- coding: utf-8 -*-
"""
Author:duan
Date: 2021/1/31 10:14
"""
"""
在互联网广泛普及和快速发展的时代，信息安全被越来越多的人重视，其中账户安全是信息安全最重要的一个部分。
很多网站都会有一个账号异常登录检测和诊断机制。当账户异常登录时，会以短信或邮件的方式将登录信息（登录的时间、地区、IP地址等）
发送给已经绑定的手机或邮箱。登录异常其实就是登录状态的改变。服务器会记录你最近几次登录的时间、地区、IP地址，从而得知你常用的登录地区；
如果哪次检测到你登录的地区与常用登录地区相差非常大（说明是登录地区的改变），则认为是一次异常登录。
而短信和邮箱的发送机制我们可以认为是登录的监听者，只要登录异常一出现就自动发送信息。
逻辑分析清楚之后就可以设计我们的代码了，首先设计类图，如图1-2所示。

源码示例：
"""
import time


class Account(object):
    def __int__(self):
        super(Account, self).__init__()
        self._lastIP = {}
        self._lastRegion = {}
        self.observer = []

    def login(self):
        pass

    def _getRegion(self):
        pass

    def _isLongDistance(self):
        pass

    def addObserver(self):
        pass

    def removeObserver(self):
        pass

    def notify(self):
        pass


class SmsSender(object):
    def update(self):
        pass


class EmailSender(object):
    def update(self):
        pass


if __name__ == '__main__':
    pass
