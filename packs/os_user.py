import subprocess


def set_password(username, password):
    try:
        password = password.encode() + b'\n'
        subk = dict(stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        pwd_change = subprocess.Popen(['passwd', username], **subk)
        for i in range(2):
            pwd_change.stdin.write(password)
        (output, err) = pwd_change.communicate()
        pwd_change.wait()
        print("passwd output: " + str(output))
    except Exception as e:
        print(e)
        print(f"Failed to set password of {username}.")
        raise e


def add_user(username, password):
    try:
        subprocess.run(['useradd', '-p', password, username])
        set_password(username, password)
        print('New user by ' + username + ' username and ' + password + ' password')
    except Exception as e:
        print(e)
        print(f"Failed to add user {username}.")


def remove_user(username):
    try:
        subprocess.run(['userdel', '-r', username])
        print('User by ' + username + ' username was deleted successfully')
    except Exception as e:
        print(e)
        print(f"Failed to remove user {username}.")
