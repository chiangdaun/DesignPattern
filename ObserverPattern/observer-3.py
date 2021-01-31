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
from ObserverPattern.observer import Observer
from ObserverPattern.observer import Observable


class Account(Observable):
    """用户账户"""

    def __init__(self):
        super(Account, self).__init__()
        self.__latestIp = {}
        self.__latestRegion = {}

    def login(self, name, ip, time):
        region = self.__getRegion(ip)
        if self.__isLongDistance(name, region):
            self.notifyObservers({"name": name, "ip": ip, "region": region, "time": time})
        self.__latestRegion[name] = region
        self.__latestIp[name] = ip

    def __getRegion(self, ip):
        # 由IP地址获取地区信息。这里只是模拟，真实项目中应该调用IP地址解析服务
        ipRegions = {
            "101.47.18.9": "浙江省杭州市",
            "67.218.147.69":"美国洛杉矶"
        }
        region = ipRegions.get(ip)
        return "" if region is None else region


    def __isLongDistance(self, name, region):
        # 计算本次登录与最近几次登录的地区差距。
        # 这里只是简单地用字符串匹配来模拟，真实的项目中应该调用地理信息相关的服务
        latestRegion = self.__latestRegion.get(name)
        return latestRegion is not None and latestRegion != region


class SmsSender(Observer):
    """短信发送器"""

    def update(self, observable, object):
        print("[短信发送] " + object["name"] + "您好！检测到您的账户可能登录异常。最近一次登录信息：\n"
              + "登录地区：" + object["region"] + "  登录ip：" + object["ip"] + "  登录时间："
              + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))


class MailSender(Observer):
    """邮件发送器"""

    def update(self, observable, object):
        print("[邮件发送] " + object["name"] + "您好！检测到您的账户可能登录异常。最近一次登录信息：\n"
              + "登录地区：" + object["region"] + "  登录ip：" + object["ip"] + "  登录时间："
              + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))


if __name__ == '__main__':
    accout = Account()
    accout.addObserver(SmsSender())
    accout.addObserver(MailSender())
    accout.login("Tony", "101.47.18.9", time.time())
    accout.login("Tony", "67.218.147.69", time.time())
