## What's gradle?
- ビルド自動化ツール

### ビルド方法
- ./gradlew (linux) or .\gradlew.bat (windows) を使用する
- このスクリプトを実行するためには gradle-wrapper.jar が必要 (SpringInitializer でプロジェクトを作成すると既に含まれている) 

### マルチプロジェクト構成  
- 複数のプロジェクトをルートプロジェクトに配置し、まとめてビルドすることもできる  
- setting.gradle に以下のように記載した後、./gradlew compileJava により、記載したサブプロジェクトをまとめてビルドできる  
```groovy
rootProject.name = "root"
include(':sub1')
include(':sub2')
``` 
- ./gradlew :sub1:compileJava により、指定したサブプロジェクトだけをビルドすることもできる  

### build.gradle
Groovy or kotlin で書かれたスクリプトファイル  
このファイルをもとにプロジェクトがビルドされる  
#### dependencies
- 読み込みたいパッケージをここに記述できる  


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