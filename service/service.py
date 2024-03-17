from time import sleep
from datetime import datetime
import random


class Service:
    def __init__(self):
        self.name = "Service"

    def run(self):
        while True:
            print(f"im running at {datetime.now()}")

            wait_time = random.randint(1, 5)
            print(f"waiting for {wait_time} secs")
            sleep(wait_time)