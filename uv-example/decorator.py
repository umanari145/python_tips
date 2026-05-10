import random
from retrying import retry


@retry(stop_max_attempt_number=3)
def retry_function():
    print("ここはオリジナルの関数です")
    raise Exception("エラーが発生しました")


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("前処理")
        result = func(*args, **kwargs)
        print("後処理")
        return result
    return wrapper

@my_decorator
def sample_function():
    print("ここはオリジナルの関数です")





if __name__ == "__main__":
    print("-----sample_functionの例----------")
    sample_function()
    retry_function()