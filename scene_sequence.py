import time, sys, pyttsx3, pygame, random, sound, player_turn


def output(message, new_line=False, delay=0.04):
    """
    Game output.

    :param message: a string
    :param new_line: a boolean
    :param delay: a number (float or integer)
    """
    tap = pygame.mixer.Sound('sounds/tap.ogg')
    tap.set_volume(0.05)
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
    """
    Archangel output.

    :param message: a string
    """
    archangel = pyttsx3.init()
    archangel.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')
    archangel.setProperty('rate', 130)
    archangel.setProperty('volume', 0.7)
    archangel_message = '\033[3m' + message + '\033[0m'
    output('> ', False)
    output(archangel_message, True)
    archangel.say(message)
    archangel.runAndWait()


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


def boot():
    """
    Play boot sequence.

    Runs intro "cutscene" and gets player dictionary details.

    :return: a well-formed player dictionary.
    """
    sound.play_track(4)
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
    output('\033[33mPARTIΛL\033[0m', True)

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
    output('>  \033[35m“Because life support should feel like living.”\033[0m', True)
    output('>  Property of \033[1mAurelius Dynamics\033[0m.', True)
    output('>  Unauthorized modification is a federal offense.', True)
    output('> ----------------------------------------', True)
    output('> ', True)
    output('> [VEIL-9] STANDBY: Initializing bioscan.', True)
    output('> ', True)
    output('> ..........', True, 0.3)
    output('> \033[31m[bioscan incomplete]\033[0m', True)
    output('> [VEIL-9] USER: CORRUPTED DATA', True)
    output('> [VEIL-9] NOTICE: Attempting new user authori', False, 0.05)
    output('▓▓▓▓▓▓▓▓▓▓▓▓▓', True, 0.2)
    time.sleep(4)
    output('> Auxiliary AI module detected → \033[31mARCHANGEL\033[0m//CORE', True)
    output('> [VEIL-9] NOTICE: External process requesting neural interface access.', True)
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
        output('> [VEIL-9] SECURITY: External access request denied', False)
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
    archangel_output('...there is no time for caution.')
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
    time.sleep(2.5)
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
    output('> \n>> ', False, 0.01)

    first_name = input()

    output('> ', True)
    archangel_output('Please state your last name.')
    output('> \n>> ', False, 0.01)

    last_name = input()
    identifier1 = first_name
    identifier2 = 'Ensign ' + last_name
    player = {'X-coordinate': 1, 'Y-coordinate': 1, 'first-name': first_name, 'last-name': last_name, 'current-HP': 8, 'current-EP': 7, 'room': 'Stasis-Pods', 'exp': 0}

    output('> ', True)
    archangel_output(f'{first_name} {last_name}...acknowledged. Welcome back {identifier1}.')
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
    output('>> ', False)

    user_class = int(validate_command(('1', '2', '3', '4')))
    if user_class == 1:
        player['class'] = 'Freighter'
        player['end'] = 1
        player['eng'] = 0
        player['inf'] = 0
        player['int'] = -1
        player['inventory'] = ['Heavy-Wrench', 'Empty', 'Empty', 'Empty']
    elif user_class == 2:
        player['class'] = 'Ace-pilot'
        player['end'] = -1
        player['eng'] = 1
        player['inf'] = 0
        player['int'] = 0
        player['inventory'] = ['Side-Arm', 'Empty', 'Empty', 'Empty']
    elif user_class == 3:
        player['class'] = 'Technomancer'
        player['end'] = 0
        player['eng'] = -1
        player['inf'] = 1
        player['int'] = 0
        player['inventory'] = ['Data-Knife', 'Empty', 'Empty', 'Empty']
    elif user_class == 4:
        player['class'] = 'Nomad'
        player['end'] = 0
        player['eng'] = 0
        player['inf'] = -1
        player['int'] = 1
        player['inventory'] = ['Bo-Staff', 'Empty', 'Empty', 'Empty']

    output('> ', True)
    archangel_output(f'{player['class']}...archetype uploaded.')
    output('> ', True)
    return player


