from dataclasses import asdict, dataclass

@dataclass
class User:
    name: str
    age: int
    address: str

user = User("John", 20, "123 Main St")
print(user)
# dictionary型のようにして扱える
print(asdict(user))

#デコレーターを使わない書き方で実装
#class User:
#    def __init__(self, name: str, age: int, address: str) -> None:
#        self.name = name
#        self.age = age
#        self.address = address
#    def __repr__(self) -> str:
#        return f"User(name={self.name!r}, age={self.age!r}, address={self.address!r})"
#

@dataclass(frozen=True)
class UserFrozen:
    name: str
    age: int
    address: str

user_frozen = UserFrozen("John", 20, "123 Main St")
print(user_frozen)
print(asdict(user_frozen))
# frozen=True なので代入は AttributeError
# user_frozen.name = "Jane"
