from PyQt6.QtWidgets import QApplication

class Application(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
