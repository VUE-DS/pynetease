# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import json
import os
import traceback

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QFont
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from NetEase import apis

from MyQLabel import MyQLabel

class Ui_Dialog(object):

    loginSignal = pyqtSignal(dict,bool,str,str,str)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(367, 548)
        Dialog.setStyleSheet("#Dialog {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"#widget {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"}\n"
"#closeButton {\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"#closeButton:hover {\n"
"    color: white;\n"
"    background-color: rgb(232, 16, 16);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("border-radius:7px;")
        self.widget.setObjectName("widget")
        self.label_close = QtWidgets.QPushButton(self.widget)
        self.label_close.setGeometry(QtCore.QRect(320, 10, 16, 16))
        self.label_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_close.setStyleSheet("QPushButton#label_close:hover{background-color: rgba(0, 0, 0, 10);}\n"
"")
        self.label_close.setText("×")
        #self.label_close.setStyleSheet("QPushButton#label_close{font: 12pt \"微软雅黑\";}\n")
        font = QFont("Microsoft YaHei")
        font.setPointSize(15)
        self.label_close.setFont(font)
        self.label_close.setObjectName("label_close")
        self.button_login = QtWidgets.QPushButton(self.widget)
        self.button_login.setGeometry(QtCore.QRect(40, 330, 260, 40))
        self.button_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_login.setStyleSheet("QPushButton#button_login{\n"
"border:0px;\n"
"background-color: rgb(234, 72, 72);\n"
"border-radius:5px;\n"
"font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#button_login:hover{background-color: rgb(199, 46, 46);};")
        self.button_login.setObjectName("button_login")
        self.label_change_passwd = MyQLabel(self.widget)
        self.label_change_passwd.setGeometry(QtCore.QRect(240, 261, 51, 16))
        self.label_change_passwd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_change_passwd.setStyleSheet("font: 10pt \"微软雅黑\";\n"
"color: rgb(179,179,179);")
        self.label_change_passwd.setObjectName("label_change_passwd")
        self.label_register = MyQLabel(self.widget)
        self.label_register.setGeometry(QtCore.QRect(154, 380, 31, 21))
        self.label_register.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_register.setStyleSheet("font: 11pt \"微软雅黑\";\n"
"color: rgb(0, 0, 0);")
        self.label_register.setOpenExternalLinks(True)
        self.label_register.setObjectName("label_register")
        self.label_2 = MyQLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 48, 301, 161))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/pic/images/login_phone.png"))
        self.label_2.setObjectName("label_2")
        self.label_login_bg_border = MyQLabel(self.widget)
        self.label_login_bg_border.setGeometry(QtCore.QRect(40, 210, 260, 80))
        self.label_login_bg_border.setStyleSheet("border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(216,216,216);\n"
"border-radius:5px;")
        self.label_login_bg_border.setText("")
        self.label_login_bg_border.setObjectName("label_login_bg_border")
        self.label_rule_3 = MyQLabel(self.widget)
        self.label_rule_3.setGeometry(QtCore.QRect(221, 488, 91, 16))
        self.label_rule_3.setStyleSheet("font: 9pt \"微软雅黑\";\n"
"color: rgb(80, 125, 175);")
        self.label_rule_3.setObjectName("label_rule_3")
        self.lineEdit_country_callingCode = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_country_callingCode.setGeometry(QtCore.QRect(71, 220, 31, 20))
        self.lineEdit_country_callingCode.setStyleSheet("border-width:0;\n"
"font: 8pt \"微软雅黑\";\n"
"border-style:outset;")
        self.lineEdit_country_callingCode.setObjectName("lineEdit_country_callingCode")
        self.lineEdit_password = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_password.setGeometry(QtCore.QRect(70, 259, 161, 20))
        self.lineEdit_password.setStyleSheet("border-width:0;\n"
"font: 75 11pt \"微软雅黑\";\n"
"border-style:outset;")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_rule_2 = MyQLabel(self.widget)
        self.label_rule_2.setGeometry(QtCore.QRect(147, 488, 71, 16))
        self.label_rule_2.setStyleSheet("font: 9pt \"微软雅黑\";\n"
"color: rgb(80, 125, 175);")
        self.label_rule_2.setObjectName("label_rule_2")
        self.label_163_icon = MyQLabel(self.widget)
        self.label_163_icon.setGeometry(QtCore.QRect(260, 420, 41, 41))
        self.label_163_icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_163_icon.setStyleSheet("QLabel#label_163_icon{background-image: url(:/pic/images/163_icon.png);}\n"
"QLabel#label_163_icon:hover{background-image: url(:/pic/images/163_hover_icon.png);};")
        self.label_163_icon.setText("")
        self.label_163_icon.setObjectName("label_163_icon")
        self.checkBox_rule = QtWidgets.QCheckBox(self.widget)
        self.checkBox_rule.setGeometry(QtCore.QRect(30, 489, 51, 16))
        self.checkBox_rule.setStyleSheet("font: 9pt \"微软雅黑\";\n"
"selection-color: rgb(207, 32, 255);\n"
"color: rgb(129, 129, 129);")
        self.checkBox_rule.setChecked(True)
        self.checkBox_rule.setObjectName("checkBox_rule")
        self.label_weibo_icon = MyQLabel(self.widget)
        self.label_weibo_icon.setGeometry(QtCore.QRect(188, 419, 41, 41))
        self.label_weibo_icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_weibo_icon.setStyleSheet("QLabel#label_weibo_icon{background-image: url(:/pic/images/weibo_icon.png);}\n"
"QLabel#label_weibo_icon:hover{background-image: url(:/pic/images/weibo_hover_icon.png);};")
        self.label_weibo_icon.setText("")
        self.label_weibo_icon.setObjectName("label_weibo_icon")
        self.label_qq_icon = MyQLabel(self.widget)
        self.label_qq_icon.setGeometry(QtCore.QRect(112, 420, 41, 41))
        self.label_qq_icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_qq_icon.setStyleSheet("QLabel#label_qq_icon{background-image: url(:/pic/images/qq_icon.png);}\n"
"QLabel#label_qq_icon:hover{background-image: url(:/pic/images/qq_hover_icon.png);};")
        self.label_qq_icon.setText("")
        self.label_qq_icon.setObjectName("label_qq_icon")
        self.label_rule_1 = MyQLabel(self.widget)
        self.label_rule_1.setGeometry(QtCore.QRect(72, 488, 71, 16))
        self.label_rule_1.setStyleSheet("font: 9pt \"微软雅黑\";\n"
"color: rgb(80, 125, 175);")
        self.label_rule_1.setObjectName("label_rule_1")
        self.lineEdit_phonenum = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_phonenum.setGeometry(QtCore.QRect(120, 220, 161, 20))
        self.lineEdit_phonenum.setStyleSheet("border-width:0;\n"
"font: 75 11pt \"微软雅黑\";\n"
"border-style:outset;")
        self.lineEdit_phonenum.setObjectName("lineEdit_phonenum")
        self.checkBox_autoLogin = QtWidgets.QCheckBox(self.widget)
        self.checkBox_autoLogin.setGeometry(QtCore.QRect(40, 300, 71, 16))
        self.checkBox_autoLogin.setStyleSheet("font: 9pt \"微软雅黑\";\n"
"selection-color: rgb(207, 32, 255);\n"
"color: rgb(129, 129, 129);")
        self.checkBox_autoLogin.setChecked(True)
        self.checkBox_autoLogin.setObjectName("checkBox_autoLogin")
        self.label_locker_icon = MyQLabel(self.widget)
        self.label_locker_icon.setGeometry(QtCore.QRect(50, 260, 18, 21))
        self.label_locker_icon.setText("")
        self.label_locker_icon.setPixmap(QtGui.QPixmap(":/pic/images/locker_icon.png"))
        self.label_locker_icon.setObjectName("label_locker_icon")
        self.label_phone_icon = MyQLabel(self.widget)
        self.label_phone_icon.setGeometry(QtCore.QRect(50, 219, 18, 21))
        self.label_phone_icon.setText("")
        self.label_phone_icon.setPixmap(QtGui.QPixmap(":/pic/images/phone_icon.png"))
        self.label_phone_icon.setObjectName("label_phone_icon")
        self.label_wechat_icon = MyQLabel(self.widget)
        self.label_wechat_icon.setGeometry(QtCore.QRect(40, 420, 41, 41))
        self.label_wechat_icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_wechat_icon.setStyleSheet("QLabel#label_wechat_icon{background-image: url(:/pic/images/wechat_icon.png);}\n"
"QLabel#label_wechat_icon:hover{background-image: url(:/pic/images/wechat_hover_icon.png);};")
        self.label_wechat_icon.setText("")
        self.label_wechat_icon.setObjectName("label_wechat_icon")
        self.label_vertical_line = MyQLabel(self.widget)
        self.label_vertical_line.setGeometry(QtCore.QRect(107, 210, 1, 40))
        self.label_vertical_line.setStyleSheet("border-width: 1px;border-style: solid;border-color: rgb(217, 217, 217);")
        self.label_vertical_line.setText("")
        self.label_vertical_line.setObjectName("label_vertical_line")
        self.label_horizontal_line = MyQLabel(self.widget)
        self.label_horizontal_line.setGeometry(QtCore.QRect(40, 250, 260, 1))
        self.label_horizontal_line.setStyleSheet("border-width: 1px;border-style: solid;border-color: rgb(217, 217, 217);")
        self.label_horizontal_line.setText("")
        self.label_horizontal_line.setObjectName("label_horizontal_line")
        self.label_2.raise_()
        self.label_login_bg_border.raise_()
        self.label_close.raise_()
        self.button_login.raise_()
        self.label_change_passwd.raise_()
        self.label_register.raise_()
        self.label_rule_3.raise_()
        self.lineEdit_country_callingCode.raise_()
        self.lineEdit_password.raise_()
        self.label_rule_2.raise_()
        self.label_163_icon.raise_()
        self.checkBox_rule.raise_()
        self.label_weibo_icon.raise_()
        self.label_qq_icon.raise_()
        self.label_rule_1.raise_()
        self.lineEdit_phonenum.raise_()
        self.checkBox_autoLogin.raise_()
        self.label_locker_icon.raise_()
        self.label_phone_icon.raise_()
        self.label_wechat_icon.raise_()
        self.label_vertical_line.raise_()
        self.label_horizontal_line.raise_()
        self.verticalLayout.addWidget(self.widget)
        self.label_close.clicked.connect(self.close)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.label_qq_icon.connect_customized_slot(self.no_login_tips)
        self.label_wechat_icon.connect_customized_slot(self.no_login_tips)
        self.label_163_icon.connect_customized_slot(self.no_login_tips)
        self.label_weibo_icon.connect_customized_slot(self.no_login_tips)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.button_login.clicked.connect(self.login)
        self.load_data()
        self.label_rule_1.connect_customized_slot(self.label1_clicked)
        self.label_rule_2.connect_customized_slot(self.label2_clicked)
        self.label_rule_3.connect_customized_slot(self.label3_clicked)
        self.label_change_passwd.connect_customized_slot(self.label_change_passwd_clicked)
        self.label_register.connect_customized_slot(self.label_register_clicked)

    def label_register_clicked(self):
        import webbrowser as web
        web.open_new('https://st.music.163.com/official-terms/service')

    def label_change_passwd_clicked(self):
        import webbrowser as web
        web.open_new('https://music.163.com/')

    def label1_clicked(self):
        import webbrowser as web
        web.open_new('https://st.music.163.com/official-terms/service')

    def label2_clicked(self):
        import webbrowser as web
        web.open_new('https://st.music.163.com/official-terms/privacy')

    def label3_clicked(self):
        import webbrowser as web
        web.open_new('https://st.music.163.com/official-terms/children')

    def no_login_tips(self):
        QMessageBox.information(self.label_close,"Tips:","这几个登陆都还没时间做....目前只能用手机登陆", QMessageBox.Close)

    def login(self):
        if not (self.checkBox_rule.isChecked()):
            QMessageBox.information(self.button_login, "Tips:", "请勾选同意 《服务条款》、《隐私政策》、《儿童隐私政策》！")
            return 0
        try:
            from NetEase import apis
            if len(self.lineEdit_phonenum.text()) < 11:
                QMessageBox.information(self.button_login,"Tips:","手机号填写错误，请重新填写！")
                return 0
            if len(self.lineEdit_password.text()) < 6:
                QMessageBox.information(self.button_login,"Tips:","密码长度小于6位！")
                return 0
            citycode = self.lineEdit_country_callingCode.text().replace('+','')
            res = apis.login.LoginViaCellphone(phone=self.lineEdit_phonenum.text(), password=self.lineEdit_password.text(),
                                               ctcode=int(citycode))
            if (res['success'] == True):
                print("登陆成功")
                if (self.checkBox_autoLogin.isChecked()):
                    self.loginSignal.emit(res, True, self.lineEdit_phonenum.text(), self.lineEdit_password.text(), citycode)  # 发射信号
                else:
                    self.loginSignal.emit(res, False, self.lineEdit_phonenum.text(), self.lineEdit_password.text(), citycode)
                self.close()

        except Exception as e:
            traceback.print_exc()
            try:
                res = eval(e.__str__())
                print(res)
                QMessageBox.information(self.button_login, "Tips:", res['message'])
            except:
                traceback.print_exc()
    def load_data(self):
        if (os.path.exists('./data/config.json')):
            with open('./data/config.json', 'r') as f:
                data = json.loads(f.read())
                self.lineEdit_phonenum.setText(data['phonenum'])
                self.lineEdit_password.setText(data['password'])
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "登录"))
        self.button_login.setText(_translate("Dialog", "登 录"))
        self.label_change_passwd.setText(_translate("Dialog", "重设密码"))
        self.label_register.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://music.163.com/\"><span style=\" text-decoration: underline; color:black;\">注册</span></a></p></body></html>"))
        self.label_rule_3.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://st.music.163.com/official-terms/children\" style=\"text-decoration:none;\"><span style=\" color:#507daf;\">《儿童隐私政策》</span></a></p></body></html>"))
        self.lineEdit_country_callingCode.setText(_translate("Dialog", "+86"))
        self.lineEdit_password.setPlaceholderText(_translate("Dialog", "请输入密码"))
        self.label_rule_2.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://st.music.163.com/official-terms/privacy\" style=\"text-decoration:none;\"><span style=\" color:#507daf;\">《隐私政策》</span></a></p></body></html>"))
        self.checkBox_rule.setText(_translate("Dialog", "同意"))
        self.label_rule_1.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://st.music.163.com/official-terms/service\" style=\"text-decoration:none;\"><span style=\" color:#507daf;\">《服务条款》</span></a></p></body></html>"))
        self.lineEdit_phonenum.setPlaceholderText(_translate("Dialog", "请输入手机号"))
        self.checkBox_autoLogin.setText(_translate("Dialog", "自动登录"))
import login_rc
