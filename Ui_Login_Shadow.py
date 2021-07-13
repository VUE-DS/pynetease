

import math

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QGraphicsDropShadowEffect
from Ui_Login import Ui_Dialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from NetEase import apis


class LoginWindow(QDialog, Ui_Dialog):

    def __init__(self, *args, **kwargs):
        super(LoginWindow, self).__init__(*args, **kwargs)
        self.mPos = None
        self.setupUi(self)
#        self.closeButton.clicked.connect(self.close)
        # 重点
        # 无边框
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        # 背景透明（就是ui中黑色背景的那个控件）
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(15)
        effect.setOffset(0, 0)
        effect.setColor(Qt.black)
        self.setGraphicsEffect(effect)

    # 加上简单的移动功能

    def mousePressEvent(self, event):
        """鼠标点击事件"""
        if event.button() == Qt.LeftButton:
            self.mPos = event.pos()
        event.accept()

    def mouseReleaseEvent(self, event):
        '''鼠标弹起事件'''
        self.mPos = None
        event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.mPos:
            self.move(self.mapToGlobal(event.pos() - self.mPos))
        event.accept()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = LoginWindow()
    w.show()
    sys.exit(app.exec_())
