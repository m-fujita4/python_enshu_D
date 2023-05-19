import sys
args = sys.argv
input1 = int(args[1])
sum = 0
while(True):
    sum = sum + input1
    if(sum==100):
        print("Just 100!",end="")
        break       
    elif(sum<100):
        pass
    else:
        print("Over!",end="")
        break