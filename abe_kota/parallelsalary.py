from func_salary import calcsalary

import sys
args = sys.argv
input_salary1=int(args[1])
input_salary2=int(args[2])
input_salary3=int(args[3])

#returnで値を二つ返しているのでそれぞれ変数に代入
pay_amount,tax=calcsalary(input_salary)

print(f"給与:{input_salary}、支給額:{pay_amount}、税額:{tax}")