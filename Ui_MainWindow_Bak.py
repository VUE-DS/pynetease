# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import math
import traceback

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pyncm import apis



class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1022, 670)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_top_bg = QtWidgets.QLabel(self.centralwidget)
        self.label_top_bg.setGeometry(QtCore.QRect(10, 10, 1001, 60))
        self.label_top_bg.setStyleSheet("background-color: rgb(57, 175, 234);")
        self.label_top_bg.setText("")
        self.label_top_bg.setObjectName("label_top_bg")
        self.label_left_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_left_logo.setGeometry(QtCore.QRect(10, 10, 191, 51))
        self.label_left_logo.setStyleSheet("background-image: url(:/png/images/left_logo.png);")
        self.label_left_logo.setText("")
        self.label_left_logo.setObjectName("label_left_logo")
        self.label_input_search_bg = QtWidgets.QLabel(self.centralwidget)
        self.label_input_search_bg.setGeometry(QtCore.QRect(280, 26, 171, 31))
        self.label_input_search_bg.setStyleSheet("border-radius:15px;\n"
"font: 10pt \"微软雅黑\";\n"
"margin left: 10px; \n"
"background:rgba(235,235,235,0.5);")
        self.label_input_search_bg.setText("")
        self.label_input_search_bg.setObjectName("label_input_search_bg")
        self.label_search_icon = QtWidgets.QLabel(self.centralwidget)
        self.label_search_icon.setGeometry(QtCore.QRect(289, 34, 16, 16))
        self.label_search_icon.setStyleSheet("")
        self.label_search_icon.setText("")
        self.label_search_icon.setPixmap(QtGui.QPixmap(":/png/images/search_ico.png"))
        self.label_search_icon.setScaledContents(True)
        self.label_search_icon.setObjectName("label_search_icon")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(309, 33, 127, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius:0px;\n"
"background:rgba(0,0,0,0);\n"
"color:white;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_top_avatar = QtWidgets.QLabel(self.centralwidget)
        self.label_top_avatar.setGeometry(QtCore.QRect(550, 26, 32, 32))
        self.label_top_avatar.setStyleSheet("")
        self.label_top_avatar.setText("")
        self.label_top_avatar.setPixmap(QtGui.QPixmap(":/png/images/avatar.png"))
        self.label_top_avatar.setScaledContents(True)
        self.label_top_avatar.setObjectName("label_top_avatar")
        self.label_top_id = QtWidgets.QLabel(self.centralwidget)
        self.label_top_id.setGeometry(QtCore.QRect(590, 35, 141, 16))
        self.label_top_id.setStyleSheet("font: 9pt \"微软雅黑\";\n"
"color:rgba(255,255,255,0.9);")
        self.label_top_id.setObjectName("label_top_id")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(680, 38, 35, 12))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/png/images/vip4.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_minimize = QtWidgets.QLabel(self.centralwidget)
        self.label_minimize.setGeometry(QtCore.QRect(920, 31, 21, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_minimize.setFont(font)
        self.label_minimize.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_minimize.setObjectName("label_minimize")
        self.label_close = QtWidgets.QLabel(self.centralwidget)
        self.label_close.setGeometry(QtCore.QRect(960, 30, 21, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.label_close.setFont(font)
        self.label_close.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_close.setObjectName("label_close")
        self.label_main_bg = QtWidgets.QLabel(self.centralwidget)
        self.label_main_bg.setGeometry(QtCore.QRect(10, 70, 1001, 581))
        self.label_main_bg.setStyleSheet("background-color: rgb(255,255,255);")
        self.label_main_bg.setText("")
        self.label_main_bg.setObjectName("label_main_bg")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(24, 586, 50, 50))
        self.label_2.setStyleSheet("border-radius:10px;\n"
"background-image: url(:/png/images/album_default.jpg);\n"
"background-size:100% 100%;")
        self.label_2.setText("")
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_song_name = QtWidgets.QLabel(self.centralwidget)
        self.label_song_name.setGeometry(QtCore.QRect(90, 593, 161, 16))
        self.label_song_name.setStyleSheet("font: 10pt \"微软雅黑\";\n"
"color: rgb(77, 77, 77);")
        self.label_song_name.setObjectName("label_song_name")
        self.label_song_name_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_song_name_2.setGeometry(QtCore.QRect(90, 615, 161, 16))
        self.label_song_name_2.setStyleSheet("font: 10pt \"微软雅黑\";\n"
"color: rgb(77, 77, 77);")
        self.label_song_name_2.setObjectName("label_song_name_2")
        self.slider_progress = QtWidgets.QSlider(self.centralwidget)
        self.slider_progress.setGeometry(QtCore.QRect(318, 624, 411, 21))
        self.slider_progress.setStyleSheet("QSlider::handle:horizontal{width:6px;height:6px;background-color:rgb(57, 175, 234);margin:-2px 0px -2px 0px;border-radius:3px;}\n"
"QSlider::groove:horizontal{height:3px;background-color:rgb(219,219,219);}\n"
"QSlider::add-page:horizontal{background-color:rgb(219,219,219);}\n"
"QSlider::sub-page:horizontal{background-color:rgb(57, 175, 234);}")
        self.slider_progress.setOrientation(QtCore.Qt.Horizontal)
        self.slider_progress.setObjectName("slider_progress")
        self.label_progress_left = QtWidgets.QLabel(self.centralwidget)
        self.label_progress_left.setGeometry(QtCore.QRect(280, 626, 35, 16))
        self.label_progress_left.setStyleSheet("font: 9pt \"微软雅黑\";\n"
"color: rgb(159, 159, 159);")
        self.label_progress_left.setObjectName("label_progress_left")
        self.label_progress_right = QtWidgets.QLabel(self.centralwidget)
        self.label_progress_right.setGeometry(QtCore.QRect(737, 626, 35, 16))
        self.label_progress_right.setStyleSheet("font: 9pt \"微软雅黑\";\n"
"color: rgb(159, 159, 159);")
        self.label_progress_right.setObjectName("label_progress_right")
        self.button_play = QtWidgets.QPushButton(self.centralwidget)
        self.button_play.setGeometry(QtCore.QRect(500, 590, 35, 35))
        self.button_play.setStyleSheet("QPushButton#button_play{\n"
"    background-color: rgba(125, 125, 125, 30);\n"
"    border-radius:17px;\n"
"    background-image: url(:/png/images/play_button.png);\n"
"}\n"
"QPushButton#button_play:hover{\n"
"    background-color: rgba(125, 125, 125, 50);\n"
"};")
        self.button_play.setText("")
        self.button_play.setObjectName("button_play")
        self.button_last_song = QtWidgets.QPushButton(self.centralwidget)
        self.button_last_song.setGeometry(QtCore.QRect(460, 594, 25, 25))
        self.button_last_song.setStyleSheet("QPushButton#button_last_song{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    background-image: url(:/png/images/last_song.png);\n"
"}\n"
"QPushButton#button_last_song:hover{\n"
"    background-image: url(:/png/images/last_song_pressed.png);\n"
"};")
        self.button_last_song.setText("")
        self.button_last_song.setObjectName("button_last_song")
        self.button_next_song = QtWidgets.QPushButton(self.centralwidget)
        self.button_next_song.setGeometry(QtCore.QRect(548, 594, 25, 25))
        self.button_next_song.setStyleSheet("QPushButton#button_next_song{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    background-image: url(:/png/images/next_song.png);\n"
"}\n"
"QPushButton#button_next_song:hover{\n"
"    background-image: url(:/png/images/next_song_pressed.png);\n"
"};")
        self.button_next_song.setText("")
        self.button_next_song.setObjectName("button_next_song")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 80, 981, 491))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.lineEdit.returnPressed.connect(self.search_song_lineedit)
        self.retranslateUi(MainWindow)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        #self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QTableView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 600)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 50)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.tableWidget.horizontalHeaderItem(0).setForeground(QBrush(QColor(101, 101, 101)))
        self.tableWidget.horizontalHeaderItem(1).setForeground(QBrush(QColor(101, 101, 101)))
        self.tableWidget.horizontalHeaderItem(2).setForeground(QBrush(QColor(101, 101, 101)))
        self.tableWidget.horizontalHeaderItem(3).setForeground(QBrush(QColor(101, 101, 101)))
        self.tableWidget.horizontalHeaderItem(4).setForeground(QBrush(QColor(101, 101, 101)))
        self.tableWidget.verticalScrollBar().setStyleSheet("QScrollBar{border-radius:3px;width: 6px;}\n"
                                                             "QScrollBar::handle{background:lightgray;border-radius:3px;}\n"
                                                             "QScrollBar::handle:hover{background:gray;}")
        self.tableWidget.setStyleSheet("QTableWidget::item:hover{background:#5B5B5B;}")
        self.tableWidget.setShowGrid(False)
        self.tableWidget.horizontalHeader().setSectionsClickable(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_top_id.setText(_translate("MainWindow", "Swaggy-Macro          ▼"))
        self.label_minimize.setText(_translate("MainWindow", "一"))
        self.label_close.setText(_translate("MainWindow", "×"))
        self.label_song_name.setText(_translate("MainWindow", "Mood "))
        self.label_song_name_2.setText(_translate("MainWindow", "24kGoldn / iann dior"))
        self.label_progress_left.setText(_translate("MainWindow", "00:00"))
        self.label_progress_right.setText(_translate("MainWindow", "00:00"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "音乐标题"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "歌手"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "专辑"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "时长"))

    def search_song_lineedit(self):
        keyword = self.lineEdit.text()
        res = apis.cloudsearch.GetSearchResult(keyword)
        for (idx, details) in enumerate (res['result']['songs']):
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            itemSongName = QTableWidgetItem(details['name'])
            itemSingerName = []
            for singerName in details['ar']:
                itemSingerName.append(singerName['name'])
            itemSingerName = QTableWidgetItem(str('/'.join(itemSingerName)))
            itemAlbum = QTableWidgetItem(details['al']['name'])
            itemDt = (float(details['dt']) / 1000)/60
            secs = str(int(math.modf(itemDt)[0]*60))
            if (len(secs)<2):
                secs = "0" + secs
            itemDt = str(int(itemDt)) + ':' + secs
            itemDt = QTableWidgetItem(itemDt)
            idx = str(idx+1)
            if (len(idx)<2):
                idx = "0" + idx
            itemIdx = QTableWidgetItem(idx)
            self.tableWidget.setItem(row, 0, itemIdx)
            self.tableWidget.setItem(row, 1, itemSongName)
            self.tableWidget.setItem(row, 2, itemSingerName)
            self.tableWidget.setItem(row, 3, itemAlbum)
            self.tableWidget.setItem(row, 4, itemDt)
            self.tableWidget.item(row, 0).setForeground(QBrush(QColor(217, 195, 211)))
            self.tableWidget.item(row, 1).setForeground(QBrush(QColor(101, 101, 121)))
            self.tableWidget.item(row, 2).setForeground(QBrush(QColor(101, 101, 101)))
            self.tableWidget.item(row, 3).setForeground(QBrush(QColor(101, 101, 101)))
            self.tableWidget.item(row, 4).setForeground(QBrush(QColor(101, 101, 101)))






import test_rc
if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    # ui.pushButton.clicked.connect(test)
    icon = QtGui.QIcon("./images/icon.ico")
    ui.show()
    sys.exit(app.exec_())