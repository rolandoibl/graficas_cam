from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
import sys
from d_spline_widget import Ui_FormSpline
import numpy as np
from scipy import interpolate

class FormSpline(QWidget, Ui_FormSpline):
    def __init__(self):
        QWidget.__init__(self)
        Ui_FormSpline.__init__(self)
        self.setupUi(self)
        self.graphWidget.setBackground('w')
        self.graphWidget.setMenuEnabled(False)
        # Evento que genera conecta con la función de calcular
        self.btn_graficar.clicked.connect(self.calcular)

    def calcular(self):
        # Leer valores de entrada
        p1 = list(map(float, self.ledt_p1.text().split(',')))
        p2 = list(map(float, self.ledt_p2.text().split(',')))
        p3 = list(map(float, self.ledt_p3.text().split(',')))
        p4 = list(map(float, self.ledt_p4.text().split(',')))
        lamb = float(self.ledt_line_lamb.text())

        # Manejo de excepciones
        if lamb > 1 or lamb < 0 or lamb < 0.00001:
            # Ventana que indica ingresar un nuevo valor de lambda
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Parece que hubo un error, vuelve a intentar con otros valores.")
            m = msg.exec_()
        else:
            # Cálculo de la línea
            nodes = np.array([p1, p2, p3, p4])
            linea = self.spline(nodes, lamb)
            # Limpiar área de graficación
            self.graphWidget.clear()
            # Llamar a función de graficación
            self.plot(linea['x'], linea['y'])

    def plot(self, x, y):
        # Color y tamaño de letras en la gráficas
        styles = {'color': '000000', 'font-size': '14px'}
        # Poner nombres de los ejes y dar formato
        self.graphWidget.setLabel('left', 'y', **styles)
        self.graphWidget.setLabel('bottom', 'x', **styles)
        self.graphWidget.setBackground('w')
        self.graphWidget.setXRange(x.min() - 1, x.max() + 1)
        self.graphWidget.setYRange(y.min() - 1, y.max() + 1)
        self.graphWidget.setMenuEnabled(False)
        # Función que grafica los puntos
        self.graphWidget.plot(x, y, symbol='o', pen=None)

    def spline(self, nodes, lamb):
        linea = {}
        x = nodes[:, 0]
        y = nodes[:, 1]
        tck, u = interpolate.splprep([x, y], s=0)
        xnew, ynew = interpolate.splev(np.arange(0, 1, lamb), tck, der=0)
        linea['x'] = xnew
        linea['y'] = ynew
        return linea


if __name__ == '__main__':
    app = QApplication([])
    application = FormSpline()
    application.show()
    app.exec()