#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/24 18:08
# @Author  : StephenCurry
# @File    : Glocalme.py
# @Software: PyCharm

import sys, subprocess
from models import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal

BASEDIR = os.path.dirname(__file__)

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.device = U3()
        self.log = Logger(log_level='logging.INFO')
        self.initUI()


    def initUI(self):
        self.setWindowTitle("优克联工具")
        self.resize(600, 500)
        self.setMaximumWidth(500)
        self.setMaximumHeight(600)

        # 水平布局
        layout = QHBoxLayout()

        self.leftList = QListWidget()

        #设置左侧菜单最大宽度
        self.leftList.setMaximumWidth(100)

        self.leftList.insertItem(0, 'U3X')
        self.leftList.insertItem(1, 'G4')
        self.leftList.insertItem(2, 'G4S')
        self.leftList.insertItem(4, 'U5')
        self.leftList.insertItem(4, 'G3')

        self.stack = QStackedWidget()

        self.stack_U3X = QWidget()
        self.stack_G4 = QWidget()
        self.stack_G4P = QWidget()
        self.stack_U5 = QWidget()
        self.stack_G3 = QWidget()

        self.stackUI_U3X()
        self.stackUI_G4()
        self.stackUI_G4P()
        self.stackUI_U5()
        self.stackUI_G3()

        self.stack.addWidget(self.stack_U3X)
        self.stack.addWidget(self.stack_G4)
        self.stack.addWidget(self.stack_G4P)
        self.stack.addWidget(self.stack_U5)
        self.stack.addWidget(self.stack_G3)

        layout.addWidget(self.leftList)
        layout.addWidget(self.stack)

        self.setLayout(layout)

        self.leftList.currentRowChanged.connect(self.display)


    def display(self, i):
        device_type = self.leftList.item(i).text()
        self.device = eval(device_type)()
        self.stack.setCurrentIndex(i)

    def stackUI_U3X(self):
        layout = QFormLayout()
        # label = QLabel()
        # label.setMinimumHeight(35)
        # label.setAlignment(Qt.AlignCenter)
        # if self.device.connect_device():
        #     label.setText("设备已连接")
        #     label.setStyleSheet("background-color: green")
        # else:
        #     label.setText("设备未连接")
        #     label.setStyleSheet("background-color:red")
        btn_reboot = QPushButton("重启")
        btn_reboot.clicked.connect(self.reboot)
        btn_PullLog = QPushButton("提取日志")
        btn_PullLog.clicked.connect(self.pullLog)
        btn_root = QPushButton("获取root权限")
        btn_root.clicked.connect(self.root)
        btn_saas2 = QPushButton("切换到SaaS2")
        btn_saas2.clicked.connect(self.changeToSaaS2)
        # layout.addWidget(label)
        layout.addWidget(btn_reboot)
        layout.addWidget(btn_PullLog)
        layout.addWidget(btn_root)
        layout.addWidget(btn_saas2)
        self.stack_U3X.setLayout(layout)


    def stackUI_G4(self):
        pass

    def stackUI_G4P(self):
        layout = QFormLayout()
        btn_reboot = QPushButton("重启")
        btn_reboot.clicked.connect(self.reboot)
        btn_PullLog = QPushButton("提取日志")
        btn_PullLog.clicked.connect(self.pullLog)
        btn_root = QPushButton("获取root权限")
        btn_root.clicked.connect(self.root)
        btn_saas2 = QPushButton("切换到SaaS2")
        btn_saas2.clicked.connect(self.changeToSaaS2)
        btn_logoutCloudsim = QPushButton("停止云卡登录")
        btn_logoutCloudsim.clicked.connect(self.logoutCloudsim)
        btn_displayBattery = QPushButton("显示电量百分比")
        btn_displayBattery.clicked.connect(self.displayBattery)
        layout.addWidget(btn_reboot)
        layout.addWidget(btn_PullLog)
        layout.addWidget(btn_root)
        layout.addWidget(btn_saas2)
        layout.addWidget(btn_logoutCloudsim)
        layout.addWidget(btn_displayBattery)
        self.stack_G4P.setLayout(layout)

    def stackUI_U5(self):
        pass

    def stackUI_G3(self):
        layout = QFormLayout()
        btn_pullUcLog = QPushButton("提取UCLOG")
        btn_pullUcLog.clicked.connect(self.pullUcLog)

        layout.addWidget(btn_pullUcLog)
        self.stack_G3.setLayout(layout)

    def reboot(self):
        # subprocess.getoutput("adb reboot")
        self.device.reboot()

    def pullLog(self):
        log_file = QFileDialog()
        log_file.setFileMode(QFileDialog.Directory)
        file_dir = log_file.getExistingDirectory(self, "请选择日志保存路径（非中文路径）", './')
        if file_dir:
            print(file_dir)
            self.device.pull_AllLog(file_dir)
            reply = QMessageBox.about(self, "提示", "日志提取完成")
        else:
            print("OK")



    def root(self):
        self.device.root()

    def changeToSaaS2(self):
        # self.device.changeToSaaS2()
        # self.device.root()
        ip_file = os.path.join(BASEDIR, 'grt--saas2.cfg')
        res = subprocess.getstatusoutput(' '.join(['adb push', ip_file, '/productinfo/ucloud/grt.cfg']))
        print(res)
        if res[0] == 0:
            QMessageBox.about(self, '提示', '切换到SaaS2成功')
        else:
            if "Operation not permitted" in res[1]:
                QMessageBox.about(self, '提示', '切换到SaaS2失败，请先root后再尝试')

    def logoutCloudsim(self):
        res = subprocess.getoutput("adb shell am broadcast -a com.ucloudlink.cmd.logout")
        print(res)
        if res == 'Broadcasting: Intent { act=com.ucloudlink.cmd.logout flg=0x400000 }\nBroadcast completed: result=0':
            reply = QMessageBox.about(self, "提示", "已经停止云卡登录")

    def displayBattery(self):
        battery = self.device.battery_percentage()
        QMessageBox.about(self, "提示", "当前电量百分比：%s" % battery)

    def pullUcLog(self):
        log_file = QFileDialog()
        log_file.setFileMode(QFileDialog.Directory)
        file_dir = log_file.getExistingDirectory(self, "请选择日志保存路径（非中文路径）", './')
        if file_dir:
            print(file_dir)
            self.device.pullUcLog(file_dir)
            reply = QMessageBox.about(self, "提示", "日志提取完成")
        else:
            print("OK")


    def wakey(self):
        pass


        # print(file)



def main():
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
