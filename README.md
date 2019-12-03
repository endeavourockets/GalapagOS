# GalapagOS
![https://github.com/endeavourockets/GalapagOS/actions?query=workflow%3A%22Python+Application%22](https://github.com/endeavourockets/GalapagOS/workflows/Python%20Application/badge.svg)

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

# serve
poetry run gunicorn src.app:server
````
