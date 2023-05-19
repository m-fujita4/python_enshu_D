import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('sentence', help='', type=str)
    parser.add_argument('pos', help='', type=int)
    args = parser.parse_args()

    print(args.sentence.split()[args.pos-1], end='')


if __name__ == '__main__':
    main()
