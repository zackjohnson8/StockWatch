from multiprocessing import freeze_support

from src.stock_watch.app import StockWatch

def main():
    stock_watch = StockWatch()
    stock_watch.run()


if __name__ == '__main__':
    # freeze_support() # Remove this line until future need for freezing for executable creation.
    main()
