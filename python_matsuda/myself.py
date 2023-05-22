import sys
args = sys.argv
import introduce #importで指定するのはファイル名

myself = introduce.Intro(args[1],args[2]) #ファイル名.クラス名で呼び出し
print(myself.name_out())
print(myself.age_out())