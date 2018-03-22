"D:\Program Files\Git\usr\bin\ssh.exe" wmj@123.206.57.166 "uwsgi --stop /web-server/cloud-server/uwsgi.pid"
"D:\Program Files\Git\usr\bin\ssh.exe" wmj@123.206.57.166 "cd /web-server/cloud-server/ && git pull origin master"
"D:\Program Files\Git\usr\bin\scp.exe" wx/secret.py wmj@123.206.57.166:/web-server/cloud-server/wx/secret.py
"D:\Program Files\Git\usr\bin\scp.exe" tencent_server/SECRET_KEY.py wmj@123.206.57.166:/web-server/cloud-server/tencent_server/SECRET_KEY.py
"D:\Program Files\Git\usr\bin\ssh.exe" wmj@123.206.57.166 "uwsgi --ini /web-server/cloud-server/uwsgi.ini"