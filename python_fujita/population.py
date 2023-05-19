import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('pos', help='', type=int)
    args = parser.parse_args()

    population_rank = (
        "China", "India", "U.S.A", "Indonesia", "Pakistan",
        "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico"
    )

    print(population_rank[args.pos-1], end='')


if __name__ == '__main__':
    main()
