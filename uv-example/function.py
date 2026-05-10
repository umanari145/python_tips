def sample_function(a=4, b=5):
    return a + b

def sample_function2(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)


def sample_function3(name,**kwargs):
    print(name)
    for key, value in kwargs.items():
        print(key, value)

if __name__ == "__main__":
    print("-----関数の例----------")
    print(sample_function(a=1, b=2))
    print(sample_function(2, 1))
    print(sample_function())
    print("--------------------------------")

    print("-----関数の例2----------")
    sample_function2(1, 2, 3, 4, 5)
    print("--------------------------------")

    print("-----関数の例3----------")
    sample_function3("John", age=20, city="New York")
    print("--------------------------------")


    print("-----関数の例4----------")
    num = [1, 2, 3, 4, 5]
    print(sum(num, start=10))
    print("--------------------------------")