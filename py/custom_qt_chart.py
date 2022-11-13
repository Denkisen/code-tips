import pathlib
from PySide6 import QtCore, QtWidgets, QtGui
import pyqtgraph

class QtChart(pyqtgraph.PlotWidget):
  def __init__(self, parent = None):
    super().__init__(parent)
    pass

if __name__ == "__main__":
  class MainWindow(QtWidgets.QWidget):
    def __init__(self):
      super().__init__()
      self.widget1 = QtChart(self)
      mainLayout = QtWidgets.QVBoxLayout()
      mainLayout.addWidget(self.widget1)
      self.setLayout(mainLayout)

  app = QtWidgets.QApplication()
  widget = MainWindow()
  widget.resize(800, 720)
  widget.show()
  app.exec_()