import sys
# command line arguments -> args[]
args = sys.argv

# 3 numbers(integer)
num1 = args[1]
num2 = args[2]
num3 = args[3]

# add numbers
sum = int(num1) + int(num2) + int(num3)

# print sum
print(sum, end="")

