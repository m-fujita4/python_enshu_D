def main():
    while True:
        money = input(
            "お茶：110円\n" +
            "コーヒー：100円\n" +
            "ソーダ：160円\n" +
            "コーンポタージュ：130円\n" +
            "投入金額を入力してください"
        )
        money = int(money)
        if money < 10000:
            if money > 100:
                if money % 10 == 0:
                    break
                else:
                    print("1円玉、5円玉は使用できません。" +
                          "再度投入金額を入力してください")
            else:
                print(f"{money}円では購入できる商品がありません。" +
                      "再度投入金額を入力してください")
        else:
            print("10,000円を超える金額は投入できません。" +
                  "再度投入金額を入力してください")

    # dict = {
    #     "お茶": 110,
    #     "コーヒー": 100,
    #     "ソーダ": 160,
    #     "コーンポタージュ": 130
    # }

    # purchase = input("何を購入しますか (商品名/cance)")
    # if purchase


if __name__ == '__main__':
    main()
