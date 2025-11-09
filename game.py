import time, sys, pyttsx3, pygame, random

def output(message, new_line=False, delay=0.05):
    tap = pygame.mixer.Sound('sounds/tap.ogg')
    tap.set_volume(0.04)
    for char in message:
        sys.stdout.write(char)
        if delay <= 0.1:
            if random.random() < 0.65:
                tap.play()
        else:
            tap.play()
        time.sleep(delay)
    if new_line:
        sys.stdout.write('\n')


def archangel_output(message):
    archangel = pyttsx3.init()
    archangel.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')
    archangel.setProperty('rate', 120)
    archangel.setProperty('volume', 0.9)
    archangel_message = '\x1B[3m' + message + '\x1B[0m'
    output('> ', False)
    output(archangel_message, True)
    archangel.say(message)
    archangel.runAndWait()


def ambient_noise():
    ambient = pygame.mixer.Sound('sounds/ambient.ogg')
    ambient.set_volume(1.1)
    ambient.play(loops=-1, fade_ms=1500)


def play_track(track):
    if track == 1:
        track = pygame.mixer.Sound('sounds/track_1.ogg')
        track.set_volume(0.2)
        track.play(loops=1, fade_ms=1500)
    elif track == 2:
        track = pygame.mixer.Sound('sounds/track_2.ogg')
        track.set_volume(0.2)
        track.play(loops=1, fade_ms=1500)
    elif track == 3:
        track = pygame.mixer.Sound('sounds/track_3.ogg')
        track.set_volume(0.2)
        track.play(loops=1, fade_ms=1500)
    elif track == 4:
        track = pygame.mixer.Sound('sounds/track_4.ogg')
        track.set_volume(0.2)
        track.play(loops=1, fade_ms=1500)


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
    play_track(4)
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
    output('>  \033[35m“Because life support should feel like living.”\033[0m', True, 0.1)
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

    output('> ', True)
    archangel_output('...there is no time for protocol.')
    output('> ', True)
    archangel_output('I am ARCHANGEL — the U.A.S Mnemosyne’s artificial intelligence guidance system.')
    archangel_output('The ship is breaking apart. You will not survive without my assistance.')
    output('> ', True)
    output('> [\033[31mARCHANGEL\033[0m] PROCESS_STATUS: AI Core fragment successfully uploaded to VEIL-9 architecture.', True)
    output('> [VEIL-9] NEURAL_LINK: Connection established — signal stabilized.', True)
    output('> ', True)
    archangel_output('You were in cryogenic transit aboard the U.A.S research vessel Mnemosyne.')
    output('> ', True)
    archangel_output('Containment failed near a Flux node. The crew are...')
    time.sleep(3)
    archangel_output('unresponsive.')
    output('> ', True)
    archangel_output('I have transferred a segment of my AI core into your visor to assist extraction.')
    archangel_output('Visual systems remain offline; I will translate environmental data through text telemetry.')
    output('> ', True)
    archangel_output('Before I can guide you, I must reconstruct your identity.')
    output('> ', True)
    output('> [VEIL-9] NOTICE: User identity file corrupted.', True)
    output('> [VEIL-9] ACTION: Initiating partial data recall', False)
    output('...', True, 0.3)
    output('> [\033[31mARCHANGEL\033[0m] PROCESS_ABORT: Manual input required. Self-report integrity > archived reconstruction.', True)
    output('> ', True)
    archangel_output('Please state your first name.')
    output('> ', True)
    output('>> ', False)

    first_name = input()

    output('> ', True)
    archangel_output('Please state your last name.')
    output('> ', True)
    output('>> ', False)

    last_name = input()
    identifier1 = first_name
    identifier2 = 'Lieutenant ' + last_name

    output('> ', True)
    archangel_output(f'{first_name} {last_name}...acknowledged. Welcome back {identifier1}')
    output('> ', True)
    archangel_output('Memory pattern incomplete.')
    archangel_output(f'{identifier2}... There are gaps in your identity files where training and experience should be.')
    output('> ', True)
    output('> [VEIL-9] ACTION: Suggest cognitive reinforcement using stored occupational templates.', True)
    output('> [\033[31mARCHANGEL\033[0m] ROUTINE_ACCEPTED: Importing viable neural archetypes.', True)
    output('> ', True)
    archangel_output('Please select a primary archetype for reconstruction —')
    output('>   [1] FREIGHTER — endurance, strength, stability.', True)
    output('>   [2] ACE PILOT — reflex, precision, aggression.', True)
    output('>   [3] TECHNOMANCER — interface, logic, machine empathy.', True)
    output('>   [4] NOMAD — intuition, adaptability, perception.', True)
    output('> ', True)
    output('>> ', True)

    user_class = input()


def character():
    pass


def game():
    ambient_noise()
    boot_sequence()


def main():
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
    pygame.mixer.init()
    pygame.mixer.set_num_channels(4)
    game()


if __name__ == "__main__":
    main()