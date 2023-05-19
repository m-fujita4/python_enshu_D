from decimal import Decimal, ROUND_HALF_UP
import sys
args = sys.argv
# 引数を変数に代入
salary = int(args[1])

if salary > 1000000:
    tax_rate = 0.2
    tax = (salary-1000000)*tax_rate + 1000000*0.1

else:
    tax_rate = 0.1
    tax = salary*tax_rate
    
tax = Decimal(str(tax)).quantize(Decimal("0"),rounding = ROUND_HALF_UP)
pay_amount = salary - tax
print("支給額:" + str(pay_amount) + "、税額:" + str(tax), end="")

