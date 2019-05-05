import os
import sys

argCount = len(sys.argv)
if argCount == 1:
    print("python", "to.py", "-help")
    exit(0)

key = sys.argv[1]
if key in ["help", "-help", "--help"]:
    print("params list:")
    print("%10s" % "dp|deply", "to deply file folder", sep=" --> ")
    print("%10s" % "out", "to packup out file folder", sep=" --> ")
    exit(0)

path = "C:\\Users\\Administrator\\Desktop\\tools"
if key in ['dp', 'deply']:
    path = "F:\\LIANLIAN_DAYLY\\生产环境\\升级申请\\升级文件列表"
elif key == 'out':
    path = "F:\\output"

os.system("explorer " + path)
