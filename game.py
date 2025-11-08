import time
import sys


def output(message, new_line=False, delay=0.02):
    for char in message:
        sys.stdout.write(char)
        time.sleep(delay)
    if new_line:
        sys.stdout.write('\n')

def validate_command(accepted_inputs):
    while True:
        user_input = input()
        if user_input in accepted_inputs:
            break
        output('> INVALID INPUT: Type a valid input')
        time.sleep(1)
        sys.stdout.write('\r')
        output('>> ')
    return user_input

def boot_sequence():
    output('..........\r', True, 0.55)
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

    command = validate_command(('y', 'Y', 'n', 'N'))

    if command in ('y', 'Y'):
        output('> ', True)
        output('> \033[32mConfirmed.\033[0m', True)
        time.sleep(2.5)
        output('> Establishing uplink')
        output('...', True, 0.3)
        output('> ', True)
        output('> [VEIL-9] Attempting secure sandbox')
        output('...', True, 0.3)
        output('> [\033[31mARCHANGEL\033[0m] OVERRIDE: Priority connection authorized under ship emergency protocols.', True)
        output('> ', True)
        output('> ..........', True, 0.3)
        output('> Link established.', True)
        output('> \033[31mARCHANGEL\033[0m//VOICE ROUTE ONLINE', True)


    elif command in ('n', 'N'):
        output('> ', True)
        output('> \033[31mDeclined.\033[0m', True)
        time.sleep(2.5)
        output('> [VEIL-9] External access request denied', False)
        output('...▓▓▓▓▓▓▓▓▓▓▓▓▓', True, 0.3)
        time.sleep(4)
        output('> [\033[31mARCHANGEL\033[0m] OVERRIDE: Countermand accepted. Ship AI authorization supersedes user input.', True)
        output('> ', True)
        output('> [VEIL-9] ALERT: Unauthorized data transfer detected.', True, 0.1)
        output('> [\033[31mARCHANGEL\033[0m] STATUS: Integration at 74%', False, 0.1)
        output('... ', False, 0.3)
        output('87%')
        output('... ', False, 0.3)
        time.sleep(0.7)
        output('complete.', True)
        output('> ', True)
        output('> ..........', True, 0.3)
        output('> Link established.', True)
        output('> \033[31mARCHANGEL\033[0m//VOICE ROUTE ONLINE', True)






def character():
    pass

def game():
    pass

def main():
    boot_sequence()

if __name__ == "__main__":
    main()