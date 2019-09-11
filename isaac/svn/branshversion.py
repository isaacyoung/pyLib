import svn.remote

url = "http://192.168.68.12/svn/app/unifiedcenter/branches/"
r = svn.remote.RemoteClient(url)
files = r.list()
for f in files:
    r = svn.remote.RemoteClient(url + f)
    logs = r.log_default(stop_on_copy=True)

    for log in logs:
        msg = log.msg
    if msg is None:
        msg = ""
    print(f + " " + msg)
