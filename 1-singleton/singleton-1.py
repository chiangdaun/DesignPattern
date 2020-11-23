# -*- coding: utf-8 -*-
"""
Author:duan
Date: 2020/11/19 23:04
"""


class Singleton(object):
    """
    单例模式
    """

    class _A(object):
        """
       真正干活的类, 对外隐藏
        """

        def __init__(self):
            pass

        def display(self):
            """ 返回当前实例的 ID，是全局唯一的"""
            return id(self)

    # 类变量，用于存储 _A 的实例
    _instance = None

    def __init__(self):
        """ 先判断类变量中是否已经保存了 _A 的实例，如果没有则创建一个后返回"""
        if Singleton._instance is None:
            Singleton._instance = Singleton._A()

    def __getattr__(self, attr):
        """ 所有的属性都应该直接从 Singleton._instance 获取"""
        return getattr(self._instance, attr)


"""
__getattr__(),这是python里的一个内建函数，当调用的属性或者方法不存在时，该方法会被调用.
在访问对象的item属性的时候，如果对象并没有这个相应的属性或者方法，那么将会调用__getattr__这个方法来处理;
这里要注意的时，假如一个对象叫obj,它一个属性：obj.name ="aaaa",那么在访问obj.name的时候因为当前对象有这个属性，
那么将不会调用__getattr__()方法，而是直接返回了拥有的name属性了。
"""
"""
对于本例,s1、s2都是Singleton的实例，没有display()方法，所以会执行__getattr__()方法,
进入__getattr__()方法，通过反射调用嵌套类_A的方法display(),返回该实例的id.
"""

if __name__ == '__main__':
    # 创建两个实例
    s1 = Singleton()
    s2 = Singleton()
    print(id(s1), s1.display())
    print(id(s2), s2.display())
