import sys
import introduce
args = sys.argv
input1 = str(args[1])
input2 = int(args[2])
input3 = str(args[3])

myname = introduce.intro(input1,input2)
print(myname.name_out())
print(myname.age_out())

myname_2 = introduce.introfam(input1,input2,input3)
print(myname_2.name_out())
print(myname_2.age_out())
print(myname_2.cat_out())