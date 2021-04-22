#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time    : 2021/3/18 18:12
# @Author  : StephenCurry
# @File    : test.py
# @Software: PyCharm


import sys
from PyQt5.QtWidgets import (QApplication, QMessageBox, QWidget, QPushButton)
from random import randint

class A:
    def what(self):
        print('777')

dic = {0: 'A'}

d = eval(dic[0])()
d.what()


