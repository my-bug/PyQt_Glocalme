#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 17:50
# @Author  : StephenCurry
# @File    : test_window.py
# @Software: PyCharm

import sys, subprocess
from models import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import *

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(1100, 500)
        self.setMaximumWidth(1100)
        self.setWindowTitle("优克联自动化测试")
        layout = QVBoxLayout()

        layout_01 = QHBoxLayout()
        label = QLabel("测试版本：")
        lineEdit = QLineEdit()
        lineEdit.setReadOnly(True)
        btn_01 = QPushButton()
        btn_01.setIcon(QIcon('static/kaishi.png'))
        layout_01.addWidget(label)
        layout_01.addWidget(lineEdit)
        layout_01.addWidget(btn_01)


        layout_table = QHBoxLayout()

        tableWidget = QTableWidget(4, 8)
        # 设置表格可伸缩模式
        # tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        # tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.Interactive)

        # 如果设置了表格可伸缩模式，就不能设置如下每列的宽度
        tableWidget.setColumnWidth(0, 150)
        tableWidget.setColumnWidth(1, 50)
        tableWidget.setColumnWidth(2, 200)
        tableWidget.setColumnWidth(3, 200)
        tableWidget.setColumnWidth(4, 200)
        tableWidget.setColumnWidth(5, 100)
        tableWidget.setColumnWidth(6, 50)
        tableWidget.setColumnWidth(7, 110)



        # 将表格变为禁止编辑
        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置为不显示网格
        # tableWidget.setShowGrid(False)

        # 设置表头的字体、颜色
        tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{background-color:rgb(155, 194, 230);font:11pt '宋体';color: black;};")

        # tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)


        """
        # 设置表头的字体、颜色
        for x in range(self.MyTable.columnCount()):
            headItem = self.MyTable.horizontalHeaderItem(x)  # 获得水平方向表头的Item对象
            headItem.setFont(textFont)  # 设置字体
            headItem.setBackgroundColor(QColor(0, 60, 10))  # 设置单元格背景颜色
            headItem.setTextColor(QColor(200, 111, 30))  # 设置文字颜色
        """


        tableWidget.setHorizontalHeaderLabels(['测试用例', '优先级', '测试前准备', '测试步骤', '预期结果', '测试结果', '执行', '备注'])

        # 添加数据
        newItem = QTableWidgetItem('云卡网络-开机检测')
        tableWidget.setItem(0, 0, newItem)

        one = ('手动检测', '1', '1.登录云卡;\n2.设备重启;', '1.进入fota界面手动点击升级;\n2.查看是否可以检测到新版本', '可以检测到版本')
        # for i in one:
        #     newItem = QTableWidgetItem(i)
        #     tableWidget.setItem(1, one.index(i), newItem)

        for i in range(5):
            # print(i)
            if i in [2, 3, 4]:
                edit = QTextEdit()
                # 设置文本内容不可编辑
                edit.setFocusPolicy(Qt.NoFocus)
                edit.setText(one[i])
                tableWidget.setCellWidget(1, i, edit)
            else:
                newItem = QTableWidgetItem(one[i])
                tableWidget.setItem(1, i, newItem)

        newItem01 = QPushButton()
        newItem01.setIcon(QIcon('static/kaishi.png'))
        newItem01.clicked.connect(self.excute)
        tableWidget.setCellWidget(1, 6, newItem01)




        layout_table.addWidget(tableWidget)
        layout.addLayout(layout_01)
        layout.addLayout(layout_table)

        self.setLayout(layout)

    def excute(self):
        pass

def main():
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