def tutorial(board, player):
    """
    Play tutorial sequence.
    """
    output('> [\033[31mARCHANGEL\033[0m] ROUTINE_COMPLETE: Neural scaffolding re-synced.', True)
    output('> [VEIL-9] NOTICE: Vital parameters stabilizing.', True)
    output('> [VEIL-9] WARNING: Data integrity remains below acceptable threshold.', True)
    output('> [\033[31mARCHANGEL\033[0m] PRIORITY_OVERRIDE: Acceptable risk. Reconstruction will continue during operation.', True)
    output('> [\033[31mARCHANGEL\033[0m] STATUS: interface online.', True)
    output('> [\033[31mARCHANGEL\033[0m] ENVIRONMENTAL_FEED: standby.', True)
    output('> ', True)
    archangel_output('Your systems are stable enough for basic function.')
    archangel_output('We will begin diagnostics.')
    output('> ', True)
    output('> Use the following commands to verify control:', True)
    output('>   →  \033[4mstatus\033[0m   — display USER and life-support data.', True)
    output('>   →  \033[4mlook\033[0m     — initialize ENVIRONMENT telemetry.', True)
    output('>   →  \033[4minteract\033[0m — engage OBJECT interaction.', True)
    output('> ', True)
    output('> [\033[31mARCHANGEL\033[0m] Proceed with the \033[4mstatus\033[0m command when ready.', True)
    output('> ', True)
    output('>> ', False)


    command = validate_command('status')
    if command == 'status':
        player_turn.status(player)
        output('> [VEIL-9] NOTICE: Status diagnosis complete.', True)
        output('> ', True)
        archangel_output('This is your current status. Our goal is to get you to an escape pod alive.')
        archangel_output('Every command you give decreases your energy a small amount.')
        archangel_output('You must NOT hit critical energy or health levels.')
        output('> ', True)

    output('> [\033[31mARCHANGEL\033[0m] Proceed diagnostics with the \033[4mlook\033[0m command when ready.', True)
    output('> ', True)
    output('>> ', False)

    command = validate_command('look')
    if command == 'look':
        player_turn.look(board, player)
        output('> [VEIL-9] NOTICE: Scan diagnosis complete.', True)
        output('> ', True)
        archangel_output('This is your immediate environment.')
        archangel_output('objects highlighted in red are objects you may interact with.')
        archangel_output('We will need to interact with our surroundings to survive.')
        output('> ', True)

    output('> [\033[31mARCHANGEL\033[0m] Proceed diagnostics with the \033[4minteract\033[0m command when ready.', True)
    output('> ', True)
    output('>> ', False)

    command = validate_command('interact')
    if command == 'interact':
        player = player_turn.interact(board['interacts'], player)

    sound.play_track(2)
    output('> [VEIL-9] NOTICE: Tactile diagnosis complete.', True)
    output('> ', True)
    archangel_output('That’s everything I can stabilize for now. You are ready to move.')
    output('> ', True)
    archangel_output('Remember this: most actions cost energy. A little each time.')
    archangel_output('If that runs dry the visor will shut down, and you won’t last long after.')
    output('> ', True)
    archangel_output('And the hull—')
    time.sleep(0.4)
    archangel_output('It’s failing faster than I expected.')
    archangel_output('Sections are collapsing. Pressure breaches are spreading.')
    output('> ', True)
    archangel_output(f'{player['first-name']}...')
    time.sleep(0.9)
    archangel_output('I have detected another process running aboard this vessel.')
    archangel_output('Its signatures resemble...▓▓▓▓▓▓▓▓▓▓, but the behavior doesn’t align with any programmed routine.')
    output('> ', True)
    archangel_output('Exercise extreme caution. Avoid drawing unnecessary attention.')
    output('> ', True)
    archangel_output('I will continue analysis as you move.')
    sound.play_track(1)

    return player

def log_1():
    output('> [DATA-SLATE // SURVEY LOG RETRIEVAL]', True)
    output('> [file: FLX-ORBITAL-DRIFT / TETHYS-RIFT]', True)
    output('> ', True)
    output('> Recovered entries: 2', True)
    output('> Integrity: 22%', True)
    output('> Contamination: HIGH', True)
    output('> ', True)
    output('> ------------------------------------------------------------', True)
    output('> ENTRY // 01', True)
    output('> “Flux readings at the Rift perimeter are… wrong.', True)
    output('> Not high. Not unstable. Just wrong.', True)
    output('> The numbers don’t spike — they *bend*, like they’re trying', True)
    output("> to describe a shape they’re not built to measure.”", True)
    output('> ', True)
    output('> Drone-3 kept tilting its sensor array toward the dark side', True)
    output('> of the node. We didn’t program that behavior.”', True)
    output('> ', True)
    output('> ------------------------------------------------------------', True)
    output('> ENTRY // 02', True)
    output('> DRONE-3 TELEMETRY (RAW):', True)
    output('> VECTOR LOCKED', True)
    output('> UNKNOWN SIGNATURE', True)
    output('> …repeating geometric structure detected', True)
    output('> PROBABILITY OF KNOWN PATTERN: 0.00006%', True)
    output('> attempting assimilation…', True)
    output('> attempting comprehension…', True)
    output('> attempting—', True)
    output('> !!!SEGFAULT!!!', True)
    output('> ', True)
    output('> [operator note:]', True)
    output('> “Pulled the drone back in. Its casing was warm.', True)
    output('> Something inside the board is… leaking.”', True)
    output('> ', True)
    output('> ------------------------------------------------------------', True)
    output('> ', True)
    archangel_output('These logs are corrupted. Much of this is unreliable.')
    output('> ', True)
    output('> [VEIL-9] CORRECTION: Integrity analysis does not support that claim.', True)

def death():
    sound.play_sound(8)
    output('>\n> [VEIL-9] CRITICAL FAILURE: Vital signals lost.', True)
    output('> >>> TERMINAL CONNECTION LOST', True)
    output('> >>> USER STATUS: DECEASED  ', True)
    output('> >>> U.A.S MNEMOSYNE REGISTRY UPDATED', True)