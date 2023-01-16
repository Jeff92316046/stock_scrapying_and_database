import controller

if __name__ == '__main__':
    import sys
    app = controller.QtWidgets.QApplication(sys.argv)
    window = controller.MainWindow_controller()
    window.show()
    sys.exit(app.exec_())