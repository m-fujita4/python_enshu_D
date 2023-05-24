from func_salary import calcsalary

import sys
args = sys.argv
input_salary=int(args[1])

#returnで値を二つ返しているのでそれぞれ変数に代入
pay_amount,tax=calcsalary(input_salary)

print(f"給与:{input_salary}、支給額:{pay_amount}、税額:{tax}")