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
        self.drawer = draw.drawer()

    def setup_control(self):
        self.ui.pushButton_2.clicked.connect(self.buttonClicked_scrapying)
        self.ui.pushButton.clicked.connect(self.buttonClicked_draw)

    def buttonClicked_scrapying(self):
        stock_code = self.ui.lineEdit_1.text()
        self.drawer.data1 = data_sort.find_data_people(stock_code)
        self.drawer.data2 = data_sort.find_data_share(stock_code)




    def buttonClicked_draw(self):
        stock_code = self.ui.lineEdit_1.text()
        up_people = self.ui.lineEdit_2.text()
        down_people = self.ui.lineEdit_3.text()
        self.drawer.set_up_down(down_people,up_people,stock_code)




