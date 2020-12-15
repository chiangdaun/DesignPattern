# -*- coding: utf-8 -*-
"""
Author:duan
Date: 2020/12/9 21:47
"""
from abc import abstractmethod


class Person:
    u"""人类"""

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def showMyself(self):
        return "{name} 年龄：{age}; 身高：{height}; 体重：{weight}".format(
            name=self.name, age=self.age, height=self.height, weight=self.weight)


class ICompare:
    u"""比较算法"""

    @abstractmethod
    def comparable(self, person1, person2):
        u""""""
        pass


class CompareByAge(ICompare):
    u"""通过年龄排序"""

    def comparable(self, person1, person2):
        return person1.age - person2.age


class CompareByHeight(ICompare):
    u"""通过身高排序"""

    def comparable(self, person1, person2):
        return person1.height - person2.height

class CompareByHeightAndWeight(ICompare):
    u"""
    通过身高和体重综合情况排序
    权重分别0.6和0.4
    """
    def comparable(self, person1, person2):
        value1 = person1.height * 0.6 + person1.weight * 0.4
        value2 = person2.height * 0.6 + person2.weight * 0.4
        return value1 - value2


class SortPerson:
    u"""Person的排序类"""

    def __init__(self, compare):
        self._compare = compare

    def sort(self, person_list):
        u"""排序算法，使用最简单的冒泡排序"""
        person_list_len = len(person_list)
        for i in range(0, person_list_len - 1):
            for j in range(0, person_list_len - i - 1):
                if self._compare.comparable(person_list[j], person_list[j + 1]) > 0:
                    person_list[j + 1] ,person_list[j] = person_list[j], person_list[j + 1]
                j += 1
            i += 1


def testSortPerson():
    person_list = [
        Person("Tony", 2, 54.5, 0.82),
        Person("Jack", 21, 58.5, 1.72),
        Person("Nick", 32, 64.5, 1.62),
        Person("Eric", 23, 64.5, 1.72),
        Person("Helen", 18, 59.5, 1.79)
    ]
    age_sort = SortPerson(CompareByAge())
    age_sort.sort(person_list)
    print("根据年龄排序的结果：")
    for person in person_list:
        print(person.showMyself())

    print('\b')

    height_sort = SortPerson(CompareByHeight())
    height_sort.sort(person_list)
    print("根据身高排序的结果：")
    for person in person_list:
        print(person.showMyself())


if __name__ == '__main__':
    testSortPerson()
