import sys
args = sys.argv
import introfamily #importで指定するのはファイル名

family = introfamily.IntroFam(args[1],args[2],args[3]) #ファイル名.クラス名で呼び出し
print(family.name_out())
print(family.age_out())
print(family.cat_out())