
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from Ui_MainWindow_Shadow import MainWindow
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    mainWindow.create_tray(app)
    sys.exit(app.exec_())