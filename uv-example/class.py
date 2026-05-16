class User:
    user_type = None
    
    def __init__(self, name, age, address):
        self.name = name    
        self.age = age
        self.address = address
    
    def self_increment(self):
        self.age += 1

    # このデコレーターをつけると、start_nameを属性のように呼び出せる
    @property
    def start_name(self):
        if len(self.name) > 0:
            return self.name[0]
        else:
            return None

    def __repr__(self):
        return f"User(name={self.name}, age={self.age}, address={self.address})"

    def __eq__(self, other):
        return self.name == other.name

user = User("John", 20, "123 Main St")
# propertyをつけていないと、メソッドのように呼び出さないといけない
#print(user.start_name())
print(user.start_name)
print(user.self_increment())
print(user.age)
# __repr__をいれているとprintのときに自動的に呼ばれる
print(user)

user2 = User("John", 20, "123 Main St")
#__eq__をいれていると==のときに自動的に呼ばれる
print(user == user2)
