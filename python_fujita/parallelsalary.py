# def check_smaller_than_10thousand(money):
#     if money < 10000:
# import argparse
import sys
from func_salary import calcsalary


def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument('salary', help='', type=int)
    # args = parser.parse_args()

    for salary in sys.argv[1:]:

        pay, tax = calcsalary(int(salary))

        print(f"給与:{int(salary)}、支給額:{int(pay)}、税額:{int(tax)}")


if __name__ == '__main__':
    main()
