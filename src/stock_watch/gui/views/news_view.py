from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDockWidget, QWidget


class NewsView(QDockWidget):
    def __init__(self, parent):
        super().__init__("News", parent)
        # self.setFeatures(QDockWidget.DockWidgetFeatures.AllDockWidgetFeatures)
        self.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)
        # self.setFloating(False)
        self.setWidget(QWidget(self))
