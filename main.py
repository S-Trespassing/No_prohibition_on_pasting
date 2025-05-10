#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：main.py 
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：Trespassing
@Date    ：2025/5/9 20:26 
"""
import json
import webbrowser
from pathlib import Path
import pyperclip
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QTimer)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import (QAction, QFont)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
                               QPushButton, QStatusBar, QVBoxLayout,
                               QWidget, QLineEdit, QDialog, QMessageBox)
from pynput.keyboard import Controller
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 400)
        MainWindow.setMinimumSize(QSize(640, 400))
        MainWindow.setMaximumSize(QSize(640, 400))
        self.act1 = QAction(MainWindow)
        self.act1.setObjectName(u"act1")
        self.act2 = QAction(MainWindow)
        self.act2.setObjectName(u"act2")
        self.is_top = QAction(MainWindow)
        self.is_top.setObjectName(u"is_top")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(51, 9, 530, 311))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.notice = QLabel(self.layoutWidget)
        self.notice.setObjectName(u"notice")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(11)
        self.notice.setFont(font)
        self.notice.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.notice)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.start_bt = QPushButton(self.layoutWidget)
        self.start_bt.setObjectName(u"start_bt")

        self.horizontalLayout.addWidget(self.start_bt)

        self.paste_bt = QPushButton(self.layoutWidget)
        self.paste_bt.setObjectName(u"paste_bt")

        self.horizontalLayout.addWidget(self.paste_bt)

        self.parttime_bt = QPushButton(self.layoutWidget)
        self.parttime_bt.setObjectName(u"parttime_bt")

        self.horizontalLayout.addWidget(self.parttime_bt)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.content = QPlainTextEdit(self.layoutWidget)
        self.content.setObjectName(u"content")

        self.verticalLayout.addWidget(self.content)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.is_top)
        self.menu.addSeparator()
        self.menu.addAction(self.act1)
        self.menu.addAction(self.act2)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"(\uff0f\u2035\u0414\u2032)\uff0f~ \u2567\u2567(\u7981\u6b62\u7c98\u8d34)", None))
        self.act1.setText(QCoreApplication.translate("MainWindow", u"\u8054\u7cfb\u4f5c\u8005", None))
        self.act2.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u76f4\u8fbe", None))
        self.is_top.setText(QCoreApplication.translate("MainWindow", u"取消窗口置顶", None))
        self.notice.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u95f4\u9694\u65f6\u95f4:", None))
        self.start_bt.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.paste_bt.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\u7c98\u8d34", None))
        self.parttime_bt.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u95f4\u9694\u65f6\u95f4", None))
        self.content.setPlainText("")
        self.content.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u8981\u8f93\u5165\u7684\u5185\u5bb9;", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"更多", None))
    # retranslateUi
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 194)
        Dialog.setMinimumSize(QSize(400, 194))
        Dialog.setMaximumSize(QSize(400, 194))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 130, 75, 24))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 60, 231, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u8bbe\u7f6e\u95f4\u9694\u65f6\u95f4", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u8bf7\u8f93\u5165\u95f4\u9694\u65f6\u95f4:", None))
class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_conform)
        self.time=None
    def on_conform(self):
        con=self.ui.lineEdit.text()
        if con.isdecimal():
            #QMessageBox并不支持指定参数传参
            # (父窗口, 标题, 消息内容, 按钮组合, 默认按钮)
            QMessageBox.information(self,"成功",f"设置的间隔时间为:{con}")
            # QDialog的一个方法,用于以接受状态关闭对话框
            self.time=con
            self.accept()
        else:
            QMessageBox.warning(self,"错误","请输入间隔时间!")
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config_dic=None
        with open("config.json",'r') as f:
            self.config_dic=json.load(f)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.parttime_bt.clicked.connect(self.show_dialog)
        self.ui.start_bt.clicked.connect(self.start_countdown)
        self.ui.paste_bt.clicked.connect(lambda :self.ui.content.setPlainText(pyperclip.paste()))
        self.timer=QTimer()
        self.timer.timeout.connect(self.update_notice)
        self.time=self.config_dic['time']
        self.ui.notice.setText(f"当前间隔时间为{self.time}秒")
        self.remain=self.time
        self.ui.act1.triggered.connect(lambda:webbrowser.open_new_tab("https://qm.qq.com/cgi-bin/qm/qr?k=qIaENQvu9-jWTr5x2NUC2s-jTupUokdk"))
        self.ui.act2.triggered.connect(lambda:webbrowser.open_new_tab("https://github.com/S-Trespassing/No_prohibition_on_pasting"))
        self.ui.is_top.triggered.connect(self.updata_top)
        # 窗口置顶
        self.is_top=True
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.ui.is_top.setText("取消窗口置顶")
    def change_top(self):
        if self.is_top:
            return (Qt.Window |
                 Qt.WindowCloseButtonHint |
                 Qt.WindowMinimizeButtonHint |
                 Qt.WindowStaysOnTopHint)
        else:
            return (Qt.Window |
                 Qt.WindowCloseButtonHint |
                 Qt.WindowMinimizeButtonHint)

    def updata_top(self):
        self.is_top=not self.is_top
        if self.is_top:
            self.setWindowFlags(self.change_top())
            self.ui.is_top.setText("取消窗口置顶")
        else:
            self.setWindowFlags(self.change_top())
            self.ui.is_top.setText("设置窗口置顶")
        self.show()

    def update_json(self):
        with open("config.json",'w') as f:
            json.dump(self.config_dic,f)
    def show_dialog(self):
        dialog=MyDialog()
        if self.is_top:
            dialog.setWindowFlags(self.change_top())
        if dialog.exec() == QDialog.Accepted:
            self.ui.notice.setText(f"当前间隔时间为{dialog.time}秒")
            self.time=int(dialog.time)
            self.config_dic["time"]=self.time
            self.update_json()
    def type_words(self):
        keyboard=Controller()
        keyboard.type(self.ui.content.toPlainText())
        self.ui.notice.setText("输入结束ξ( ✿＞◡❛)")
    # 倒计时函数
    def start_countdown(self):
        if self.config_dic['is_dialog']:
            QMessageBox.warning(self,"警告","开始前务必保证输入法为英文模式!\n此窗口后续不再弹出...")
            self.config_dic["is_dialog"]=False
            self.update_json()
        self.remain=self.time
        self.timer.start(1000)
        self.update_notice()

    def update_notice(self):
        if self.remain>0:
            self.ui.notice.setText(f"时间剩余:{self.remain}秒")
            self.remain-=1
        else:
            self.timer.stop()
            self.ui.notice.setText("正在输入٩(๑•̀ω•́๑)۶...")
            self.type_words()
if __name__=='__main__':
    if not Path("config.json").exists():
        with open("config.json", 'w') as f:
            json.dump({'time':5,"is_dialog":True}, f)
    appui = QApplication([])
    mainw = MainWindow()
    mainw.show()
    appui.exec()