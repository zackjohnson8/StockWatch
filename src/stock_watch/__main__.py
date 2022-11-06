from src.stock_watch.app import StockWatch
import src.stock_watch.logger as logger

logging = logger.get(__name__)


def main():
    stock_watch = StockWatch()
    stock_watch.run()


if __name__ == '__main__':
    logging.info('Starting main.py')
    main()
