#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 17:50
# @Author  : StephenCurry
# @File    : test_window.py
# @Software: PyCharm

import sys, subprocess
from models import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(1000, 500)
        self.setWindowTitle("优克联自动化测试")
        layout = QHBoxLayout()

        tableWidget = QTableView()

        model = QStandardItemModel(4, 8)
        model.

        tableWidget.setModel(model)





        layout.addWidget(tableWidget)
        self.setLayout(layout)

    def view_db(self):
        self.model = QStandardItemModel(4, 8)
        self.tableWidget.setModel(self.model)


def main():
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
