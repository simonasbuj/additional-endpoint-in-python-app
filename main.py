from service.service import Service
from service.api import routes
from threading import Thread

if __name__ == "__main__":
    
    # start api on different thread
    api_thread = Thread(target=routes.start_api)
    api_thread.daemon = True
    api_thread.start()

    # start service on main thread
    s = Service()
    s.run()