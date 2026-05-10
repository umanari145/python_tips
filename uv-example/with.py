def main():
    # withを使わない場合
    f = None
    try:
        f = open('test.txt', 'w')
        f.write('Hello, World!')
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()

    # withを使った場合
    with open('test2.txt', 'w') as f:
        f.write('Hello, World2!')
    　　# with のブロックを抜けるとき（正常終了でも例外でも）に、close が自動で呼ばれる
　　　  #だから上の try / finally で f.close() していた部分を、with だけで短く書けます。

if __name__ == "__main__":
    main()
