from PyQt6.QtWidgets import QMenu


class ViewMenu(QMenu):
    def __init__(self, parent):
        super().__init__("&View", parent)

        self.stock_list_action = self.addAction("Stock &List")
        # self.stock_list_action.triggered.connect(self.stock_list)
