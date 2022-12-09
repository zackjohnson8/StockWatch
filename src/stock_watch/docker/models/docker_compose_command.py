from typing import Optional, List, Dict, Any
from .docker_compose_command_option import DockerComposeCommandOption


class DockerComposeCommand:
    def __init__(self,
                 command: DockerComposeCommandOption,
                 files: Optional[List[str]] = None,
                 profiles: Optional[List[str]] = None,
                 parent_options: Optional[Dict[str, Any]] = None,
                 child_options: Optional[Dict[str, Any]] = None,
                 *args):
        """
        :param files: A list of docker compose files to use.
        :param profile: A list of profiles to use.
        :param parent_options: A dictionary of parent options to use. Example: docker compose {parent_options} {command}
        :param child_options: A dictionary of child options to use. Example: docker compose {command}
        {child_options}
        :param command: The docker compose command to use. Example: docker compose {parent_options} {command}
        {child_options}
        :param args: A list of arguments to use.
        """
        self.files = files
        self.profiles = profiles
        self.parent_options = parent_options
        self.child_options = child_options
        self.command = command
        self.args = args

    def __name__(self):
        return self.__class__.__name__

    def cli_format(self):
        """
        :return: A string of the docker compose command in the format of: docker-compose {files} {profiles}
        {parent_options} {command} {child_options} {args}
        """
        return f'docker-compose {self._format_files()} {self._format_profiles()} {self._format_parent_options()} ' \
               f'{self.command.value} {self._format_child_options()} {self._format_args()}'

    def _format_files(self):
        files_string = ''
        if self.files:
            for file in self.files:
                files_string += f'-f {file} '
            files_string = files_string[:-1]
        return files_string

    def _format_profiles(self):
        profile_string = ''
        if self.profiles:
            for profile in self.profiles:
                profile_string += f'--profile {profile} '
            profile_string = profile_string[:-1]
        return profile_string

    def _format_parent_options(self):
        option_string = ''
        if self.parent_options:
            for option in self.parent_options:
                if self.parent_options[option]:
                    option_string += f'{option} {self.parent_options[option]} '
                else:
                    option_string += f'{option} '
            option_string = option_string[:-1]
        return option_string

    def _format_child_options(self):
        option_string = ''
        if self.child_options:
            for option in self.child_options:
                if self.child_options[option]:
                    option_string += f'{option} {self.child_options[option]} '
                else:
                    option_string += f'{option} '
            option_string = option_string[:-1]
        return option_string

    def _format_args(self):
        args_string = ''
        if self.args:
            for arg in self.args:
                args_string += f'{arg} '
            args_string = args_string[:-1]
        return args_string
