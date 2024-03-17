# additional-endpoint-in-python-app

Just an example on how python app could have api running alongside another infinite service, for example kafka consumer.
This example is using a secondary thread to launch API.


## Problem
What if we need api to run alongside our main service?
For example we are listening for kafka messages and each message trigger some code. We also need to trigger that code manually sometimes using api.
In this case we need both kafka consumer and API running at the same time.

Another reason for this might be kubernetes liveness checks. In this way we can add a simple "/health" route to any python app.
Because API thread has daemon set as True, it's gonna crash if main app in main thread crashes.


## Logging
Logging is setup in json format, but most imporantly all serive runs have unique correlation id, that you can track.
Even if more than 1 requests trigger service run at the same time, each of them gonna have unique logging.
This is achieved using LoggingAdapter.

## Running example
### Using Docker
    docker build -t additional-endpoint-in-python-app .
    docker run --name additional-endpoint-in-python-app -p 5000:5000 additional-endpoint-in-python-app


### Using python
    pip install poetry
    poetry install
    poetry run python -B main.py

### Available routes are
    http://localhost:5000/health
    http://localhost:5000/run-service

