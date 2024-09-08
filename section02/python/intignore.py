import signal


# ignore SIGIINT signal
# first arg is signal number which is set for following signal handler
# socond arg is signal handler

signal.signal(signal.SIGINT, signal.SIG_IGN)

while True:
    pass
