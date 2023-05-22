import sys
args = sys.argv

place_1 = str(args[1]) # 場所1
place_2 = str(args[2]) # 場所2

# 停車駅：東京駅からの距離
sinkansen = {
    '東京':0.00,
    '品川':6.78,
    '新横浜':25.54,
    '名古屋':342.02,
    '京都':476.31,
    '新大阪':515.35
}

def printerror ():
    print("のぞみの停車駅を引数に設定してください", end="")

def calc_distance(place_1, place_2):
    dis_1 = sinkansen[place_1] # 距離1
    dis_2 = sinkansen[place_2] # 距離2
    if dis_1 > dis_2:
        ans = dis_1 - dis_2
    else:
        ans = dis_2 - dis_1
    ans = round(ans, 2) # 小数点第二位で四捨五入
    print(ans, end="")

try:
    place_1 in sinkansen
    place_2 in sinkansen
    calc_distance(place_1,place_2)

except:
    printerror()