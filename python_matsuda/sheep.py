import sys
args = sys.argv
# 引数を変数に代入
n = int(args[1])

# iとnは数値にして表示される
for i in range(1,n):
    print("ひつじが"+str(i)+"匹")
    continue
print("ひつじが"+str(n)+"匹")
