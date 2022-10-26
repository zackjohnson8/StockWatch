from src.stock_watch.stockbroker.docker.models.types import docker_compose_command_type


class DockerComposeCommandModel:
    def __init__(self,
                 child_command: docker_compose_command_type.DockerComposeCommandType,
                 child_command_options: list[str] = None,
                 child_input_command_options: dict[str, str] = None,
                 parent_options: list[str] = None,
                 parent_input_options: dict[str, str] = None,
                 ):
        """
        :param DockerComposeCommandType child_command: The enum value of the child command. (ex. up, down, create)
        :param list[str] child_command_options: The options for the child command. (ex. -d, --build, --force-recreate)
        :param dict[str, str] child_input_command_options: The input options for the child command. (ex.
            --project-directory, --file)
        :param list[str] parent_options: A list of non-input based options. Any value not included will be ignored
            Example: ['--help', '--verbose', '--version']
        :param dict[str, str] parent_input_options: A dictionary of input based options. Any dictionary value not
            included or given a value of None will be ignored.
            Example: {'--ansi': None, '--compatibility': None, '--env-file': None,
            '--file': None, '--profile': None, '--project-directory': './docker_directory/project_directory',
            '--project-name': None}
        """
        self.child_command = child_command
        self.child_command_options = child_command_options
        self.child_input_command_options = child_input_command_options
        self.parent_options = parent_options
        self.parent_input_options = parent_input_options
