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

1. start server

    in default server listen 8888 port.

    If you want change, reference config.ini file and rewrite.

    ```
    pipenv run start
    ```
1. add device definition

    click device マスター link and sen data.

1. add item definitions

    click item マスター link and sen data.

1. select device, from date and to date. next click データ取得 button.

## REST API

### cyclic data

|url|method|format|description|
|----|----|----|----|
|cyclic/add|POST|JSON|{"version": number, "datetime": UTC, "deviceID": string, "item_id_1": number, "item_id_2": number,...}|

item_id_1,item_id_2... are defined item_id

### asynchronous data

|url|method|format|description|
|----|----|----|----|
|asynchronous/add|POST|JSON|{"version": number, "datetime": UTC, "deviceID": string, "code": string, "category": string,  "name": string, "messageType": string}|


## Licence
MIT Licence

## Author
wazatoki

## References
