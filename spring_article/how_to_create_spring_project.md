
## プロジェクトの作成方法 (Intellij)
 spring initializer からプロジェクトを作成する  
 https://start.spring.io/

 (有償版限定) Intellij のプロジェクト作成時にSpring initializer を選択してプロジェクトを作成する

### 各種アノテーションについて
#### @SpringBootApplication
Spring Application のエントリポイントとなるクラス  
main メソッドを定義する

#### @Component
Spring Application の実行時に自動で読み込まれるクラス  
@SpringBootApplication を付与したクラス、または @ComponentScan を付与したクラスによって読み込まれる  
前者ではサブディレクトリが読み込まれ、後者においては @ComponentScan(basePackages = "package name") で指定したパッケージに含まれる Component が読み込まれる  
