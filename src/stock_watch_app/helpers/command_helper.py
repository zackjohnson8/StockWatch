import subprocess
from src.stock_watch_app.utils import logger

logging = logger.get_logger(__name__)


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
