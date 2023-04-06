import datetime
import os
import random
import shutil
import string
import subprocess
import time

from django.contrib.auth.models import User
from django.db import models

from VpnServer.settings import PORTS
from . import os_user


class Pack(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name='packs')
    start_time = models.DateTimeField(blank=True, null=True, default=None)
    days = models.IntegerField(blank=False, null=False)
    linux_username = models.CharField(blank=True, null=True, default='', max_length=10)
    linux_password = models.CharField(blank=True, null=True, default='', max_length=10)
    port = models.IntegerField(default=0, blank=True, null=True)
    started = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + '-' + 'pack' + str(self.id) + '(' + str(self.days) + ' days)'

    def get_most_free_port(self):
        uses = {}
        for port in PORTS:
            uses[port] = 0
        for pack in Pack.objects.filter(started=True, finished=False):
            if uses.__contains__(pack.port):
                uses[pack.port] += 1

        best_port = PORTS[0]
        for port in PORTS:
            if uses[port] < uses[best_port]:
                best_port = port
        return best_port

    def run_pack(self):
        if self.start_time is None:
            self.start_time = datetime.datetime.now()
        self.started = True
        self.finished = False
        if self.linux_username == '' or self.linux_username is None:
            self.linux_username = 'vpn' + str(self.id)
        if self.linux_password == '' or self.linux_password is None:
            letters = string.ascii_lowercase + string.digits
            self.linux_password = ''.join(random.choice(letters) for _ in range(8))
            self.port = self.get_most_free_port()
        self.save()
        os_user.add_user(self.linux_username, self.linux_password)
        self.run_ssh_service()

    def run_ssh_service(self):
        with open('sshd_config', 'r') as file:
            filedata = file.read()
        filedata = filedata.replace('$username$', self.linux_username)
        filedata = filedata.replace('$port$', str(self.port))
        related_ssh_config_file = self.get_ssh_config_path()
        with open(related_ssh_config_file, 'w') as file:
            file.write(filedata)
        os.system('/usr/sbin/sshd -f ' + os.path.abspath(related_ssh_config_file))

    def finish(self):
        self.started = True
        self.finished = True
        self.save()
        os_user.remove_user(self.linux_username)

    def get_ssh_command(self):
        related_ssh_config_file = self.get_ssh_config_path()
        return '/usr/sbin/sshd -f ' + os.path.abspath(related_ssh_config_file)

    def get_ssh_config_path(self):
        return 'ssh_configs/' + self.linux_username + '_ssh'


def check_finished_packs():
    while True:
        time.sleep(60 * 60)
        for pack in Pack.objects.filter(started=True, finished=False):
            passed_seconds = (datetime.datetime.now(datetime.timezone.utc) - pack.start_time).total_seconds()
            if passed_seconds > (pack.days * 24 * 60 * 60):
                pack.finish()


def init_sshd_services():
    ssh_configs_folder = "ssh_configs"
    if not os.path.exists(ssh_configs_folder):
        os.makedirs(ssh_configs_folder)

    for filename in os.listdir(ssh_configs_folder):
        file_path = os.path.join(ssh_configs_folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    for pack in Pack.objects.filter(started=True, finished=False):
        pack.run_pack()
