import os, sys


# if this is parent process, it returns its child pid
# if this is child process, it returns 0
ret = os.fork()


# child process
if ret == 0:
    print("child process: pid={}, parent process: pid={}".format(os.getpid(), os.getppid()))
    exit()


# parent process
elif ret > 0:
    print("parent process: pid={}, child process: pid={}".format(os.getpid(), ret))
    exit()

sys.exit(1)
