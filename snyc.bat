"C:\Users\wming\cwRsync_5.5.0_x86_Free\bin\rsync.exe" -e '"C:\Users\wming\cwRsync_5.5.0_x86_Free\bin\ssh.exe" -i C:\Users\wming\.ssh\id_rsa' -r  ../tencent_server/ wmj@123.206.57.166:/web-server/
"C:\Program Files\Git\usr\bin\ssh.exe" wmj@123.206.57.166 "uwsgi --stop /web-server/uwsgi.pid"
"C:\Program Files\Git\usr\bin\ssh.exe" wmj@123.206.57.166 "uwsgi --ini /web-server/uwsgi.ini"