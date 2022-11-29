import multiprocessing

class MessageBusProcess(multiprocessing.Process):
    # This process exists to allow classes to be serialized.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _prepare(self):
        # This conversion is necessary because the process cannot be serialized.
        self._config['authkey'] = bytes(self._config['authkey'])

    def start(self):
        self._prepare()
        return super().start()
