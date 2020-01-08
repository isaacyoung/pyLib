import os
import sys
import svn.remote
import ctypes
# pip install svn

args_length = len(sys.argv)
if args_length == 1:
    print('params list:')
    print('%10s' % 'center','unified center branshes version',sep=' --> ')
    print('%10s' % 'auth','unified auth branshes version',sep=' --> ')

    print('%10s' % 'sc_center','local center branshes version',sep=' --> ')
    print('')

    print('additional param:')
    print('%10s' % '-n','max row number',sep=' --> ')
    exit(0)

key = sys.argv[1]

if key == 'center':
    url = 'http://192.168.68.12/svn/app/unifiedcenter/branches/'
elif key == 'auth':
    url = 'http://192.168.68.12/svn/app/unifiedauth/branches/'
elif key == 'sc_center':
    url = 'http://192.168.68.12/svn/app/paymenthall/branches/'

r = svn.remote.RemoteClient(url)
files = list(r.list())

max_num = 10
if args_length == 4 and sys.argv[2] == '-n':
    max_num = int(sys.argv[3])

length = len(files) - max_num
if length < 0:
    length = 0

for f in files[length:]:
    r = svn.remote.RemoteClient(url + f)
    logs = r.log_default(stop_on_copy=True)

    for log in logs:
        # print(log)
        msg = log.msg
        author = log.author
    if msg is None:
        msg = ""
    print(f + " " + msg + " " + author)
    # break