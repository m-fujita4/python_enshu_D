import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='表示する名前')

    args = parser.parse_args()

    print(f"Hello {args.name} !", end='')


if __name__ == '__main__':
    main()
