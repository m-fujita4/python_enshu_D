from decimal import Decimal, ROUND_HALF_UP
import sys
args = sys.argv
salary = int(args[1])
if(salary>=1000000):
    tax = (salary-1000000) * 0.2 + 100000
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
else:
    tax = int(salary * 0.1)
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
payment_amount = salary - tax
payment_amount = Decimal(str(payment_amount)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
print("支給額:"+str(payment_amount)+"、"+"税額:"+str(tax),end="")