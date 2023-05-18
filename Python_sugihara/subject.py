import sys
args = sys.argv
input1 = int(args[1])
input2 = int(args[2])
input3 = int(args[3])
if(input1>=70) and (input2>=70) and (input3 >= 70):
    print("合格",end="")
elif(input1 < 50) or (input2 < 50) or (input3 < 50):
    print("不合格",end="")
elif(input1+input2+input3 >=220):
    print("合格",end="")
else:
    print("不合格",end="")
    