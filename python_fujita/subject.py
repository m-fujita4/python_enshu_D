import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mat', help='', type=int,)
    parser.add_argument('jap', help='', type=int,)
    parser.add_argument('eng', help='', type=int,)
    args = parser.parse_args()

    judge = "不合格"
    sum = args.mat + args.jap + args.eng

    if (args.mat >= 70 and args.jap >= 70 and args.eng >= 70) or sum >= 220:
        if args.mat >= 50 and args.jap >= 50 and args.eng >= 50:
            judge = "合格"

    print(judge, end='')


if __name__ == '__main__':
    main()
