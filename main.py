import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QPainter, QColor
import random


def draw(qp):
    qp.setBrush(QColor(255, 247, 0))
    x, y, r = random.randint(10, 452), random.randint(10, 358), random.randint(50, 100)
    qp.drawEllipse(x, y, r, r)


class Example(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.flag = False
        self.button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            draw(qp)
            qp.end()

    def paint(self):
        self.flag = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
