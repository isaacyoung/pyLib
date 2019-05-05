import os
import sys

argCount = len(sys.argv)
if argCount == 1:
    print("python", "do.py", "-help")
    exit(0)

key = sys.argv[1]
if key in ["help", "-help", "--help"]:
    print("params list:")
    print("%10s" % "ch|cache", "run memcached", sep=" --> ")
    exit(0)

path = ''
if key in ['ch', 'cache']:
    path = r"C:\Users\Administrator\Desktop\tools\memcached.exe"

if path != '':
    os.system('start ' + path)
