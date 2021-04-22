#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/23 11:41
# @Author  : StephenCurry
# @File    : twoWindow.py
# @Software: PyCharm

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QLabel, QApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGUI()
        #这一句比较关键，先声明这个窗体2等到需要show的时候在展示出来。
        self.child = Exaple2()
    def initGUI(self):
        btn = QPushButton('打开窗体', self)
        btn.setToolTip('这是个btn')
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.showSecond)

    def showSecond(self):
        self.child.show()

#第二个窗口
class Exaple2(QWidget):
    def __init__(self):
        super().__init__()
        self.configUI()
    def configUI(self):
        self.lable = QLabel('我是第二个窗体', self)
        self.lable.setWordWrap(True)  # 自动换行
        #设置frame
        self.lable.setGeometry(50, 100, 200, 50)
        #设置新窗体frame
        self.setGeometry(500,500,300,300)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Example()
    main.show()
    sys.exit(app.exec_())