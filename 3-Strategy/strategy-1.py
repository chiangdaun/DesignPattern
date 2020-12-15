# -*- coding: utf-8 -*-
"""
Author:duan
Date: 2020/11/25 0:13
"""
"""
在实验楼问答模块中，一个问题可能有多种显示方式。
如果用户有管理权限，那么问题的详情页面可能会显示编辑按钮，如果是普通用户则只显示问题内容。这样一个对象我们该怎么实现呢？
"""


class Question(object):
    """
    问题对象，没有使用策略模式之前的作法
    """

    def __init__(self, admin=True):
        self._admin = admin

    def show(self):
        """
        根据是否是管理员显示不同的信息
        """
        if self._admin is True:
            return "show page with admin"
        else:
            return "show page with user"


if __name__ == '__main__':
    q = Question(admin=False)
    print(q.show())

"""
以上代码中，最重要的操作就是Question.show操作，它会根据Quesiton._admin标志的不同完成两种显示。
现在我们有一些新的需求，增加Question的显示方式，怎么办？
如果增加更多的显示方式，按照以上作法，我们必然要修改Quesiton.show方法，并增加更多的标志位。
这样一来Question在面对不断增加的显示需求时都需要修改其代码，显然这是一种不好的设计。
"""
"""
下面该轮到策略模式发挥作用的时候了，
策略模式将各种操作（算法）进行封装，并使它们之间可以互换。
互换的意思是说可以动态改变对象的操作方式（算法）。下面让我们使用策略模式来重现实现Question.show操作。
"""
