apt install python3.8-venv

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate

python_file=$(pwd)/venv/bin/python
manage_file=$(readlink -f manage.py)
running_file=$(readlink -f runserver.sh)
project_root=$(pwd)

echo "[Unit]
Description=MMD VPN Startup Script
[Service]
Restart=on-failure
WorkingDirectory=$project_root
ExecStart=$python_file $manage_file runserver 0.0.0.0:80
[Install]
WantedBy=multi-user.target" >mmdvpn.service
mv mmdvpn.service /lib/systemd/system/mmdvpn.service

echo "
source ./venv/bin/activate
python manage.py runserver 0.0.0.0:80
" >"$running_file"

chmod +x runserver.sh
chmod +x adduser.sh

echo "#############################################"
echo "############# Create Admin User #############"
echo "#############################################"
python manage.py createsuperuser
echo "############# You can create another admin user by executing ./adduser.sh #############"

systemctl daemon-reload
systemctl eable --now mmdvpn

echo "<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>"
echo "<<<<<<<<<<<<<<<    >>>>>>>>>>>>>>>>"
echo "<<<<<<<<<<<<          >>>>>>>>>>>>>"
echo "<<<<<<<<<                >>>>>>>>>>"
echo "<<<<<<                      >>>>>>>"
echo "<<<   installed successfully   >>>>"
echo "<<<<<<                      >>>>>>>"
echo "<<<<<<<<<                >>>>>>>>>>"
echo "<<<<<<<<<<<<          >>>>>>>>>>>>>"
echo "<<<<<<<<<<<<<<<    >>>>>>>>>>>>>>>>"
echo "<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>"
