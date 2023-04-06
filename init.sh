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

chmod +x runserver.sh