from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDockWidget, QWidget

from src.stock_watch.gui.models.news_data import NewsData


class NewsView(QDockWidget):
    def __init__(self, parent):
        super().__init__("News", parent)
        self.news_data = NewsData()

        # self.setFeatures(QDockWidget.DockWidgetFeatures.AllDockWidgetFeatures)
        self.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)
        # self.setFloating(False)
        self.setWidget(QWidget(self))
