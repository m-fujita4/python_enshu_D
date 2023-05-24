def check_smaller_than(money, threshold=10000):
    if money > threshold:
        print(f"{threshold:,}円を超える金額は投入できません。" + "再度投入金額を入力してください")
        return False
    else:
        return True


def check_larger_than(money, threshold=100):
    if money < threshold:
        print(f"{money:,}円では購入できる商品がありません。" + "再度投入金額を入力してください")
        return False
    else:
        return True


def check_not_allowed_coins(money, unit=10):
    if money % 10 != 0:
        print("1円玉、5円玉は使用できません。" + "再度投入金額を入力してください")
        return False
    else:
        return True


def calc_change(money):
    dict = {}
    for banknote in [5000, 2000, 1000]:
        num = money // banknote
        if num > 0:
            money = money - banknote * num
            dict[f"{banknote}円札"] = f"{num}枚"
    for coin in [500, 100, 50, 10]:
        num = money // coin
        if num > 0:
            money = money - coin * num
            dict[f"{coin}円玉"] = f"{num}枚"

    return dict


def template_change(money):
    print("おつり")
    change = calc_change(money)
    for key, value in change.items():
        print(key + "：" + value)


def main():
    dict = {
        "お茶": 110,
        "コーヒー": 100,
        "ソーダ": 160,
        "コーンポタージュ": 130
    }

    lowest_price = 10000
    for key in dict.keys():
        if dict[key] < lowest_price:
            lowest_price = dict[key]
    print(lowest_price)
    while True:
        put_money = input(
            "お茶：110円\n" +
            "コーヒー：100円\n" +
            "ソーダ：160円\n" +
            "コーンポタージュ：130円\n" +
            "投入金額を入力してください"
        )
        put_money = int(put_money)

        if check_larger_than(put_money):
            if check_smaller_than(put_money):
                if check_not_allowed_coins(put_money):
                    break

    while True:
        item = input("何を購入しますか (商品名/cancel)")
        if item in dict.keys():
            if dict[item] < put_money:
                remaining_money = put_money - dict[item]
                print(f"残金：{remaining_money}円")

                if remaining_money < lowest_price:
                    template_change(remaining_money)
                    break
                else:
                    one_more_drink = input("続けて購入しますか (Y/N)")
                    if one_more_drink == "Y":
                        continue
                    elif one_more_drink == "N":
                        template_change(remaining_money)
                        break
                    else:
                        print("最初からやり直してください☆")
                        break

            elif dict[item] == put_money:
                break
            else:
                print("お金が足りません。商品を選びなおしてください。")
                continue
        elif item == "cancel":
            template_change(put_money)
            break
        else:
            print("最初からやり直してください☆")
            break


if __name__ == '__main__':
    main()
