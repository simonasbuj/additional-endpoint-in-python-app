from time import sleep
import random

from service.service import Service

def run_kafka_consumer():
    wait_time = 0
    while True:
        print(f"New Message Received")
        correlation_id = f"correlation-id-wait-time-{wait_time}"

        s = Service(correlation_id=correlation_id)
        s.run()


        wait_time = random.randint(1, 9)
        print(f"waiting for {wait_time} secs")
        sleep(wait_time)
