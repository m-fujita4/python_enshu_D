import sys
args = sys.argv
text = str(args[1])
num = int(args[2])
word = text.split(" ")
print(word[num-1], end="")