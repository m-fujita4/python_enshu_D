import qrcode
import os
import sys
args = sys.argv
url=args[1]
pic_name=args[2]

path=os.path.join("..","..","files",pic_name)

img=qrcode.make(url)
img.save(path)