from service.kafka.kafka_consumer import run_kafka_consumer
from service.api import routes
from threading import Thread

from service.utils.logs import setup_logging

if __name__ == "__main__":
    
    # setup loggin
    setup_logging("logs/logs.txt", "root")

    # start api on different thread
    api_thread = Thread(target=routes.start_api)
    api_thread.daemon = True
    api_thread.start()

    # start service on main thread
    run_kafka_consumer()