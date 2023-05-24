import os
import qrcode
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='', type=str)
    parser.add_argument('fname', help='', type=str)
    args = parser.parse_args()

    os.makedirs("../files/", exist_ok=True)
    qr = qrcode.QRCode()
    qr.add_data(args.url)

    img = qr.make_image()
    path = os.path.join("..", "files", args.fname)
    img.save(path)


if __name__ == '__main__':
    main()
