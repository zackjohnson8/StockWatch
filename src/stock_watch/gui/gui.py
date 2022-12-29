import multiprocessing
from .view_controllers.main_window_controller import MainWindowController

class GUI(object):
    def __init__(self):
        self.main_view_controller = None

    def start(self, conn):
        # Start the main window
        self.main_view_controller = MainWindowController()
        main_window_parent_conn, main_window_child_conn = multiprocessing.Pipe(duplex=True)
        process = multiprocessing.Process(target=self.main_view_controller.start, args=(main_window_child_conn,))
        process.start()

        # Listen for messages from the main window and message bus
        while True:
            if conn.poll():
                message = conn.recv()
                # TODO: Handle messages. Currently only have a single window
                main_window_parent_conn.send(message)

            if main_window_parent_conn.poll():
                message = main_window_parent_conn.recv()
                # TODO: Handle messages from the main window controller
                pass