import sys
args = sys.argv

#引数を変数に代入
hm_class = args[1]          #値下げ対象の種別
price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 ,
            "みかん":198, 
            "バナナ":150, 
            "ビール":360,
            "日本酒":580, 
            "ラーメン":380, 
            "うどん":128, 
            "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")      #果物類をタプルで定義
alcohol = ("ビール", "日本酒")              #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")  #麺類をタプルで定義

#ここ以降にプログラムを書く
# 果物類が入力された場合
if hm_class =="果物類":
    hinmoku["リンゴ"] = hinmoku["リンゴ"] - price_down
    hinmoku["みかん"] = hinmoku["みかん"] - price_down
    hinmoku["バナナ"] = hinmoku["バナナ"] - price_down
    if hinmoku["リンゴ"] < 1:
        hinmoku["リンゴ"] = 1
    if hinmoku["みかん"] < 1:
        hinmoku["みかん"] = 1
    if hinmoku["バナナ"] < 1:
        hinmoku["バナナ"] = 1
# 酒類が入力された場合
elif hm_class =="酒類":
    hinmoku["ビール"] = hinmoku["ビール"] - price_down
    hinmoku["日本酒"] = hinmoku["日本酒"] - price_down
    if hinmoku["ビール"] < 1:
        hinmoku["ビール"] = 1
    if hinmoku["日本酒"] < 1:
        hinmoku["日本酒"] = 1
# 麺類が入力された場合
else:
    hinmoku["ラーメン"] = hinmoku["ラーメン"] - price_down
    hinmoku["うどん"] = hinmoku["うどん"] - price_down
    hinmoku["パスタ"] = hinmoku["パスタ"] - price_down
    if hinmoku["ラーメン"] < 1:
        hinmoku["ラーメン"] = 1
    if hinmoku["うどん"] < 1:
        hinmoku["うどん"] = 1
    if hinmoku["パスタ"] < 1:
        hinmoku["パスタ"] = 1

print(hinmoku,end="")

