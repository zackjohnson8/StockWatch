import argparse


class ArgumentHandler(argparse.ArgumentParser):
    def __init__(self):
        # These are the arguments that will be parsed from the command line. These arguments will override the
        # configuration file.
        super().__init__()
        self.add_argument('-a', '--access', action='store', required=True, help='TD Ameritrade API access token')
        self.add_argument('-r', '--refresh', action='store', required=True, help='TD Ameritrade API refresh token')