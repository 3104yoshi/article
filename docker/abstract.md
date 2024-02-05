# docker-compose.yml を用いた docker コンテナの作成例

 - 作成時の要点をまとめたのでメモ

## docker-compose.yml のサンプル

url : https://github.com/3104yoshi/docker_sample/tree/main

- ./setup.sh でコンテナを起動できる

### サンプル概要
 - DB と連携する webアプリケーション
 - DB、アプリケーションサーバともに、 docker コンテナ内で作成している
 - DB には postgres と Adminer を, アプリケーション側では Flask を使用しており、以下が必要
     - postgres
     - Adminer
     - python
     - Flask
 - docker によって ↑ を管理できるため、ホストマシンにインストールする必要がない

### ディレクトリ構成
```
root
 ├ src
 |  :
 ├ docker-compose
 ├ Dockerfile
 ├ .env                      # db の接続情報を分離
 └ postgres
    └ init
       ├ 1_create_table.sql  # テーブルの作成
       └ 2_insert.sql        # テーブルデータの初期化
```

### docker-compose.yml
``` yml:docker-compose.yml
version: '3'
services:
  postgres:
    image: postgres:14.4-alpine
    ports:
      - "5432:5432"
    volumes:
      - ./postgres/init:/docker-entrypoint-initdb.d
    container_name: postgres
    environment:
      POSTGRES_USER: $POSTGRES_USER
      POSTGRES_PASSWORD: "$POSTGRES_PASSWORD"
      POSTGRES_DB: "$POSTGRES_DB"
      
  
  server:
    build: .
    ports:
      - '4000:80'
    environment:
      POSTGRES_USER: $POSTGRES_USER
      POSTGRES_PASSWORD: "$POSTGRES_PASSWORD"
      POSTGRES_DB: "$POSTGRES_DB"
      POSTGRES_HOST: "$POSTGRES_HOST"
      FLASK_SECRET_KEY: "$FLASK_SECRET_KEY"
  
  adminer:
    container_name: adminer
    hostname: adminer
    image: adminer:4.7.5
    ports:
      - 8080:8080
    depends_on:
      - postgres

 ```
 - services
    - 各コンテナの設定を定義している
 - image
    - Dockerイメージを指定する
 - build
    - Dockerfile のパスを指定する  

 `Docker Hub のようなリポジトリから Docker イメージを取得する場合はimageを、Dockerfile を指定する場合は build を使用する `

 - volumes
    - /docker-entrypoint-initdb.d にローカルのディレクトリをマウントしている
    - マウントしたディレクトリ直下にある sql ファイルが build 時に実行される 
    - 実行順は prefix の数字に従う
 - 環境変数
    - environment 下で用いている環境変数は .env ファイルで定義できる

#### .env
 - ここでは以下の環境変数を定義している
```
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_DB
POSTGRES_HOST
FLASK_SECRET_KEY
```

### コンテナ起動
```
docker compose build
docker-compose up -d
```

### コンテナへの接続
 - ポートやユーザ名は自身が定義したものを使用する

#### dbへの接続
```
psql -h localhost -p 5432 -U postgres -d postgres
```
#### アプリケーションサーバへの接続

```
http://localhost:4000/
```

## docker-compose.yml を使用するメリット
- Dockerfile をビルドしても、一度に 1 つのコンテナしか起動できない
- docker-compose.yml をビルドすると、一度に複数のコンテナを起動できる
- コンテナの情報をまとめて管理できるため、多数のコンテナを使用するアプリケーションにおいて有用
