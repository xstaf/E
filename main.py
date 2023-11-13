import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle('EtoSdelalMurmansk100%')
        self.btn = QPushButton('Нарисовать', self)
        self.btn.move(250, 400)
        self.btn.resize(60, 40)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        a = random.randint(10, 300)
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        yellow = random.randint(0, 255)
        qp.setBrush(QColor(red, green, yellow))
        qp.drawEllipse(random.randint(0, 200), random.randint(0, 200), a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
