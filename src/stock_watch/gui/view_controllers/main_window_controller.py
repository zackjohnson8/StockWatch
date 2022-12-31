import sys
from src.stock_watch.gui.extends.application import Application
from src.stock_watch.gui.extends.main_window import MainWindow


class MainWindowController(object):
    def __init__(self):
        self.app = None
        self.main_window = None

    def show(self):
        self.app = Application(sys.argv)
        self.main_window = MainWindow()
        self.app.exec()
