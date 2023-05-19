import sys
args = sys.argv
# 引数を変数に代入
math_score = int(args[1])
japanese_score = int(args[2])
english_score = int(args[3])
score = math_score+japanese_score+english_score

if (math_score >= 70 and japanese_score >= 70 and english_score >= 70) or score >= 220:
    
    if math_score >= 50 and japanese_score >= 50 and english_score >= 50:
        print("合格",end="")
    else:
        print("不合格",end="")
else:
    print("不合格",end="")


