"""クラスに付くデコレータの例。

- @dataclass … 標準ライブラリ。フィールドから __init__ などを生成する。
- @mark_simple … 自作。クラスオブジェクトを受け取り、属性を足して返す。
"""

from dataclasses import dataclass


# --- 標準: クラスデコレータ @dataclass ---
@dataclass
class Person:
    name: str
    age: int = 0


# --- 自作: クラスそのものに @ を付ける例 ---
def mark_simple(cls):
    """定義されたクラス cls に印を付けて、そのまま返す。"""
    cls._marked = True
    return cls


@mark_simple
class Greeter:
    def hello(self) -> str:
        return "hello"


if __name__ == "__main__":
    p = Person("Alice")
    print(p)
    q = Person("Bob", 25)
    print(q.name, q.age)

    g = Greeter()
    print(g.hello())
    print(Greeter._marked)
