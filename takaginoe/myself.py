import sys
import introduce
args = sys.argv

name = str(args[1])
age = int(args[2])

person = introduce.Intro(name, age)
print(person.name_out())
print(person.age_out())