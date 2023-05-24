import argparse
import datetime


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('date', help='', type=str)
    parser.add_argument('adalt', help='', type=int)
    parser.add_argument('child', help='', type=int)
    args = parser.parse_args()

    dist_changes = {
        "weekday": {"adalt": 2000, "child": 1200},
        "holiday": {"adalt": 2400, "child": 1500}
        }

    weekdays = (0, 1, 2, 3, 4)
    holidays = (5, 6)

    year, month, day = args.date[0:4], args.date[4:6], args.date[6:8]
    today = datetime.date(int(year), int(month), int(day))
    weekday = today.weekday()  # 0~6

    if weekday in weekdays:
        print(dist_changes["weekday"]["adalt"] * args.adalt + dist_changes["weekday"]["child"] * args.child, end="")
    elif weekday in holidays:
        print(dist_changes["holiday"]["adalt"] * args.adalt + dist_changes["holiday"]["child"] * args.child, end="")

    print(sum, end="")


if __name__ == '__main__':
    main()
