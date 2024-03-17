import logging
from datetime import datetime
from time import sleep


class Service:
    def __init__(self, correlation_id):
        self.name = "Service"
        self.correlation_id = correlation_id

        self.log = self._setup_extra_logging_info()


    def run(self):
        self.log.info(f"Service is running at {datetime.now()} with correlation id {self.correlation_id}")
        sleep(5)
        self.log.info(f"Service finished running")


    def _setup_extra_logging_info(self):
        logger = logging.LoggerAdapter(
            logging.getLogger(f"{self.__class__.__name__} from {__name__}"),
            extra = {
                "correlation_id" : self.correlation_id,
                "username": "dbadmin"
            }
        )
        return logger