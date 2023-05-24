def calcsalary(salary, threshold=1000000, tax_rate1=0.1, tax_rate2=0.2):
    if salary > threshold:
        tax = threshold * tax_rate1 + (salary - threshold) * tax_rate2
    else:
        tax = salary * tax_rate1

    return salary - tax, tax
