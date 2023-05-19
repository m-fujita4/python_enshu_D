import sys
args = sys.argv

num = int(args[1])
animal = str(args[2])

animals = [
    "giraffe", "tiger", "zebra", "elephant", "lion"
]

animals.insert(num, animal)
animals.pop()

print(sorted(animals),end="")