### about this
 - ビルド・テスト・デプロイ作業を自動化するための CI/CD 基盤
 - リポジトリに対して何らかの操作 (commit, pull request の作成, issue の作成、など) が行われたときに、あらかじめ設定したワークフローを起動できる
 - workflow はリポジトリ内の .github/workflows ディレクトリに YAML ファイルとして定義する必要がある。

#### example workflow
 - In this chapter, I will create a basic workflow which is triggered with push event.
 - https://github.com/3104yoshi/cicd_sample

 - 補足
    - uses: actions/checkout@v4 : This is necessary for runner to access the repository



#### Glossary
 - Jobs : shell script や action の集まり
 - Actions : スクリプトより複雑なことをしたいときに使用する？
 - runner : workflow を実行するサーバー (Github-hosted or Self-hosted)
 - ※当然ではあるが、CI/CD においてはテストを実行するためにビルドするための環境 (build host) を用意する必要がある。 aws codebuild なら ec2, ecr, lambda などを利用する。

#### reference
 - https://docs.github.com/en/actions/about-github-actions/understanding-github-actions