from rich import print
from rich.text import Text

def start():
    while True:
        try:
            command = str(input("user@blackhole~$ "))
        except KeyboardInterrupt:
            print("\nExiting...")
            break