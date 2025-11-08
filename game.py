import time
import sys

def output(message, new_line=False, delay=0.02):
    for char in message:
        sys.stdout.write(char)
        time.sleep(delay)
    if new_line:
        sys.stdout.write('\n')

def boot_sequence():
    output('> _boot sequence initiated')
    output('...', True, 0.3)

    time.sleep(1)

    output('> assigned vessel: UAS MNEMOSYNE', True)
    output('> personal interface: VEIL-9 Life-Support Visor', True)
    output('>', True)

    time.sleep(1)

    output('> system integrity')
    output('..........', False, 0.3)
    time.sleep(0.7)
    output('\033[33mPARTIAL\033[0m', True)

    time.sleep(1)

    output('> visual feed')
    output('..........', False, 0.3)
    time.sleep(0.7)
    output('\033[31mOFFL!NE\033[0m [SIG_NAL ΔECAY ')
    output('██▓░░░]', True, 0.3)

    time.sleep(1)

    output('> auditory sensors')
    output('..........', False, 0.3)
    time.sleep(0.7)
    output('\033[33mPARTIΛL\033[0m', True, 0.3)

    time.sleep(0.5)

    output('> tactile feedback')
    output('..........', False, 0.3)
    time.sleep(0.7)
    output('\033[32mSTABLE\033[0m', True)

    time.sleep(1)

    output('> ', True, 0.3)
    output('> neural link handshake')
    output('...', True, 0.3)
    output('░▓▓░▓ █e̷cch̵o̷▓d̶ata̵▓re̶p̵e̷a̸t̵█▓░░', False)
    sys.stdout.write('\r')

    time.sleep(1)

    output('> ', True)
    output('> [ VEIL-9 LIFE SYSTEMS™ BOOT SEQUENCE ]', True)
    output('> ----------------------------------------', True)
    output('>  \033[35m“Because life support should feel like living.”\033[0m', True, 0.15)
    output('>  Property of \033[1mAurelius Dynamics\033[0m.', True)
    output('>  Unauthorized modification is a federal offense.', True)
    output('> ----------------------------------------', True)
    output('> ', True)
    output('> [VEIL-9] Initializing bioscan: STANDBY', True)
    output('> ', True)
    output('> ..........', True, 0.3)
    output('> \033[31m[bioscan incomplete]\033[0m', True)
    output('> [VEIL-9] User signature: CORRUPTED DATA', True)
    output('> [VEIL-9] Attempting new user authori', False, 0.05)
    output('▓▓▓▓▓▓▓▓▓▓▓▓▓', True, 0.2)
    time.sleep(4)
    output('> Auxiliary AI module detected → \033[31mARCHANGEL\033[0m//CORE', True)
    output('> [VEIL-9] External process requesting neural interface access.', True)
    output('>    origin: \033[31mARCHANGEL\033[0m//CORE', True)
    output('>    classification: Astronavigation & Guidance Heuristic', True)
    output('>    trust rating:', False)
    output(' ░░______%', True, 0.2)
    output('> ', True)
    output('> \033[31mWARNING — this connection may violate corporate firmware policy.\033[0m', True)
    output('> Proceed with integration? [Y/N]', True)
    output('> ', True)
    output('>> ', False)

    while True:
        accepted_inputs = ('y', 'Y', 'n', 'N')
        yes_or_no = input()
        if yes_or_no in accepted_inputs:
            break
        output('> INVALID INPUT: Type a valid input')
        time.sleep(1)
        sys.stdout.write('\r')
        output('>> ')


def character():
    pass

def game():
    pass

def main():
    boot_sequence()

if __name__ == "__main__":
    main()