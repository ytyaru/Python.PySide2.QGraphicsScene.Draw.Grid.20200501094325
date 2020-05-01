#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PySide2 import QtCore, QtGui, QtWidgets
 
class GraphicView(QtWidgets.QGraphicsView):
    def __init__(self):
        QtWidgets.QGraphicsView.__init__(self)
        self.setWindowTitle("QGraphicsScene draw Grid")
        self.setScene(GridScene())
 
class GridScene(QtWidgets.QGraphicsScene):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.size = 16
        self.scale = 32
        self.setSceneRect(0, 0, self.size*self.scale, self.size*self.scale)
    def drawBackground(self, painter, rect):
        background_brush = QtGui.QBrush( QtGui.QColor(255,255,255), QtCore.Qt.SolidPattern)
        painter.fillRect(rect, background_brush)
        lines = []
        for y in range(self.size+1):
            lines.append(QtCore.QLineF(0, y*self.scale, self.size*self.scale, y*self.scale))
        for x in range(self.size+1):
            lines.append(QtCore.QLineF(x*self.scale, 0, x*self.scale, self.size*self.scale))
        painter.drawLines(lines)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = GraphicView()
    widget.show()
    sys.exit(app.exec_())

