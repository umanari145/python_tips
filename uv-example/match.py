def subject(drink: str):
    match drink:
        case "coffee":
            return "コーヒー"
        case "tea":
            return "紅茶"
        case "water":
            return "水"
        case _:
            return "その他"


def subject2(drink: str):

    match drink:
        case "coffee" | "latte":
            return "コーヒー"
        case "tea" | "green tea":
            return "紅茶"
        case "water" | "ice water":
            return "水"
        case _:
            return "その他の飲み物"


def subject3(drink: str):
    match drink:
        case value:
            return f"あなたは{value}を飲みたいようですね"


def subject4(drink: str):
    match drink:
        case "L" | "M" | "N" as size:
            return f"コーヒーのサイズは{size}です"

import enum    
class OrderType(enum.Enum):
    DRINK = "drink"
    FOOD = "food"

def subject5(item: Size):
    match item:
        case OrderType.DRINK:
            return "飲み物"
        case OrderType.FOOD:
            return "食べ物"

def guard(subject):
    match subject:
        case ("peopele", int(num)) if num <=0:
            return "0人以下の予約はできません"
        case ("peopele", int(num)) if num <= 2:
            return "カウンターでお願いします。"
        case ("peopele", int(num)) if num <= 5:
            return "テーブル席でお願いします。"
        case _:
            return "予約人数が不正です"

if __name__ == "__main__":
    print("-----飲み物のパターンマッチ----------")
    print(subject("coffee"))
    print(subject("tea"))
    print(subject("water"))
    print(subject("other"))
    print("--------------------------------")

    print("-----飲み物のパターンマッチ2----------")
    print(subject2("coffee"))
    print(subject2("latte"))
    print(subject2("tea"))
    print(subject2("green tea"))
    print(subject2("water"))
    print(subject2("ice water"))
    print(subject2("other"))
    print("--------------------------------")

    print("-----飲み物のパターンマッチ3----------")
    print(subject3("coffee"))
    print("--------------------------------")

    print("-----飲み物のパターンマッチ4----------")
    print(subject4("L"))
    print(subject4("M"))
    print(subject4("N"))
    print("--------------------------------")

    print("-----飲み物のパターンマッチ5----------")
    print(subject5(OrderType.DRINK))
    print(subject5(OrderType.FOOD))
    print("--------------------------------")

    print("-----飲み物のパターンマッチ6----------")
    print(guard(("peopele", 0)))   
    print(guard(("peopele", 1)))
    print(guard(("peopele", 2)))
    print(guard(("peopele", 5)))
    print(guard(("peopele", 6)))
    print("--------------------------------")