# write-math-py
Pure Python implementation of the backend of write-math

## Docker

```bash
$ sudo docker run -t -p 8080:5000 --name writemath_api themoosemind/write-math-api
```

where 80 is the target port on the host system and 5000 is the port in the
container.

### Basics

Stop and remove all containers:

```bash
$ docker stop $(docker ps -a -q)
$ docker rm $(docker ps -a -q)
```


## Technology

* Flask
  * Werkzeug routing
  * Jinja2 templating
* MySQL database

## REST API

The payload has to be send as JSON. The server always returns JSON.

* `POST /api/recording`: Submit data of a recording
  - Payload: `{'recording': [[{x: 12, y: 4, t: 0}, ...], ...], 'recording_id': None}`
  - Returns:
      - 200: The recording as it is in the database (inclusive recording_id)
      - 400: `{'error': 'Invalid recording'}`
* `GET /api/classification/<int:recording_id>`
  - Returns:
      - 200: The recording as it is in the database
      - 400: `{'error': 'Invalid recording'}`

### Users

* `POST /api/users`: Create a new user
* `POST /api/users/login`