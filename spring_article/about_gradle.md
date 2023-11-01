## What's gradle?


### build.gradle
Groovy で書かれたスクリプトファイル  
このファイルをもとにプロジェクトがビルドされる  


#### sourceSets
sourceSets にソースディレクトリとリソースの位置が定義されている  
build.gradle 内で以下のように定義できる  

```
sourceSets {
    main {
        java {
            srcDir 'src/main/java'
        }
        resources {
            srcDir 'src/main/resources'
        }
    }

    test {
        java {
            srcDir 'src/test/java'
        }
        resources {
            srcDir 'src/test/resources'
        }
    }
}
```

sourceSets の定義を省略した場合、以下のデフォルトの設定が適用される
main の source : 'src/main/java'
main の resource : 'src/main/resources'
test の source : 'src/test/java'
test の resource : 'src/test/resources'