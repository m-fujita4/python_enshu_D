import sys
from func_salary import calcsalary
args = sys.argv

for i in range(1,len(args)):
    salary = int(args[i]) # 給与
    payment, tax_amount = calcsalary(salary) # payment : 支給額　tax_amount : 税額
    print("給与:",str(salary), "支給額:",str(payment), "税額:", str(tax_amount))