import sys


def main():
    args = sys.argv

    # substitute args to var
    name = args[1]

    # aaa
    print(f"Hello {name} !", end='')


if __name__ == '__main__':
    main()
