## docker-compose でのポートフォワードについて
### 概要
 - docker-compose で定義する ports で何が行われているかをまとめた

### 想定読者
 - docker-compose で定義する ports が分からない人

### ポートフォワードとは
 - 特定のポート番号に届けられたメッセージを、特定のIPアドレス、ポート番号に転送する仕組みのこと

### docker-compose の port から、ホスト側とコンテナ側のポートを対応付けることができる (ポートフォワード)
以下は db と adminer (db を管理する GUI) を定義した docker-compose.yaml  
ホストマシン側の 5433 ポート、 8081 ポートをコンテナ側の 5432 ポート、8080 ポートに紐付けている

```docker-compose:docker-compose.yaml
services:
  postgres:
    image: postgres:14.4-alpine
    ports:
      - "5433:5432"
    container_name: postgres

  adminer:
    container_name: adminer
    hostname: adminer
    image: adminer:4.7.5
    ports:
      - 8081:8080
    depends_on:
      - postgres
```

※ 注意点として、コンテナ側のポートは Dockerfile 内で定義されているポートを指定しないとアクセスできない。  
docker-compose では、ポートの紐付けを行っているだけで、コンテナ側でどのポートを listen するかは Dockerfile で定義する

adminer にアクセスする際のイメージとしては以下の通り

 ![Alt text](image.png)


### 何故ポートフォワードが必要なのか？
コンテナとホストマシンが接続するネットワークはそれぞれ異なる  
そのため、ポートフォワードを行わずにホストマシンに対してコンテナ側のポート 8080 を直接指定しても、コンテナにはアクセスできず、ホストマシンの 8080 にアクセスするだけである



### コンテナの起動方法で接続するネットワークが異なる
 - docker run でコンテナを起動するとデフォルトで存在する bridge ネットワークに接続する
 - docker compose up でコンテナ群を起動すると、新たに作成された bridge ネットワークに接続する


