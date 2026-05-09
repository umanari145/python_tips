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
envファイルの中に一時的な環境がつくられる<br>
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