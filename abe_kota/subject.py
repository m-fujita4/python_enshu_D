import sys
args = sys.argv

math=int(args[1])
jap=int(args[2])
eng=int(args[3])

sum=math+jap+eng

if (math>=70 and jap>=70 and eng>=70) or (sum>=220) and math>50 and jap>50 and eng>50  :
    print("合格")


#elif math>=50 and jap>=50 and eng>=50:
 #   print("合格")


else:
    print("不合格")
    