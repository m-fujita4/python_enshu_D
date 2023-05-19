import sys
args = sys.argv
# 引数を変数に代入
num = int(args[1])
name = args[2]
# リストを作成
animal_list = ["giraffe","tiger","zebra","elephant","lion"]
# リストに追加
animal_list.insert(num,name)
# リストの末尾の値を削除
animal_list.pop()
# 昇順に並べ替え
animal_list.sort()
# 出力
print(animal_list,end="")
