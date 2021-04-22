#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/24 16:44
# @Author  : StephenCurry
# @File    : StackedWindow.py
# @Software: PyCharm

import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class StackedExample(QtWidgets.QWidget):
    def __init__(self):
        super(StackedExample, self).__init__()

        # self.setGeometry(300, 50, 10, 10)
        self.resize(500, 500)
        self.setWindowTitle('Glocalme Tool')

        self.leftList = QtWidgets.QListWidget()
        self.leftList.insertItem(0, 'FOTA')
        self.leftList.insertItem(1, '显示及设置')

        self.stack1 = QtWidgets.QTableWidget(10, 7)
        self.stack1.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.stack2 = QtWidgets.QTableWidget(10, 7)
        self.stack2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


        self.stack1UI()
        self.stack2UI()

        self.stack = QtWidgets.QStackedWidget(self)
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)

        HBox = QtWidgets.QHBoxLayout()
        HBox.addWidget(self.leftList)
        HBox.addWidget(self.stack)

        self.setLayout(HBox)

        self.leftList.currentRowChanged.connect(self.display)


    def stack1UI(self):
        pass

    def stack2UI(self):
        pass

    def display(self, i):
        self.stack.setCurrentIndex(i)

def main():
    app = QtWidgets.QApplication(sys.argv)
    win = StackedExample()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()






