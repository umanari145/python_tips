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
````
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