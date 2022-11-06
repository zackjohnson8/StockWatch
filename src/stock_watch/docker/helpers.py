import subprocess
import src.stock_watch.logger as logger
from src.stock_watch.docker.models.command_model import CommandModel

logging = logger.get(__name__)


def run_commands(commands: list, wait: bool = True) -> str:
    popen = subprocess.Popen(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             universal_newlines=True)
    if wait:
        popen.wait()
    stdout, stderr = popen.communicate()
    if stderr:
        logging.info(f'{stderr}: stdout: {stdout}')
    else:
        logging.info(stdout)
        return stdout


def create_command(commands: CommandModel) -> list[str]:
    """
    Create the docker compose command
    :param commands:
    """
    command = [commands.cli_type]

    if commands.parent_options:
        command = [*command, *commands.parent_options]

    if commands.parent_input_options:
        for key, value in commands.parent_input_options.items():
            if value:
                command = [*command, key, value]

    command = [*command, commands.child_command.value]

    if commands.child_command_options:
        command = [*command, *commands.child_command_options]

    if commands.child_input_command_options:
        for key, value in commands.child_input_command_options.items():
            if value:
                command = [*command, key, value]

    return command
