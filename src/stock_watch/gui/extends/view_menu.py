from PyQt6.QtWidgets import QMenu


class ViewMenu(QMenu):
    def __init__(self, parent):
        super().__init__("&View", parent)

        self.stock_list_action = self.addAction("&News")
        self.stock_list_action.setCheckable(True)
        self.stock_list_action.setChecked(True)
