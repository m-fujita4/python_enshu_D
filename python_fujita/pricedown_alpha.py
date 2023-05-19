import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('category', help='', type=str)
    parser.add_argument('pricecut', help='', type=int)
    args = parser.parse_args()

    hinmoku = {
        'リンゴ': 80, 'みかん': 198, 'バナナ': 150,
        'ビール': 360, '日本酒': 580,
        'ラーメン': 380, 'うどん': 128, 'パスタ': 258
        }

    fruits = ('リンゴ', 'みかん', 'バナナ')
    sake = ('ビール', '日本酒')
    noodle = ('ラーメン', 'うどん', 'パスタ')

    view = {
        '果物類': fruits, '酒類': sake, '麺類': noodle
        }

    for category, list in view.items():
        if args.category == category:
            for key in list:
                hinmoku[key] -= args.pricecut
                if hinmoku[key] < 1:
                    hinmoku[key] = 1

    print(hinmoku, end='')


if __name__ == '__main__':
    main()
