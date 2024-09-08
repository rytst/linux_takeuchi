
import os, sys, subprocess

ret = os.fork()


echo_path = subprocess.run(['which', 'echo'], text=True, capture_output=True)

if ret == 0:
    print("child process: pid={}, parent process: pid={}".format(os.getpid(), os.getppid()))
    os.execve(echo_path.stdout.strip(), ["echo", "hello from pid={}".format(os.getpid())], {})
    exit()

elif ret > 0:
    print("parent process: pid={}, child process: pid={}".format(os.getpid(), ret))
    exit()

sys.exit(1)
