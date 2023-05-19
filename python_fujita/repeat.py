import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('diff', help='', type=int)
    args = parser.parse_args()

    sum = 0
    while True:
        sum += args.diff
        if sum == 100:
            print("Just 100!", end='')
            break
        elif sum > 100:
            print("Over!", end='')
            break
        else:
            continue


if __name__ == '__main__':
    main()
