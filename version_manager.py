#!/usr/bin/env python3
"""
バージョン管理スクリプト
"""

import re
import subprocess
import sys
from pathlib import Path


def get_current_version():
    """pyproject.tomlから現在のバージョンを取得"""
    pyproject_path = Path("pyproject.toml")
    if not pyproject_path.exists():
        raise FileNotFoundError("pyproject.tomlが見つかりません")

    content = pyproject_path.read_text()
    match = re.search(r'^version = "([^"]+)"', content, re.MULTILINE)
    if not match:
        raise ValueError("バージョン情報が見つかりません")

    return match.group(1)


def update_version(new_version):
    """pyproject.tomlのバージョンを更新"""
    pyproject_path = Path("pyproject.toml")
    content = pyproject_path.read_text()

    # バージョンを置換
    new_content = re.sub(
        r'^version = "([^"]+)"',
        f'version = "{new_version}"',
        content,
        flags=re.MULTILINE,
    )

    pyproject_path.write_text(new_content)
    print(f"バージョンを {new_version} に更新しました")


def bump_patch_version():
    """パッチバージョンを1増やす"""
    current = get_current_version()
    major, minor, patch = map(int, current.split("."))
    new_version = f"{major}.{minor}.{patch + 1}"
    update_version(new_version)
    return new_version


def create_git_tag(version):
    """Gitタグを作成"""
    tag_name = f"v{version}"

    # タグが既に存在するかチェック
    result = subprocess.run(
        ["git", "tag", "-l", tag_name], capture_output=True, text=True
    )

    if result.stdout.strip():
        print(f"タグ {tag_name} は既に存在します")
        return False

    # タグを作成
    subprocess.run(["git", "tag", "-a", tag_name, "-m", f"Version {version}"])
    print(f"タグ {tag_name} を作成しました")
    return True


def main():
    """メイン処理"""
    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "patch":
            new_version = bump_patch_version()
            create_git_tag(new_version)
        elif command == "current":
            version = get_current_version()
            print(f"現在のバージョン: {version}")
        elif command == "tag":
            version = get_current_version()
            create_git_tag(version)
        else:
            print("使用法: python version_manager.py [patch|current|tag]")
            sys.exit(1)
    else:
        print("使用法: python version_manager.py [patch|current|tag]")
        print("  patch   - パッチバージョンを1増やしてタグを作成")
        print("  current - 現在のバージョンを表示")
        print("  tag     - 現在のバージョンでタグを作成")


if __name__ == "__main__":
    main()
