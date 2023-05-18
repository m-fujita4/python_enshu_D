import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'var', help='', type=str, default='war'
        )
    args = parser.parse_args()

    print(f"I don't like {args.var}", end='')


if __name__ == '__main__':
    main()
