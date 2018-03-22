"D:\Program Files\cwRsync_5.5.0_x86_Free\bin\rsync.exe" -e "'D:\Program Files\Git\usr\bin\ssh.exe'" -r ../tencent_server/ wmj@123.206.57.166:/web-server/
"D:\Program Files\Git\usr\bin\ssh.exe" wmj@123.206.57.166 "uwsgi --stop /web-server/uwsgi.pid"
"D:\Program Files\Git\usr\bin\ssh.exe" wmj@123.206.57.166 "uwsgi --ini /web-server/uwsgi.ini"