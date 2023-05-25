"""
import sys
args = sys.argv
input_salary=int(args[1])
"""

def calcsalary(salary):
    from decimal import Decimal , ROUND_HALF_UP

    if salary >= 1000000:
        tax=(salary-1000000)*0.2+100000

    else:
        tax=salary*0.1

    tax=Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

    pay_amount=salary-tax

    return pay_amount,tax

#print(calcsalary(input_salary))