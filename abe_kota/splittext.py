import sys
args = sys.argv

num=int(args[2]) #第三引数に何語目か
sen=args[1] #第二引数に英文

sen_list=sen.split()

#print(sen_list)

print(sen_list[num-1])
