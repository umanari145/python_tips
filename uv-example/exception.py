def main():
    try:
        num = 10  / '7'
    except ZeroDivisionError as e:
        print(e)
        print("ゼロ除算が発生しました")     
    except TypeError as e:
        print(e)
        print("型エラーが発生しました")
    except Exception as e:
        print(e)
        print("その他のエラーが発生しました")
    else:
        print("エラーが発生しませんでした")
    finally:
        print("処理が完了しました")

if __name__ == "__main__":
    main()
