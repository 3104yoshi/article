
## プロジェクトの作成方法 (Intellij)
 spring initializer からプロジェクトを作成する  
 https://start.spring.io/

 Add Dependencies から必要な依存関係をあらかじめ追加できる
 →ビルドツールの設定ファイルに依存関係が追加される (build.gradle)

 (有償版限定) Intellij のプロジェクト作成時にSpring initializer を選択してプロジェクトを作成する

### 各種アノテーションについて
#### @SpringBootApplication
Spring Application のエントリポイントとなるクラス  
main メソッドを定義する

#### @Component
Spring Application の実行時に自動で読み込まれるクラス  
@SpringBootApplication を付与したクラス、または @ComponentScan で指定したクラスによって読み込まれる  
前者ではサブディレクトリが読み込まれ、後者においては @ComponentScan(basePackages = "package name") で指定したパッケージに含まれる Component が読み込まれる  

![Alt text](image.png)  
DemoApplication クラスに @SpringBootApplication を付与し、かつ上記の構成を考える  
この場合、デフォルトでは CommonProcess クラスのみ読み込まれ、@ComponentScan(basePackages = "com.example.external") とすると ExternalProcess のみ読み込まれる  

#### @Autowired

### Entity
- 
- ※ JavaEE と JakartaEEについて
    - JakartaEE の方が新しい (javax.persistence -> jakarta.persistence など)

