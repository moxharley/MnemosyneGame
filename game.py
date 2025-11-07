import time
import sys

def output(message):
    delay = 0.25
    for char in message:
        sys.stdout.write(char)
        time.sleep(delay)

def character():
    pass

def game():
    pass

def main():
    output('> Test Message')

if __name__ == "__main__":
    main()