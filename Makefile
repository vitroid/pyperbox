.PHONY: install build test clean publish test-publish help

# デフォルトターゲット
help:
	@echo "利用可能なコマンド:"
	@echo "  install      - 開発環境をセットアップ"
	@echo "  build        - パッケージをビルド"
	@echo "  test         - テストを実行"
	@echo "  clean        - ビルドファイルをクリーンアップ"
	@echo "  publish      - PyPIにパッケージを公開"
	@echo "  test-publish - TestPyPIにパッケージを公開"

# 開発環境のセットアップ
install:
	@echo "仮想環境をアクティベート中..."
	@source .venv/bin/activate && \
	poetry install

# パッケージのビルド
build:
	@echo "パッケージをビルド中..."
	@source .venv/bin/activate && \
	poetry build

# テストの実行
test:
	@echo "テストを実行中..."
	@source .venv/bin/activate && \
	python -m pytest

# ビルドファイルのクリーンアップ
clean:
	@echo "ビルドファイルをクリーンアップ中..."
	@rm -rf dist/
	@rm -rf build/
	@rm -rf *.egg-info/

# PyPIへの公開
publish:
	@echo "PyPIにパッケージを公開中..."
	@source .venv/bin/activate && \
	poetry publish

# TestPyPIへの公開
test-publish:
	@echo "TestPyPIにパッケージを公開中..."
	@source .venv/bin/activate && \
	poetry publish --repository testpypi

# バージョンアップ（第三階層を1増やす）
bump-patch:
	@echo "パッチバージョンをアップ中..."
	@source .venv/bin/activate && \
	poetry version patch

# マイナーバージョンアップ
bump-minor:
	@echo "マイナーバージョンをアップ中..."
	@source .venv/bin/activate && \
	poetry version minor

# メジャーバージョンアップ
bump-major:
	@echo "メジャーバージョンをアップ中..."
	@source .venv/bin/activate && \
	poetry version major

# 現在のバージョンを表示
version:
	@source .venv/bin/activate && \
	poetry version

# パッチバージョンをアップしてタグを作成
bump-and-tag:
	@echo "パッチバージョンをアップしてタグを作成中..."
	@source .venv/bin/activate && \
	python version_manager.py patch

# 現在のバージョンでタグを作成
create-tag:
	@echo "現在のバージョンでタグを作成中..."
	@source .venv/bin/activate && \
	python version_manager.py tag

# 現在のバージョンを表示
show-version:
	@source .venv/bin/activate && \
	python version_manager.py current
