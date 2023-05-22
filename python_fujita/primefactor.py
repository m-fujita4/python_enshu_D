import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('num', help='', type=int)
    args = parser.parse_args()

    factor = 2
    num = args.num  # 2023
    list = []
    while num >= factor:
        if num % factor == 0:
            num = num // factor
            list.append(factor)
        else:
            factor = factor + 1

    print(list, end="")


if __name__ == '__main__':
    main()
