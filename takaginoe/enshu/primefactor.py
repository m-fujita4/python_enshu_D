import sys
args = sys.argv
num = int(args[1])

def primefactor(n):
    ans = []
    tmp = n
    for i in range (2, int(n*0.5//1-1)):
        if tmp % i == 0:
            while tmp % i == 0:
                tmp //= i
                ans.append(i)
    if ans==[]:
        ans.append(n)
    return ans

print(primefactor(num), end="")
