from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
import sys
from d_line_widget import Ui_LineForm
import numpy as np

class FormLine(QWidget, Ui_LineForm):
    def __init__(self):
        QWidget.__init__(self)
        Ui_LineForm.__init__(self)
        self.setupUi(self)
        self.graphWidget.setBackground('w')
        self.graphWidget.setMenuEnabled(False)
        # Evento que genera conecta con la función de calcular
        self.btn_graficar.clicked.connect(self.calcular)

    def calcular(self):
        # Leer valores de entrada
        x0 = float(self.ledt_line_x0.text())
        y0 = float(self.ledt_line_y0.text())
        x1 = float(self.ledt_line_x1.text())
        y1 = float(self.ledt_line_y1.text())
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
            x = np.arange(x0, x1, lamb)
            y = np.linspace(y0, y1, num=len(x))
            # Limpiar área de graficación
            self.graphWidget.clear()
            # Llamar a función de graficación
            self.plot(x, y)

    def plot(self, x, y):
        # Color y tamaño de letras en la gráficas
        styles = {'color': '000000', 'font-size': '14px'}
        # Poner nombres de los ejes y dar formato
        self.graphWidget.setLabel('left', 'y', **styles)
        self.graphWidget.setLabel('bottom', 'x', **styles)
        self.graphWidget.setBackground('w')
        self.graphWidget.setXRange(0, x[-1])
        self.graphWidget.setYRange(0, y[-1])
        self.graphWidget.setMenuEnabled(False)
        # Función que grafica los puntos
        self.graphWidget.plot(x, y, symbol='o', pen=None)


if __name__ == '__main__':
    app = QApplication([])
    application = FormLine()
    application.show()
    app.exec()