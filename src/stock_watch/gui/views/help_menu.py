import webbrowser

from PyQt6.QtWidgets import QMenu


class HelpMenu(QMenu):
    def __init__(self, parent):
        super().__init__("&Help", parent)

        self.about_stock_watch_action = self.addAction("About Stock Watch")
        self.about_stock_watch_action.triggered.connect(self.about_stock_watch)

    def about_stock_watch(self):
        # Causing error messageInvalid reason code startup for ping background-update and Missing HTTP status
        webbrowser.open("https://github.com/zackjohnson8/StockWatch")

