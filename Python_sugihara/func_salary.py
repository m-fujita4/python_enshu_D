#支給額と税額の計算
def cacsalary(salary):
    if(salary>=1000000):
        tax = int((salary-1000000) * 0.2 + 100000)
    else:
        tax = int(salary * 0.1)
        payment_amount =int(salary - tax) 
    return payment_amount,tax