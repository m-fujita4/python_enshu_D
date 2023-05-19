import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'num', type=int, help=''
        )
    args = parser.parse_args()

    if args.num % 2 == 0:
        print("偶数", end='')
    else:
        print("奇数", end='')


if __name__ == '__main__':
    main()
