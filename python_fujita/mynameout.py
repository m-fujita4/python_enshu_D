import sys


def main():
    args = sys.argv

    # substitute args to var
    name = args[1]
    print(args[0])

    # aaa
    print(f"Hello, {name}!")


if __name__ == '__main__':
    main()
