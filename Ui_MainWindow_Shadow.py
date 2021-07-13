
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QGraphicsDropShadowEffect
from Ui_MainWindow import Ui_Dialog


class MainWindow(QDialog, Ui_Dialog):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
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
            if (self.userInfo_window!=None):
                MainGeometry = self.geometry()
                self.userInfo_window.setGeometry(
                    QtCore.QRect(MainGeometry.left() + 664, MainGeometry.top() + 60, self.userInfo_window.width(),
                                 self.userInfo_window.height()))
        event.accept()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
