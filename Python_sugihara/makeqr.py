import qrcode #パッケージのインポート
import os
import sys
args = sys.argv
input1 = str(args[1])
input2 = str(args[2])
path = os.path.join("..""..""local",input2)
img = qrcode.make(input1)
img.save(path)