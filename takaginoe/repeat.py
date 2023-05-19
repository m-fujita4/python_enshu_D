import sys

args = sys.argv
# num <= command line argments
num = int(args[1])
tmp = num
while 1:
    if num == 100:
        print("Just 100!", end="")
        break
    if num > 100:
        print("Over!", end="")
        break
    num += tmp