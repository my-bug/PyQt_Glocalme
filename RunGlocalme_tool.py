#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/20 12:23
# @Author  : StephenCurry
# @File    : RunGlocalme_tool.py
# @Software: PyCharm

import sys
from glocalme_tool_bac import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())