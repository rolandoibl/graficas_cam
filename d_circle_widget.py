# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'circle_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormCircle(object):
    def setupUi(self, FormCircle):
        FormCircle.setObjectName("FormCircle")
        FormCircle.resize(732, 454)
        self.label = QtWidgets.QLabel(FormCircle)
        self.label.setGeometry(QtCore.QRect(30, 30, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ledt_circle_y = QtWidgets.QLineEdit(FormCircle)
        self.ledt_circle_y.setGeometry(QtCore.QRect(30, 130, 113, 22))
        self.ledt_circle_y.setObjectName("ledt_circle_y")
        self.label_4 = QtWidgets.QLabel(FormCircle)
        self.label_4.setGeometry(QtCore.QRect(30, 240, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.ledt_line_lamb = QtWidgets.QLineEdit(FormCircle)
        self.ledt_line_lamb.setGeometry(QtCore.QRect(30, 270, 113, 22))
        self.ledt_line_lamb.setObjectName("ledt_line_lamb")
        self.ledt_circle_r = QtWidgets.QLineEdit(FormCircle)
        self.ledt_circle_r.setGeometry(QtCore.QRect(30, 200, 113, 22))
        self.ledt_circle_r.setObjectName("ledt_circle_r")
        self.label_3 = QtWidgets.QLabel(FormCircle)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ledt_circle_x = QtWidgets.QLineEdit(FormCircle)
        self.ledt_circle_x.setGeometry(QtCore.QRect(30, 60, 113, 22))
        self.ledt_circle_x.setObjectName("ledt_circle_x")
        self.graphWidget = PlotWidget(FormCircle)
        self.graphWidget.setGeometry(QtCore.QRect(180, 20, 501, 381))
        self.graphWidget.setObjectName("graphWidget")
        self.btn_graficar = QtWidgets.QPushButton(FormCircle)
        self.btn_graficar.setGeometry(QtCore.QRect(40, 360, 101, 51))
        self.btn_graficar.setObjectName("btn_graficar")
        self.label_2 = QtWidgets.QLabel(FormCircle)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(FormCircle)
        QtCore.QMetaObject.connectSlotsByName(FormCircle)

    def retranslateUi(self, FormCircle):
        _translate = QtCore.QCoreApplication.translate
        FormCircle.setWindowTitle(_translate("FormCircle", "Form"))
        self.label.setText(_translate("FormCircle", "Coordenada en x"))
        self.label_4.setText(_translate("FormCircle", "Lambda"))
        self.label_3.setText(_translate("FormCircle", "Radio"))
        self.btn_graficar.setText(_translate("FormCircle", "Graficar"))
        self.label_2.setText(_translate("FormCircle", "Coordenada en y"))
from pyqtgraph import PlotWidget
