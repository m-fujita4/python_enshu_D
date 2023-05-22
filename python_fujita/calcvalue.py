import argparse


def calcvalue(value):
    if value % 2 == 0:
        print(f"{value}は偶数")
    elif value % 2 == 1:
        print(f"{value}は奇数")
    else:
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('value1', help='', type=int)
    parser.add_argument('value2', help='', type=int)
    parser.add_argument('value3', help='', type=int)
    args = parser.parse_args()

    calcvalue(args.value1)
    calcvalue(args.value2)
    calcvalue(args.value3)


if __name__ == '__main__':
    main()
