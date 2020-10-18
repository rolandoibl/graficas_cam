from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
import sys
from d_circle_widget import Ui_FormCircle
import numpy as np

class FormCircle(QWidget, Ui_FormCircle):
    def __init__(self):
        QWidget.__init__(self)
        Ui_FormCircle.__init__(self)
        self.setupUi(self)
        self.graphWidget.setBackground('w')
        self.graphWidget.setMenuEnabled(False)
        # Evento que genera conecta con la función de calcular
        self.btn_graficar.clicked.connect(self.calcular)

    def calcular(self):
        # Leer valores de entrada
        xc = float(self.ledt_circle_x.text())
        yc = float(self.ledt_circle_y.text())
        r = float(self.ledt_circle_r.text())
        lamb = float(self.ledt_line_lamb.text())
        # Manejo de excepciones
        if lamb > 1 or lamb < 0 or lamb <= 0.00001:
            # Ventana que indica ingresar un nuevo valor de lambda
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Parece que hubo un error, vuelve a intentar con otros valores.")
            m = msg.exec_()
        else:
            # Cálculo de la línea
            circle = self.circulo(xc, yc, r, lamb)
            # Limpiar área de graficación
            self.graphWidget.clear()
            # Llamar a función de graficación
            self.plot(circle['x'], circle['y'], r, xc, yc)

    def plot(self, x, y, r, xc, yc):
        # Color y tamaño de letras en la gráficas
        styles = {'color': '000000', 'font-size': '14px'}
        # Poner nombres de los ejes y dar formato
        self.graphWidget.setLabel('left', 'y', **styles)
        self.graphWidget.setLabel('bottom', 'x', **styles)
        self.graphWidget.setBackground('w')
        self.graphWidget.setXRange(xc-r, xc+r)
        self.graphWidget.setYRange(yc-r, yc+r)
        self.graphWidget.setMenuEnabled(False)
        # Función que grafica los puntos
        self.graphWidget.plot(x, y, symbol='o', pen=None)

    def circulo(self, xc, yc, r, lamb):
        circulo = {}
        x = []
        y = []
        for i in np.arange(0, 2 * np.pi, lamb):
            x.append(xc + r * np.cos(i))
            y.append(yc + r * np.sin(i))
        circulo['x'] = x
        circulo['y'] = y
        return circulo


if __name__ == '__main__':
    app = QApplication([])
    application = FormCircle()
    application.show()
    app.exec()
