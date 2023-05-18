import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'var1', help='', type=int, default=1
        )
    parser.add_argument(
        'var2', help='', type=int, default=2
        )
    parser.add_argument(
        'var3', help='', type=int, default=3
        )
    args = parser.parse_args()

    print(args.var1 + args.var2 + args.var3, end='')


if __name__ == '__main__':
    main()
