# import sys
# args = sys.argv
# input1 = int(args[1])
input1 =int(input("入力"))
i= 2
val = input1
result = []
while(True):
    if(val % i ==0):
        val = val / i
        result.append(i)
        i = 2
        if(val ==1):
            break
    elif(val % i != 0):
        i = i + 1
    elif(val == i):
        result.append(i)
        break   
    
print(result)
        
    