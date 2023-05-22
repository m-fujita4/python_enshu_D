import sys
import introduce
args = sys.argv
input1 = str(args[1])
input2 = int(args[2])

myname = introduce.intro(input1,input2)
print(myname.name_out())
print(myname.age_out())
