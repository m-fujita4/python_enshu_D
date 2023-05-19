from decimal import Decimal , ROUND_HALF_UP

import sys
args = sys.argv

salary=int(args[1])

if salary >= 1000000:
    #tax_rate=(salary-1000000)*0.2+100000
    tax=(salary-1000000)*0.2+100000

else:
    #tax_rate=salary*0.1
    tax=salary*0.1

tax=Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

pay_amount=salary-tax

#print(tax_rate)
print(f"支給額:{pay_amount}、税額:{tax}",end="")