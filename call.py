import subprocess
import shlex


class Task(object):
    """Little Wrapper around subprocess.call to demonstrate the usage of __call__"""

    def __call__(self, command):
        cmd = shlex.split(command)
        return subprocess.call(cmd)

t = Task()

t("ls -l")
