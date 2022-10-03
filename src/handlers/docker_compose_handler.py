from src.helpers import command_helper


class DockerComposeHandler:
    def __init__(self):
        pass

    def up(self, parent_commands: list = None, options: list = None, services: list = None):
        if parent_commands is None:
            parent_commands = []
        if options is None:
            options = []
        if services is None:
            services = []
        command_list = ['docker-compose', *parent_commands, 'up', *options, *services]
        command_helper.run_commands(command_list)

    def build(self, parent_commands: list = None, options: list = None, services: list = None):
        if parent_commands is None:
            parent_commands = []
        if options is None:
            options = []
        if services is None:
            services = []
        command_list = ['docker-compose', *parent_commands, 'build', *options, *services]
        command_helper.run_commands(command_list)

    def create(self, parent_commands: list = None, options: list = None, services: list = None):
        if parent_commands is None:
            parent_commands = []
        if options is None:
            options = []
        if services is None:
            services = []
        command_list = ['docker-compose', *parent_commands, 'create', *options, *services]
        command_helper.run_commands(command_list)

    def push(self, parent_commands: list = None, options: list = None, services: list = None):
        if parent_commands is None:
            parent_commands = []
        if options is None:
            options = []
        if services is None:
            services = []
        command_list = ['docker-compose', *parent_commands, 'push', *options, *services]
        command_helper.run_commands(command_list)

    def start(self, parent_commands: list = None, services: list = None):
        if parent_commands is None:
            parent_commands = []
        if services is None:
            services = []
        command_list = ['docker-compose', *parent_commands, 'start', *services]
        command_helper.run_commands(command_list)
