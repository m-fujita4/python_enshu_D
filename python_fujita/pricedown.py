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

    if args.category == '果物類':
        hinmoku['リンゴ'] -= args.pricecut
        hinmoku['みかん'] -= args.pricecut
        hinmoku['バナナ'] -= args.pricecut
    elif args.category == '酒類':
        hinmoku['ビール'] -= args.pricecut
        hinmoku['日本酒'] -= args.pricecut
    elif args.category == '麺類':
        hinmoku['ラーメン'] -= args.pricecut
        hinmoku['うどん'] -= args.pricecut
        hinmoku['パスタ'] -= args.pricecut
    else:
        pass

    for key, value in hinmoku.items():
        if value < 0:
            hinmoku[key] = 1

    print(hinmoku, end='')


if __name__ == '__main__':
    main()
