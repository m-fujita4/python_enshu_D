import sys
args = sys.argv
input1 = int(args[1])
input2 = str(args[2])
animal = ["giraffe", "tiger", "zebra", "elephant", "lion"]
animal.insert(input1,input2)
#del animal[len(animal)-1]
animal.pop()
animal.sort()

print(animal,end="")