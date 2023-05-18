import sys
args = sys.argv
salary = int(args[1])
if(salary>=1000000):
    tax = int((salary-1000000) * 0.2 + 100000)
else:
    tax = int(salary * 0.1)
payment_amount =int(salary - tax) 
print("支給額:"+str(payment_amount)+"、"+"税額:"+str(tax),end="")
