# -*- coding: utf-8 -*-
"""
Author:duan
Date: 2020/11/23 23:33
"""
import random
import abc


class BasicCourse(object):
    """基础课程"""

    def get_labs(self):
        return "basic_course: labs"

    def __str__(self):
        return "BasicCourse"


class ProjectCourse(object):
    """项目课"""

    def get_labs(self):
        return "project_course: labs"

    def __str__(self):
        return "ProjectCourse"


class Factory(metaclass=abc.ABCMeta):
    """抽象工厂类"""

    @abc.abstractmethod
    def create_course(self):
        pass


class BasicCourseFactory(Factory):
    """基础课程工厂类"""

    def create_course(self):
        return BasicCourse()


class ProjectCourseFactory(Factory):
    """项目课程工厂类"""

    def create_course(self):
        return ProjectCourse()


def get_factory():
    """随机获取一个工厂类"""
    return random.choice([BasicCourseFactory, ProjectCourseFactory])()


"""
Factory是一个抽象工厂类。
抽象类的一个特点是它不能直接被实例化，抽象类的目的就是让别的类继承它并实现特定的抽象方法；
即含abstractmethod方法的类不能实例化，继承了含abstractmethod方法的子类必须复写所有abstractmethod装饰的方法，未被装饰的可以不重写
"""
"""
有两种课程：BasicCourse 和 ProjectCourse，分别对应基础课和项目课。
接着，我们创建了一个抽象的工厂 Factory，该工厂有一抽象方法Factory.create_course用于创建课程，
最后我们基于抽象工厂实现了生产基础课程的工厂BasicCourseFactory和生产项目课的工厂ProjectCourseFactory。
这样当我们新增加一种课程时，就不需要修改已经存在的基础课工厂和项目课工厂了。
当我们新增加一种产品时（课程）是，不需要修改原有的代码了，只需要增加产品类和相应的工厂类就可以了。
"""
"""
但是，当我们有很多种产品时使用工厂方法模式会产生非常多的工厂类。如何有效处理这类问题？
"""
if __name__ == '__main__':
    factory = get_factory()
    course = factory.create_course()
    print(course.get_labs())
