from passlib.hash import sha512_crypt
import subprocess
import pwd


def add_user(username, password):
    pwd = sha512_crypt.encrypt(password)
    return subprocess.call(["useradd", username, "-m", "-p", pwd])


def del_user(username):
    return subprocess.call(["userdel", "-r", username])


def lock_user(username):
    return subprocess.call(["usermod", "-L", username])


def unlock_user(username):
    return subprocess.call(["usermod", "-U", username])


def list_users():
    return list(map(lambda i: i[0], filter(lambda i: int(i[2]) >= 1000, pwd.getpwall())))

