import sys
args = sys.argv

place_1 = str(args[1])
place_2 = str(args[2])

sinkansen = {
    '東京':0.00,
    '品川':6.78,
    '新横浜':25.54,
    '名古屋':342.02,
    '京都':476.31,
    '新大阪':515.35
}

dis_1 = sinkansen[place_1]
dis_2 = sinkansen[place_2]

ans = 0

if dis_1 > dis_2:
    ans = dis_1 - dis_2
else:
    ans = dis_2 - dis_1

ans = round(ans, 2)

print(ans, end="")
