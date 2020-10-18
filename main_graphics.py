from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox
from PyQt5.QtWidgets import QMessageBox, QAction, QActionGroup, QWidget
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from d_graphics_main import Ui_MainWindow
from line_logique import FormLine
from circle_logique import FormCircle


class MainApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)

        # Instancia de widgets
        self.widget_linea = FormLine()
        self.widget_circulo = FormCircle()

        # Agregar widgets al stack
        self.stk_widget.addWidget(self.widget_linea)
        self.stk_widget.addWidget(self.widget_circulo)

        # Set al primer widget
        self.stk_widget.setCurrentIndex(0)
        self.stk_widget.showFullScreen()


        # Crear botones para toolbar
        self.action_line = QAction(QIcon('img/linea.png'), 'Línea', self,checkable=True)
        self.action_circle = QAction(QIcon('img/circle.png'), 'Círculo', self, checkable=True)
        self.action_arc = QAction(QIcon('img/arc.png'), 'Arco', self, checkable=True)
        self.action_parabola = QAction(QIcon('img/parabola.png'), 'Parábola', self, checkable=True)
        self.action_spline = QAction(QIcon('img/spline.png'), 'Arco', self, checkable=True)

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

    def crear_linea(self):
        self.stk_widget.setCurrentIndex(0)

    def crear_circulo(self):
        self.stk_widget.setCurrentIndex(1)

if __name__ == '__main__':
    app = QApplication([])
    application = MainApplication()
    application.show()
    app.exit(app.exec())
