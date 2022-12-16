import multiprocessing


class MessageBusProcess(multiprocessing.Process):
    # This process exists to allow classes to be serialized.

    def __init__(self, *args, **kwargs):
        """
        Initialize the process.
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)

    def _prepare(self):
        """
        Prepare the process for running.
        :return:
        """
        # This conversion is necessary because the process cannot be serialized.
        self._config['authkey'] = bytes(self._config['authkey'])

    def start(self):
        """
        Start the process.
        :return:
        """
        self._prepare()
        return super().start()
