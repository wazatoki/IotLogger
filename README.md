# IotLogger

## Overview

The program uses the data received from the IOT client to draw a graph.  
The received data is recorded in a database and can also be downloaded as a CSV file.

## Dependency
* python 3.8.3
* nodejs 14.3.0
* sqlite3

## How to set up

1. install python dependancy module

    cd server dir and execute next commands.

    ```
    $ pipenv install
    ```

1. setup database

    ```
    $ pipenv run upgradeDB
    ```

1. install nodejs dependancy module

    cd client dir and execute next commands.

    ```
    $ nodenv install
    ```

## Usage

start server

in default server listen 8888 port.

If you want change, reference config.ini file and rewrite.

```
pipenv run start
```



## Licence
MIT Licence

## Author
wazatoki

## References
