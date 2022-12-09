from urllib3.connectionpool import xrange

import asyncio
import platform
import sys


async def run_shell_command(*args):
    """
    Run a shell command.
    :param args: Command to run
    :return:
    """
    # Create subprocess
    process = await asyncio.create_subprocess_shell(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    # Output Status
    print("Started: %s, pid=%s" % (args, process.pid), flush=True)

    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()
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

    result = stdout.decode().strip()
    return result


def make_chunks(tasks, max_threads):
    """
    Split a list of tasks into chunks of a given size.
    :param tasks: List of tasks
    :param max_threads: Maximum number of threads
    :return:
    """
    if sys.version_info.major == 2:
        for i in xrange(0, len(tasks), max_threads):
            yield tasks[i: i + max_threads]
    else:
        # Assume Python 3
        for i in range(0, len(tasks), max_threads):
            yield tasks[i: i + max_threads]


def run_asyncio_commands(tasks, max_concurrent_tasks=0):
    """
    Run a list of asyncio tasks.
    :param tasks: List of tasks
    :param max_concurrent_tasks: Maximum number of concurrent tasks
    :return:
    """
    all_results = []

    if max_concurrent_tasks == 0:
        chunks = [tasks]
        num_chunks = len(chunks)
    else:
        chunks = make_chunks(tasks=tasks, max_threads=max_concurrent_tasks)
        num_chunks = len(list(make_chunks(tasks=tasks, max_threads=max_concurrent_tasks)))

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
