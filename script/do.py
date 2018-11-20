import os
import sys

argCount = len(sys.argv)
if argCount == 1:
    exit(0)

key = sys.argv[1]
path = ''
if key in ['ch','cache']:
    path = r"C:\Users\Administrator\Desktop\tools\memcached.exe"

if path != '':
    os.system('start ' + path)