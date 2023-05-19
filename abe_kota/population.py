import sys
args = sys.argv

num=int(args[1])

countries=("China", "India", "U.S.A", "Indonesia", "Pakistan", 
           "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

print(countries[num-1])