### about this
 - ビルド・テスト・デプロイ作業を自動化するための CI/CD 基盤
 - リポジトリに対して何らかの操作 (commit, pull request の作成, issue の作成、など) が行われたときに、あらかじめ設定したワークフローを起動できる
 - workflow はリポジトリ内の .github/workflows ディレクトリに YAML ファイルとして定義する必要がある。

#### Glossary
 - Jobs : shell script や action の集まり
 - Actions : スクリプトより複雑なことをしたいときに使用する？
 - runner : workflow を実行するサーバー (Github-hosted or Self-hosted)