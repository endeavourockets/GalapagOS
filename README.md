# GalapagOS
[![Build](https://github.com/endeavourockets/GalapagOS/workflows/Build/badge.svg)](https://github.com/endeavourockets/GalapagOS/actions?query=workflow%3A%22Build%22)
[![Lint](https://github.com/endeavourockets/GalapagOS/workflows/Lint/badge.svg)](https://github.com/endeavourockets/GalapagOS/actions?query=workflow%3A%22Lint%22)
[![Heroku](https://pyheroku-badge.herokuapp.com/?app=galapag-os)](https://galapag-os.herokuapp.com)

**G**round-support **O**perations **S**ystem for Endeavour's Darwin Rocket.

![the galapagos islands](./island.svg)

## Server

### Requirements

  - python ^3.7
  - poetry ^0.12.13

### Commands

````
# install
poetry install

# lint
poetry run flake8

# test
poetry run pytest

# run development server
cd src && poetry run python main.py
````

### Production Server

````
cd src && poetry run gunicorn main:server
````
