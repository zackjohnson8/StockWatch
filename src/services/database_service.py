import os

from src.handlers.docker_compose_handler import DockerComposeHandler
from src.extends import logger
from src.helpers import file_folder_helper

logging = logger.get_logger(__name__)


class DatabaseService:
    def __init__(self, docker_compose_file: str = None, working_dir: str = None):
        self.docker_compose_handler = DockerComposeHandler()
        if docker_compose_file:
            self.docker_compose_file_command = ['-f', docker_compose_file]
        else:
            self.docker_compose_file_command = []
        if working_dir:
            self.working_dir_command = ['--project-directory', working_dir]
        else:
            self.working_dir_command = []

    def create_database(self):
        # Build, (re)create, push
        self.docker_compose_handler.up(
            parent_commands=[*self.docker_compose_file_command, *self.working_dir_command],
            options=['--build', '--no-start', '--force-recreate']
        )

    def start_database(self):
        # Start the database service

        self.docker_compose_handler.up(
            parent_commands=[*self.docker_compose_file_command, *self.working_dir_command],
            options=['-d', '--build', '--force-recreate']
        )

    def stop_database(self):
        # Stop the database service
        self.docker_compose_handler.down(
            parent_commands=[*self.docker_compose_file_command, *self.working_dir_command],
        )

    def add_volume_folders(self):
        if self.docker_compose_file_command:
            database_volume = self.docker_compose_file_command[1]
        file_folder_helper.create_directory(folder_path=database_volume, mode=0o777)
