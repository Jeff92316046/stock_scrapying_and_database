import scrapying
import data_sort
import draw
from PyQt5 import QtWidgets, QtGui, QtCore

from UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.pushButton_2.clicked.connect(self.buttonClicked_scrapying)
        self.ui.pushButton.clicked.connect(self.buttonClicked_draw)

    def buttonClicked_scrapying(self):
        stock_code = self.ui.lineEdit_1.text()
        scrapying.scrapying_1(stock_code)
        data_sort.sort_data()

        
    def buttonClicked_draw(self):
        up_people = self.ui.lineEdit_2.text()
        down_people = self.ui.lineEdit_3.text()
        draw.set_up_down(down_people,up_people)
        draw.draw_pic()
        draw.clean_data()



