import argparse


class ArgumentHandler(argparse.ArgumentParser):
    def __init__(self):
        # These are the arguments that will be parsed from the command line. These arguments will override the
        # configuration file.
        super().__init__()
        self.add_argument('-a', '--access', action='store', help='TD Ameritrade API access token')
        self.add_argument('-r', '--refresh', action='store', required=True, help='TD Ameritrade API refresh token')
        self.add_argument('-c', '--client', action='store', required=True, help='TD Ameritrade API client ID')
        self.add_argument('-u', '--url', action='store', required=True, help='TD Ameritrade API redirect URL')
        self.add_argument('--docker_user', action='store', required=True, help='Docker Hub username')
        self.add_argument('--docker_password', action='store', required=True, help='Docker Hub password')
