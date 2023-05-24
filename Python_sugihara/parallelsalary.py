import func_salary
import sys
args = sys.argv
salary = int(args[1])
payment_amount,tax= func_salary.cacsalary(salary)     #func_salary.pyの関数を用いて支給額と税額を変数に代入

print("給与:",salary,"、" + "支給額:",payment_amount,"、" + "税額",tax)
