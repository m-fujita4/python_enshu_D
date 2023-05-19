import sys
args = sys.argv

num=int(args[1])
name=args[2]


animals=["giraffe","tiger","zebra","elephant","lion"]

animals.insert(num,name)

#animals.pop()
del animals[-1]
animals.sort()

print(animals,end="")