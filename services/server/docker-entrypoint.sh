#!/bin/sh

# derived from cmd in docker-compose


if [ $WEBSOCKET_ENV = "dev" ]
then
    # TODO: make this work
    watchmedo auto-restart --pattern "/usr/local/src/app/*.py" --recursive --signal SIGTERM python3 /usr/local/src/app/app.py
elif [ $WEBSOCKET_ENV = "prod" ]
then
    python3 /usr/local/src/app/app.py
fi
    
