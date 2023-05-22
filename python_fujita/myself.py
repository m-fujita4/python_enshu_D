import argparse
import introduce


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='', type=str)
    parser.add_argument('age', help='', type=str)
    args = parser.parse_args()

    human = introduce.Intro(args.name, args.age)

    print(human.name_out())
    print(human.age_out())


if __name__ == '__main__':
    main()
