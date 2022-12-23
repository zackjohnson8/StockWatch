from screeninfo import get_monitors
from PyQt6.QtWidgets import QMainWindow

from src.stock_watch.gui.views.menu_bar import MenuBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setup_window_geometry()
        self.setWindowTitle("Stock Watch")
        self.setMenuBar(MenuBar(self))
        self.show()

    def setup_window_geometry(self):
        # Get the primary monitor
        monitor = get_monitors()[0]
        # Set the geometry of the window to the monitor's center
        self.setGeometry(int(monitor.width/4), int(monitor.height/4), int(monitor.width/2), int(monitor.height/2))