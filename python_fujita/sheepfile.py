import os
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('num_sheep', help='', type=int)
    parser.add_argument('--dst_dir', help='', type=str, default="files")
    parser.add_argument('--dst_fname', help='', type=str, default="sheep.txt")
    args = parser.parse_args()

    path_dir = os.path.join("./python_fujita/", args.dst_dir)
    os.makedirs(path_dir, exist_ok=True)

    path_w = os.path.join(path_dir, args.dst_fname)

    # 改行しちゃうよ；；
    # with open(path_w, mode='w') as f:
    #     for i in range(args.num_sheep):
    #         f.write(f"ひつじが{i+1}匹\n")

    # 改行を絶対に許さないマン
    list = []
    with open(path_w, mode='w') as f:
        for i in range(args.num_sheep):
            list.append(f"ひつじが{i+1}匹")
        hoge = '\n'.join(list)
        f.write(hoge)


if __name__ == '__main__':
    main()
