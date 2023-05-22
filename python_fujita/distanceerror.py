import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('loc_dep', help='', type=str)
    parser.add_argument('loc_dst', help='', type=str)
    args = parser.parse_args()

    dic = {
        "東京": 0.00, "品川": 6.78, "新横浜": 25.54,
        "名古屋": 342.02, "京都": 476.31, "新大阪": 515.35
    }

    try:
        distance = abs(dic[args.loc_dep] - dic[args.loc_dst])
        print(round(distance, 2), end='')
    except KeyError:
        print("のぞみの停車駅を引数に設定してください", end='')


if __name__ == '__main__':
    main()
