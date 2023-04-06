import os
import threading

from django.core.wsgi import get_wsgi_application

from packs.models import check_finished_packs, init_sshd_services

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VpnServer.settings')

application = get_wsgi_application()

threading.Thread(target=check_finished_packs, daemon=True).start()

init_sshd_services()
