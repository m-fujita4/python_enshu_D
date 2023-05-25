from func_salary import calcsalary
import sys
# 引数入力
args = sys.argv

for i in range(1,len(args)):
# 結果の出力
    salary = int(args[i])
    pay_amount,tax = calcsalary(salary)
    print("給与:",str(salary) ,"支給額:" , str(pay_amount) , "、税額:" , str(tax))
