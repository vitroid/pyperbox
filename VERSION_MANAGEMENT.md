# バージョン管理ガイド

このプロジェクトでは、自動バージョン管理システムが設定されています。

## 自動バージョン管理

### Git Hooks

- **pre-commit**: コミット時に自動的にパッチバージョン（第三階層）を 1 増やします
- **post-commit**: コミット後に自動的に Git タグを作成します

### 使用方法

通常の git 操作を行うだけで、自動的にバージョン管理が行われます：

```bash
git add .
git commit -m "機能を追加"
# → 自動的にバージョンが0.1.0 → 0.1.1に増加
# → 自動的にタグ v0.1.1 が作成される
```

## 手動バージョン管理

### Makefile コマンド

```bash
# 開発環境のセットアップ
make install

# パッケージのビルド
make build

# テストの実行
make test

# PyPIへの公開
make publish

# TestPyPIへの公開
make test-publish

# パッチバージョンをアップしてタグを作成
make bump-and-tag

# 現在のバージョンでタグを作成
make create-tag

# 現在のバージョンを表示
make show-version
```

### バージョン管理スクリプト

```bash
# パッチバージョンを1増やしてタグを作成
python version_manager.py patch

# 現在のバージョンを表示
python version_manager.py current

# 現在のバージョンでタグを作成
python version_manager.py tag
```

## バージョン番号の形式

バージョン番号は `MAJOR.MINOR.PATCH` 形式です：

- **MAJOR**: 互換性のない変更
- **MINOR**: 後方互換性を保った機能追加
- **PATCH**: 後方互換性を保ったバグ修正

## 注意事項

1. Git hooks は自動的にバージョンを管理しますが、手動でバージョンを変更することも可能です
2. タグの作成はローカルでのみ行われ、リモートへのプッシュは手動で行う必要があります
3. バージョン管理スクリプトを使用する際は、仮想環境がアクティブになっていることを確認してください
