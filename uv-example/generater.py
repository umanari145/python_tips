def number_generator():

    #numbers = []
    #for i in range(10):
    #    numbers.append(i**2)
    #return numbers

    #上のを１行で書こうとするとこうなる
    numbers = [i**2 for i in range(10)]
    return numbers

def even_number_generator():
    # さらにフィルタリングを入れるとこうなる
    even_numbers = [i**2 for i in range(10) if i % 2 == 0]
    return even_numbers

def cross_size_generator():
    drinks = ["coffee", "tea", "water"]
    sizes = ["L", "M", "N"]
    cross_size = [(drink, size) for drink in drinks for size in sizes]
    return cross_size


def generator_expression_example():
    squares = (x * x for x in range(5))
    return squares

def generator_expression_example2():
    for square in generator_expression_example():
        print(square)

def generator_expression_example3():
    evens =(x for x in range(10) if x % 2 == 0)
    return evens

def count_up_to(n):
    i = 1
    while i <= n:
        yield i # 
        i += 1

if __name__ == "__main__":
    print(number_generator())
    print("-----even_number_generatorの例----------")
    print(even_number_generator())
    print("-----cross_size_generatorの例----------")
    print(cross_size_generator())
    print("-----generator_expression_exampleの例----------")
    print(generator_expression_example())#参照先がわかるだけ
    print("-----generator_expression_example2の例----------")
    print(generator_expression_example2())# 実際に展開される
    print("-----generator_expression_example3の例----------")
    print(generator_expression_example3())# 参照先がわかるだけ
    print("-----list(generator_expression_example3())の例----------")
    print(list(generator_expression_example3()))# 実際に展開される
    print("-----count_up_toの例----------")
    for x in count_up_to(3): #yieldを1つずつ展開される
        print(x)