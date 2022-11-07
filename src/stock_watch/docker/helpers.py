import asyncio
import platform
import subprocess
import sys

from urllib3.connectionpool import xrange

import src.stock_watch.logger as logger
from src.stock_watch.docker.models.command_model import CommandModel

logging = logger.get(__name__)


async def run_command(*args):
    # Create subprocess
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    # Status
    print("Started: %s, pid=%s" % (args, process.pid), flush=True)

    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()

    # Progress
    if process.returncode == 0:
        print(
            "Done: %s, pid=%s, result: %s"
            % (args, process.pid, stdout.decode().strip()),
            flush=True,
        )
    else:
        print(
            "Failed: %s, pid=%s, result: %s"
            % (args, process.pid, stderr.decode().strip()),
            flush=True,
        )

    # Result
    result = stdout.decode().strip()

    # Return stdout
    return result


def make_chunks(l, n):
    if sys.version_info.major == 2:
        for i in xrange(0, len(l), n):
            yield l[i: i + n]
    else:
        # Assume Python 3
        for i in range(0, len(l), n):
            yield l[i: i + n]


def run_asyncio_commands(tasks, max_concurrent_tasks=0):
    all_results = []

    if max_concurrent_tasks == 0:
        chunks = [tasks]
        num_chunks = len(chunks)
    else:
        chunks = make_chunks(l=tasks, n=max_concurrent_tasks)
        num_chunks = len(list(make_chunks(l=tasks, n=max_concurrent_tasks)))

    if asyncio.get_event_loop().is_closed():
        asyncio.set_event_loop(asyncio.new_event_loop())
    if platform.system() == "Windows":
        asyncio.set_event_loop(asyncio.ProactorEventLoop())
    loop = asyncio.get_event_loop()

    chunk = 1
    for tasks_in_chunk in chunks:
        print(
            "Beginning work on chunk %s/%s" % (chunk, num_chunks), flush=True
        )
        commands = asyncio.gather(*tasks_in_chunk)  # Unpack list using *
        results = loop.run_until_complete(commands)
        all_results += results
        print(
            "Completed work on chunk %s/%s" % (chunk, num_chunks), flush=True
        )
        chunk += 1

    loop.close()
    return all_results


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
