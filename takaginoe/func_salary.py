def calcsalary(salary):
    tax_upper = 0.2 # 100万円超のときの税率
    tax_lower = 0.1 # 100万円以下のときの税率
    tax_amount = 0 # 税額
    if salary >= 1000000:
        tax_amount = int((salary - 1000000) * tax_upper + 100000)
    else:
        tax_amount += int(salary * tax_lower)

    # 支給額を計算する
    return (int(salary -  tax_amount), tax_amount)