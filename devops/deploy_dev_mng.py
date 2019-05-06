"""
deploy

need:
    pip install paramiko

"""

import sys

import paramiko


def print_process(s):
    sys.stdout.write("\r___________________________________________" + s)
    sys.stdout.flush()


ip = '192.168.60.3'
port = 22
username = 'root'
password = 'jieka@123'

ssh = paramiko.SSHClient()
t = paramiko.Transport((ip, port))

try:
    print_process("0%")

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password)
    print_process("10%")

    ssh.exec_command('rm -Rf /data/temp/*')
    ssh.exec_command('killall -9 java')
    print_process("20%")

    ssh.exec_command('cp -R /usr/local/tomcat6/webapps/LIANLIAN_MNG_LOGISTICS.war /data/backup/LIANLIAN_MNG_LOGISTICS_`date "+%Y%m%d%H%M"`.war')
    print_process("50%")

    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    print_process("60%")

    sftp.put(r'E:\s\LIANLIAN_MNG_LOGISTICS.war.zip', '/data/temp/LIANLIAN_MNG_LOGISTICS.war.zip')
    print_process("80%")
    sftp.close()

    ssh.exec_command('/data/deploy.sh')
    print_process("100%")

except Exception as e:
    print(e)
finally:
    t.close()
    ssh.close()
