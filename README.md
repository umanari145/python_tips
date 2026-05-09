# python_tips

## 基本的なバージョン管理
pip・・・Pythonのパッケージ管理ツール(PHPのcomposerと近い)

```
pip list
```
インストールバージョンのリスト
```
root@7b1250d5fb03:/app# pip list
Package       Version
------------- -------
peppercorn    0.6
pip           26.0.1
sampleproject 4.0.0

```
インストールされているバージョンの管理
```
pip freeze > requirements.txt 
```


複数のpythonの環境をインストールするには・・・(dockerの外から行う)
```
brew install pyenv
pyenv install 3.14.0
# 特定のフォルダのみにインストール
pyenv local 3.14.0
pyenv rehash
さらに、~/.zshrc にこれが必要です（未設定だと command not found になります）。

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init - zsh)"
```
##　仮想環境の構築
``` 
python3.14 -m venv env
```
envディレクトリの中に一時的な環境がつくられる<br>
一時的なライブラリ置き場でPHPのvendorなどに近い
```
source env/bin/activate
(env) **********% 

参照するpythonの場所
which python 
**********/env/bin/python

無効化する
deactivate env/bin/activate

```

## パッケージマネージャーuvについて
<br>

pipと比べると主なメリットはこのあたりです。

- 高速: 依存解決とインストールがかなり速い（体感差が出やすい）
- 1ツールで完結しやすい: pip + venv + 一部 pip-tools の役割をまとめて扱える
- Python本体管理にも対応: 環境によっては pyenv 的な用途も一部カバーできる
- CIが速くなりやすい: 解決・インストール時間短縮でパイプライン全体が軽くなる

プロジェクト作成
```
uv init uv-example
```
仮想環境が作成と有効化(ファイル名は自動的に.venvになる)
```
uv venv
source .venv/bin/activate
```

任意のpythonのインストール<br>
pyenvとuvのバージョンを両方使うと混乱しそう・・・・
```
uv python install 3.12
Installed Python 3.12.11 in 4.81s

 + cpython-3.12.11-macos-x86_64-none (python3.12)
warning: `/Users/*******/.local/bin` is not on your PATH. To use installed Python executables, run `export PATH="/Users/***********/.local/bin:$PATH"` or `uv python update-shell`.

実際にインストールされたpythonを見る方法
sourceで読み込んだ状態でuv python listを見るのが一番良さげ
あとはpython3.XX --versionで実際にみる
```

uvを使ってプロジェクトで管理するpythonを管理
```
uv python install 3.14
#3.14 を使って venv を作り直す
uv venv --python 3.14
#依存追加を再実行
uv add sampleproject

#確認コマンド

uv run python --version
uv run which python
```