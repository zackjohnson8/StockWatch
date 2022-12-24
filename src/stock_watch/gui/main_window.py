from PyQt6.QtCore import Qt
from screeninfo import get_monitors
from PyQt6.QtWidgets import QMainWindow, QDockWidget, QWidget

from src.stock_watch.gui.extends.menu_bar import MenuBar
from src.stock_watch.gui.views.news_view import NewsView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setup_window_geometry()
        self.setWindowTitle("Stock Watch")
        self.setMenuBar(MenuBar(self))

        # Add placeholder widget
        docker_widget = QDockWidget("Placeholder Test Widget", self)
        docker_widget.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)
        docker_widget.setWidget(QWidget(self))
        self.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, docker_widget)

        # Add news widget
        self.news_widget = NewsView(self)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.news_widget)

        self.show()

    def setup_window_geometry(self):
        # Get the primary monitor
        monitor = get_monitors()[0]
        # Set the geometry of the window to the monitor's center
        self.setGeometry(int(monitor.width/4), int(monitor.height/4), int(monitor.width/2), int(monitor.height/2))