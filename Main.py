import signal
import sys
import os
from src.shell.shell import start

def Signal_handler(signum, frame):
    print(f"[SECURITY] Received signal {signum}, initializing secure shutdown...", file=sys.stderr)
    sys.exit(128 + signum)
if __name__ == "__main__":
    start()

signal.signal(signal.SIGINT, Signal_handler)
signal.signal(signal.SIGTERM, Signal_handler)

