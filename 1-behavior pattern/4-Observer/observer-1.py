# -*- coding: utf-8 -*-
"""
Author:duan
Date: 2020/12/6 21:09
"""
import abc


class Subject(object):
    """被观察对象的基类"""
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        """注册一个观察者"""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """注销一个观察者"""
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        """通知所有观察者，执行观察者的更新方法"""
        for observer in self._observers:
            observer.update(self)


class Course(Subject):
    """课程对象，被观察的对象"""
    def __init__(self):
        super(Course, self).__init__()
        self._message = None

    @property
    def message(self):
        """message 是一个属性"""
        return self._message

    @message.setter
    def message(self, msg):
        """message 属性设置器"""
        self._message = msg
        self.notify()


class Observer(object):
    """观察者抽象类"""
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def update(self, subject):
        pass


class UserObserver(Observer):
    """用户观察者"""
    def update(self, subject):
        print("User observer: %s" % subject.message)


class OrgObserver(Observer):
    """机构观察者"""
    def update(self, subject):
        print("Organization observer: %s" % subject.message)


if __name__ == '__main__':
    # 初始化一个用户观察者
    user = UserObserver()
    # 初始化一个机构观察者
    org = OrgObserver()

    # 初始化一个课程
    course = Course()
    # 注册观察者
    course.attach(user)
    course.attach(org)

    # 设置course.message，这时观察者会收到通知
    course.message = "two observers"

    # 注销一个观察者
    course.detach(user)
    course.message = "single observer"

"""
在上面的代码中，最重要的就是Subject类了，它实现了观察者模式中大部分功能。
作为一个被观察的对象，Subject实现了注册观察者，注销观察者和通知观察者的功能。
接着我们基于Subject创建了我们的课程Course类，并且当我们设置Course.message属性时，Course对象会通知到所有观察者。
可以看出，观察者模式使被观察的对象（主题）和观察者之间解耦了。
"""