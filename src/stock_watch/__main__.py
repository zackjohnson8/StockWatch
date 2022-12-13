from multiprocessing import freeze_support

from src.stock_watch.app import StockWatch
from . import helpers
from . import logger


def main():
    stock_watch = StockWatch()
    stock_watch.run()


if __name__ == '__main__':
    freeze_support()
    main()
