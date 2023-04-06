apt install python3.8-venv

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate

running_file=$(readlink -f runserver.sh)
echo "[Unit]
Description=MMD VPN Startup Script
[Service]
ExecStart=$running_file
[Install]
WantedBy=multi-user.target" >mmdvpn.service
mv mmdvpn.service /lib/systemd/system/mmdvpn.service

manage_file=$(readlink -f manage.py)
source_venv=$(readlink -f venv/bin/activate)
echo "
source $source_venv
python $manage_file runserver 0.0.0.0:80
" >"$running_file"

chmod +x runserver.sh
chmod +x adduser.sh
