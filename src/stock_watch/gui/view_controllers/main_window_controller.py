import multiprocessing
import sys
from src.stock_watch.gui.extends.application import Application
from src.stock_watch.gui.extends.main_window import MainWindow

class MainWindowController(object):
    def __init__(self):
        self.app = None
        self.main_window = None

    def run_window(self):
        self.app = Application(sys.argv)
        self.main_window = MainWindow()
        self.app.exec()

    def start(self, conn):

        process = multiprocessing.Process(target=self.run_window)
        process.start()

        while True:
            if conn.poll():
                message = conn.recv()
                pass