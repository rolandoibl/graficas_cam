from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtWidgets import QMessageBox, QAction, QActionGroup, QWidget
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from d_graphics_main import Ui_MainWindow
from line_logique import FormLine
from circle_logique import FormCircle
from arc_logique import FormArc
from parabola_logique import FormParabola
from spline_logique import FormSpline

class MainApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)

        # Instancia de widgets
        self.widget_linea = FormLine()
        self.widget_circulo = FormCircle()
        self.widget_arco = FormArc()
        self.widget_parabola = FormParabola()
        self.widget_spline = FormSpline()

        # Agregar widgets al stack
        self.stk_widget.addWidget(self.widget_linea)
        self.stk_widget.addWidget(self.widget_circulo)
        self.stk_widget.addWidget(self.widget_arco)
        self.stk_widget.addWidget(self.widget_parabola)
        self.stk_widget.addWidget(self.widget_spline)

        # Set al primer widget
        self.stk_widget.setCurrentIndex(0)
        self.stk_widget.showFullScreen()


        # Crear botones para toolbar
        self.action_line = QAction(QIcon('img/linea.png'), 'Línea', self,checkable=True)
        self.action_circle = QAction(QIcon('img/circle.png'), 'Círculo', self, checkable=True)
        self.action_arc = QAction(QIcon('img/arc.png'), 'Arco', self, checkable=True)
        self.action_parabola = QAction(QIcon('img/parabola.png'), 'Parábola', self, checkable=True)
        self.action_spline = QAction(QIcon('img/spline.png'), 'Spline', self, checkable=True)

        group = QActionGroup(self)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.setOrientation(Qt.Vertical)
        self.addToolBar(Qt.LeftToolBarArea, self.toolbar)
        for action in (
            self.action_line,
            self.action_circle,
            self.action_arc,
            self.action_parabola,
            self.action_spline
        ):
            widget = QWidget()
            widget.setMaximumSize(30, 30)
            widget.setMinimumSize(30, 30)
            self.toolbar.addWidget(widget)

            self.toolbar.addAction(action)
            group.addAction(action)

        self.toolbar.setMovable(False)
        self.toolbar.toggleViewAction().setEnabled(False)

        self.action_line.triggered.connect(self.crear_linea)
        self.action_circle.triggered.connect(self.crear_circulo)
        self.action_arc.triggered.connect(self.crear_arco)
        self.action_parabola.triggered.connect(self.crear_parabola)
        self.action_spline.triggered.connect(self.crear_spline)

    def crear_linea(self):
        self.stk_widget.setCurrentIndex(0)

    def crear_circulo(self):
        self.stk_widget.setCurrentIndex(1)

    def crear_arco(self):
        self.stk_widget.setCurrentIndex(2)

    def crear_parabola(self):
        self.stk_widget.setCurrentIndex(3)

    def crear_spline(self):
        msg = QMessageBox()
        msg.setWindowTitle("Atención")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Los coordenadas de los puntos deben ir separados por comas. Ejemplo: 2,2")
        m = msg.exec_()
        self.stk_widget.setCurrentIndex(4)

if __name__ == '__main__':
    app = QApplication([])
    application = MainApplication()
    application.show()
    app.exit(app.exec())
