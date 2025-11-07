import time
import sys

def output(message):
    delay = 0.05
    for char in message:
        sys.stdout.write(char)
        time.sleep(delay)
    sys.stdout.write('\n')

def boot_sequence():
    delay = 0.4
    output('> _boot sequence initiated...')
    time.sleep(delay)

def character():
    pass

def game():
    pass

def main():
    boot_sequence()

if __name__ == "__main__":
    main()