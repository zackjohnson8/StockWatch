from src.stock_watch.app import StockWatch
import logger
import helpers

def main():
    logger.setup_logging(helpers.find_file('logging_config.yml', './'))
    stock_watch = StockWatch()
    stock_watch.run()


if __name__ == '__main__':
    main()
