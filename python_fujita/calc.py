import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('var1', help='', default=1)
    parser.add_argument('var2', help='', default=2)
    parser.add_argument('var3', help='', default=3)

    args = parser.parse_args()

    sum = int(args.var1) + int(args.var2) + int(args.var3)

    print(sum, end='')


if __name__ == '__main__':
    main()
