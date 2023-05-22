import sys
import introfamily
args = sys.argv

name = str(args[1])
age = int(args[2])
cat = str(args[3])

person = introfamily.IntroFam(name, age, cat)
print(person.name_out())
print(person.age_out())
print(person.cat_out())