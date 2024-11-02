# Zip Code REST Server

[![MIT License](https://shields.io/badge/License-MIT-blue)](https://github.com/ksubpb/zipcode_flask_rest/blob/main/LICENSE)

ローカルファイルで指定された郵便番号（Zip Code）のCSVファイルを元に，REST APIを提供するサーバを作成します．
Python の Flask 学習用に作成したものです．

## Usage

### Run the server

```sh
$ python3 zipcode_rest.py zipcode.csv
Start server on port 5000
```

zipcode.csv は[日本郵政グループの提供する郵便番号データのCSVファイル](https://www.post.japanpost.jp/zipcode/download.html)です．
データのフォーマットは[日本郵政グループのページに記載されています](https://www.post.japanpost.jp/zipcode/dl/utf-readme.html)．

### Docker

```sh
$ docker run -d -p 5000:5000 --rm tamada/zipcode_rest:latest
```

郵便番号データはデフォルトのものを利用します．

### Demo

起動後，郵便番号のデータを検索できます．

![demo](assets/demo.gif)

## API

### GET /zipcode/prefs/{prefecture}

指定された都道府県の郵便番号の一覧をJSONで取得します．
指定された都道府県が見つからない場合は，404 を返す．
都道府県は，兵庫県や，東京都などのように，日本語で指定し，県や府は省略しないでください．

### GET /zipcode/{zipcode}

指定された郵便番号の住所などをJSONで取得します．
郵便番号が見つからない場合は，404 を返し，
見つかった場合は，200 および JSON をレスポンスのボディに入れて返します．

### DELETE /zipcode/{zipcode}

指定された郵便番号のデータを削除します．
このリクエストは常に成功します．
指定された郵便番号が見つかれば，そのデータを削除し，見つからなければ何もしません．

### POST /zipcode/{zipcode}

指定された郵便番号のデータを追加します．
郵便番号のデータは JSON 形式で，HTTP リクエストボディに与えます．
有効なデータは，`GET /zipcode/{zipcode}` で取得できるデータと同じです．

### PUT /zipcode/{zipcode}

指定された郵便番号のデータを更新します．
郵便番号のデータは JSON 形式で，HTTP リクエストボディに与えます．
有効なデータは，`GET /zipcode/{zipcode}` で取得できるデータと同じです．

