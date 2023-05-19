import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('num_sheep', help='', type=int)
    args = parser.parse_args()

    for i in range(args.num_sheep):
        print(f"ひつじが{i+1}匹")


if __name__ == '__main__':
    main()
