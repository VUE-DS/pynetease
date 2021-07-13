from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QGraphicsDropShadowEffect
from Ui_UserInfo import Ui_Dialog


class UserInfoWindow(QDialog, Ui_Dialog):

    def __init__(self, *args, **kwargs):
        super(UserInfoWindow, self).__init__(*args, **kwargs)
        self.mPos = None
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        # 重点
        # 无边框
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        # 背景透明（就是ui中黑色背景的那个控件）
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(5)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)



if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = UserInfoWindow()
    w.show()
    sys.exit(app.exec_())
