import os
import sys

argCount = len(sys.argv)
if argCount == 1:
    exit(0)

key = sys.argv[1]
path = "C:\\Users\\Administrator\\Desktop\\tools"
if key in ['dp','deply']:
    path = "F:\\LIANLIAN_DAYLY\\生产环境\\升级申请\\升级文件列表"
elif key == 'out':
    path = "F:\\output"

os.system("explorer " + path)