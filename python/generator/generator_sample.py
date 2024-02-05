def gen(first, last):
    for i in range(first, last):
        yield i

# gene = gen(0, 5)

gene = (i for i in range(0, 5))

for x in gene:
    print(x)

for y in gene:
    print(y)

print(sum(gen(0, 5)))

# generator の定義方法
## generator 関数
# 通常の関数では return で値を返すが、generator では yield で値を返す
# generator は iterator の一種で、for 文で回すことができる

## generator 内包表記
# リスト内包表記の [] を () に変えると generator として定義できる

# generator の特徴
## 一度しか実行できない
## generator はその場で値を作り、値を1つずつ返す。
## そのため、過去に返した値を保持していないので、一度しか実行できない

# generator のメリット
# メモリを節約できる
## 通常のリスト等では、全ての要素をメモリに格納する必要があるが、generator では必要な要素のみをメモリに格納する
## 実行速度は遅くなる場合もあるため、要素数が多い場合のみ使用するべき
