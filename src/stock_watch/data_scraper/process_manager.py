from .scraper_process import ScraperProcess


class ProcessManager(object):
    def __init__(self):
        """
        The ProcessManager class is used to manage a list of processes.
        """
        self.processes = []

    def add_process(self, process: ScraperProcess):
        """
        Add a process to the process manager
        :param process: A ScraperProcess object that will be manage by the ProcessManager
        :return:
        """
        self.processes.append(process)

    def start_all_processes(self) -> list:
        """
        Start all the processes in the process manager
        :return:
        """
        connections = []

        for process in self.processes:
            connections.append(process.start())

        return connections

    def stop_all_processes(self):
        """
        Stop all the processes in the process manager
        :return:
        """
        for process in self.processes:
            process.stop()

    def start_process(self, process: ScraperProcess):
        """
        Start a specific process in the process manager
        :param process: The process to be started. If it hasn't been added to the process manager, it will be added so
        that it can be managed.
        :return:
        """
        if process not in self.processes:
            self.processes.append(process)
        process.start()
