import multiprocessing
from .view_controllers.main_window_controller import MainWindowController

class GUI(object):
    def __init__(self):
        # Start the main window
        self.main_view_controller = None

    def show(self):
        self.main_view_controller = MainWindowController()
        self.main_view_controller.show()