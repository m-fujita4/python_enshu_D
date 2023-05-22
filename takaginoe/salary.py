# 給料から税金を差し引き、支給額を求める。
# <計算率>
# 100万円を超える部分の税率：20％
# 100万円以下の部分：10%
# 計算式：給与-税額=支給額、給与×税率=税額

import sys

# 標準入力を受け付ける
args = sys.argv

tax_upper = 0.2 # 100万円超のときの税率
tax_lower = 0.1 # 100万円以下のときの税率

# 変数salaryに入力した給料を入れる
salary = int(args[1])
tax_amount = 0 # 税額
if salary >= 1000000:
    tax_amount = int((salary - 1000000) * tax_upper + 100000)
else:
    tax_amount += int(salary * tax_lower)

# 支給額を計算する
payment = int(salary -  tax_amount) # 支給額

print("支給額:{0}、税額:{1}".format(payment,tax_amount), end="")