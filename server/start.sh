#!/bin/bash

# カレントディレクトリをスクリプトのあるディレクトリに変更
cd `dirname $0`

exec pipenv run start

# バックグラウンドプロセスのプロセスIDを表示
echo $!
