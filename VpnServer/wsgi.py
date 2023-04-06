import os
import threading
from time import sleep

from django.core.wsgi import get_wsgi_application

from VpnServer.settings import REBOOT_PERIOD_SECONDS
from packs.models import check_finished_packs, init_sshd_services

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VpnServer.settings')

application = get_wsgi_application()

threading.Thread(target=check_finished_packs, daemon=True).start()

init_sshd_services()


def reboot_os():
    sleep(REBOOT_PERIOD_SECONDS)
    import os
    os.system('reboot')


threading.Thread(target=reboot_os, daemon=True).start()
