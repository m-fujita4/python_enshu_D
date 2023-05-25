# 必要なモジュールのインポート
import qrcode
import os
import sys
# 引数を入力する
args = sys.argv
# 引数に名前つける
url = args[1]
file_name = args[2]
    # ファイル名に拡張子を追加する
    # file_name = "{0}.png".format(file_name)
# パスを作成する
path = os.path.join("..","files",f"{args[2]}.png")
# QRコード作成
img = qrcode.make(url)
# 出力
img.save(path)

