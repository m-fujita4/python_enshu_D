import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('salary', help='', type=int)
    args = parser.parse_args()

    threshold = 1000000
    if args.salary > threshold:
        tax = threshold * 0.1 + (args.salary - threshold) * 0.2
    else:
        tax = args.salary * 0.1

    pay = args.salary - tax

    print(f"支給額:{int(pay)}、税額:{int(tax)}", end='')


if __name__ == '__main__':
    main()
