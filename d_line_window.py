# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'line_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 490)
        MainWindow.setMaximumSize(QtCore.QSize(769, 490))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphWidget = PlotWidget(self.centralwidget)
        self.graphWidget.setGeometry(QtCore.QRect(230, 20, 501, 381))
        self.graphWidget.setObjectName("graphWidget")
        self.sbox_x0 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.sbox_x0.setGeometry(QtCore.QRect(30, 50, 81, 22))
        self.sbox_x0.setObjectName("sbox_x0")
        self.sbox_y0 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.sbox_y0.setGeometry(QtCore.QRect(30, 120, 81, 22))
        self.sbox_y0.setObjectName("sbox_y0")
        self.sbox_x1 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.sbox_x1.setGeometry(QtCore.QRect(30, 190, 81, 22))
        self.sbox_x1.setObjectName("sbox_x1")
        self.sbox_y1 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.sbox_y1.setGeometry(QtCore.QRect(30, 260, 81, 22))
        self.sbox_y1.setObjectName("sbox_y1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 230, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 290, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 310, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.btn_graficar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_graficar.setGeometry(QtCore.QRect(60, 350, 101, 51))
        self.btn_graficar.setObjectName("btn_graficar")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(580, 420, 161, 16))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graficación de línea"))
        self.label.setText(_translate("MainWindow", "Posición inicial x"))
        self.label_2.setText(_translate("MainWindow", "Posición inicial y"))
        self.label_3.setText(_translate("MainWindow", "Posición final x"))
        self.label_4.setText(_translate("MainWindow", "Posición final y"))
        self.label_5.setText(_translate("MainWindow", "Lambda"))
        self.btn_graficar.setText(_translate("MainWindow", "Graficar"))
        self.label_6.setText(_translate("MainWindow", "Hecho por Rolando Ibáñez"))
from pyqtgraph import PlotWidget