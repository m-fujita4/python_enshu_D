import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('pos', help='', type=int)
    parser.add_argument('additional_animal', help='', type=str)
    args = parser.parse_args()

    animal_list = ["giraffe","tiger","zebra","elephant","lion"]

    animal_list.insert(args.pos, args.additional_animal)
    animal_list.pop()
    animal_list.sort()

    print(animal_list, end='')


if __name__ == '__main__':
    main()
