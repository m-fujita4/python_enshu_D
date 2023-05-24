# drink dict
vend_machine = {
    "お茶":110,
    "コーヒー":100,
    "ソーダ":160,
    "コーンポタージュ":130
}

# money list for calc change
money_list = [5000, 2000, 1000, 500, 100, 50, 10]

money = 0 # 初期値
drink = "" # 初期値
low = min(vend_machine.values()) # lowest price

# input money(pay)
def ask_money():
    money = input("お金を投入してください : ")
    if str.isdigit(money):
        amount_judge(int(money))
        ask_drink(drink, int(money))
    else: # if input text is not digit(1, 2, 3...)
        print("error : 整数を入力してください")
        ask_money()

# make sure the amount input is correct
def amount_judge(money):
    tmp_money = str(money)
    if money > 10000:
        print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
        ask_money()
    elif money < low:
        print(str(money) + "円では購入できる商品がありません。再度投入金額を入力してください")
        ask_money()
    elif tmp_money[-1] != "0":
        print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
        ask_money()

# drink input
def ask_drink(drink, money):  
    drink = input("何を購入しますか（商品名/cancel) :")
    if drink == "cancel":
        calc_change(money)
        return
    elif drink in vend_machine:
        if money >= vend_machine[drink]:
            calc(drink, int(money))
        else:
            print("error：買えません")
            ask_drink(drink, money)
    else:
        print("error：商品名を入力してください")
        ask_drink(drink, money)

# money - cost
def calc(drink, money):
    cost = vend_machine[drink]
    money = money - cost
    if money >= low:
        print("残金：" + str(money) + "円")
        again = input("続けて購入しますか？（Y/N）:")
        if again == "Y": # もう一回購入するとき
            ask_drink(drink,money)
        elif again == "N": # もう購入しない
            calc_change(money)
    elif money < low:
        calc_change(money)
    elif money == 0:
        return

# calc num of change
def calc_change(change):
    print("おつり")
    if change == 0:
        print("0円")
    for money in money_list:
        change_money = change // money
        change = change % money
        if change_money:
            print('{}円：{}枚'.format(money, change_money))

if __name__=='__main__':
    print(vend_machine) 
    ask_money()