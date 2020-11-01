from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
import sys
from d_parabola_widget import Ui_FormParabola
import numpy as np

class FormParabola(QWidget, Ui_FormParabola):
    def __init__(self):
        QWidget.__init__(self)
        Ui_FormParabola.__init__(self)
        self.setupUi(self)
        self.graphWidget.setBackground('w')
        self.graphWidget.setMenuEnabled(False)
        # Evento que genera conecta con la función de calcular
        self.btn_graficar.clicked.connect(self.calcular)

    def calcular(self):
        # Leer valores de entrada
        xc = float(self.ledt_par_x.text())
        yc = float(self.ledt_par_y.text())
        dist_foc = float(self.ledt_dist_foc.text())
        lamb = float(self.ledt_line_lamb.text())
        r_ver_arriba = self.rbtn_ver_arriba.isChecked()
        r_ver_abajo = self.rbtn_ver_abajo.isChecked()
        r_hor_der = self.rbtn_hor_der.isChecked()
        r_hor_izq = self.rbtn_hor_izq.isChecked()
        rbtn_pos = {'ver_arriba':r_ver_arriba,'ver_abajo':r_ver_abajo,
                    'hor_der':r_hor_der,'hor_izq':r_hor_izq}

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
            parabola = self.parabola(xc, yc, dist_foc, lamb, rbtn_pos)
            # Limpiar área de graficación
            self.graphWidget.clear()
            # Llamar a función de graficación
            self.plot(parabola['x'], parabola['y'])

    def plot(self, x, y):
        # Color y tamaño de letras en la gráficas
        styles = {'color': '000000', 'font-size': '14px'}
        # Poner nombres de los ejes y dar formato
        self.graphWidget.setLabel('left', 'y', **styles)
        self.graphWidget.setLabel('bottom', 'x', **styles)
        self.graphWidget.setBackground('w')
        self.graphWidget.setXRange(min(x), max(x))
        self.graphWidget.setYRange(min(y), max(y))
        self.graphWidget.setMenuEnabled(False)
        # Función que grafica los puntos
        self.graphWidget.plot(x, y, symbol='o', pen=None)

    def parabola(self, xc, yc, dist_foc, lamb, rbtn_pos):
        parabol = {}
        h = xc
        k = yc
        if rbtn_pos['ver_arriba']:
            p = dist_foc
            x = np.arange(-h * 8, h * 10, lamb)
            y = (x ** 2 - 2 * x * h + h ** 2 + 4 * p * k) / (4 * p)
        elif rbtn_pos['ver_abajo']:
            p = -dist_foc
            x = np.arange(-h * 8, h * 10, lamb)
            y = (x ** 2 - 2 * x * h + h ** 2 + 4 * p * k) / (4 * p)
        elif rbtn_pos['hor_der']:
            p = dist_foc
            y = np.arange(-k * 8, k * 10, lamb)
            x = (y ** 2 - 2 * y * k + k ** 2 + 4 * p * h) / (4 * p)
        elif rbtn_pos['hor_izq']:
            p = -dist_foc
            y = np.arange(-k * 8, k * 10, lamb)
            x = (y ** 2 - 2 * y * k + k ** 2 + 4 * p * h) / (4 * p)
        parabol['x'] = x
        parabol['y'] = y
        return parabol


if __name__ == '__main__':
    app = QApplication([])
    application = FormParabola()
    application.show()
    app.exec()