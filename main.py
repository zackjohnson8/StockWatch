import sys

from handlers.api_handler import ApiHandler
from handlers.arg_handler import ArgumentHandler
from configs.api_config import APIConfig


def main(argv):
    arg_handler = ArgumentHandler()
    args = arg_handler.parse_args(argv)
    api_configs = APIConfig(args.access, args.refresh)
    api_handler = ApiHandler(api_configs)


if __name__ == '__main__':
    main(sys.argv[1:])
