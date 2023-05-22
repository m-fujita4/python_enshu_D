import argparse
import introfamily


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='', type=str)
    parser.add_argument('age', help='', type=str)
    parser.add_argument('cat', help='', type=str)
    args = parser.parse_args()

    family = introfamily.IntroFam(args.name, args.age, args.cat)

    print(family.name_out())
    print(family.age_out())
    print(family.cat_out())


if __name__ == '__main__':
    main()
