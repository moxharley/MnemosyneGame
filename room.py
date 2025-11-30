import sequence, logic, time, sound, player_turn


def make_interaction():

    def data_pad(character):
        sequence.output("> You reach down to the raised platform beside your open cryopod.", True)
        sequence.output("> The data-pad is half-frozen to the metal, its screen shot through with cracks.\n> ", True)
        time.sleep(1)
        sequence.output("> Carefully, you pry it loose. A few dead pixels flake away like ash.\n> ", True)
        sequence.output("> [\033[31mARCHANGEL\033[0m] ANALYSIS: Peripheral device identified — crew-issued data-slate.", True)
        sequence.output("> [\033[31mARCHANGEL\033[0m] STATUS: Housing compromised, memory sectors unstable but potentially recoverable.\n> ", True)
        sequence.output("> Possible actions:", True)
        sequence.output(f">   [1] INTERFACE — Attempt to coax surviving memory sectors online.\n>      [STAT: Interface [{character["inf"]}] | DIFFICULTY: [moderate]]", True)
        sequence.output(f">   [2] ENGAGE — Force the casing open and salvage any intact components.\n>      [STAT: Engage [{character["eng"]}] | DIFFICULTY: [intermediate]]\n> ",    True)
        sequence.output(">> ")
        action = int(sequence.validate_command(("1", "2")))
        if action == 1:
            successful = logic.roll(character["inf"], 3)
            sequence.output("> ", True)
            if successful:
                sound.play_sound(3)
                sequence.output("> [\033[31mARCHANGEL\033[0m] ACTION: Success.\n> ", True)
                sequence.output("> You bridge two exposed contacts and apply careful pressure.", True)
                sound.play_sound(1)
                sequence.output("> The screen buzzes, then stabilizes into a dim, barely functional UI.\n> ", True)
                sequence.output("> [\033[31mARCHANGEL\033[0m] ROUTINE: Bypassing damaged bootloader… partial success.\n> ", True)
                sequence.output("> Fragmented logs materialize — survey notes, flux readings, a reference to something", True)
                sequence.output("> called the “Tethys Rift.”\n> ", True)
                sequence.log_1()
                sequence.output("> [VEIL-9] ENERGY: Energy levels decreased a small amount: ", False)
                character = logic.update("current-EP", character, (-1))
                energy_percent = (character['current-EP'] / 10) * 100
                energy = player_turn.make_bar(character['current-EP'])
                sequence.output(f'{energy} {energy_percent}%\n>', True)
            else:
                sound.play_sound(4)
                sequence.output("> [\033[31mARCHANGEL\033[0m] ACTION: Failure.\n> ", True)
                sequence.output("> You try to bridge the exposed contacts.", True)
                sequence.output("> A pulse of heat flashes across your glove — the pad pops, internally shorting out.\n> ", True)
                sequence.output("> The screen dies completely.\n>", True)
                sequence.output("> [VEIL-9] HEALTH: Health levels decreased a small amount: ")
                character = logic.update("current-HP", character, -1)
                health_percent = (character['current-HP'] / 10) * 100
                health = player_turn.make_bar(character['current-HP'])
                sequence.output(f'{health} {health_percent}%\n>', True)
                character = logic.level_up(character)
        elif action == 2:
            successful = logic.roll(character["eng"], 5)
            sequence.output("> ", True)
            if successful:
                sound.play_sound(3)
                sequence.output("> [\033[31mARCHANGEL\033[0m] ACTION: Success.\n> ", True)
                sequence.output("> You dig your fingers under the casing and twist hard.", True)
                sequence.output("> The brittle housing snaps open with a sharp crack.\n> ", True)
                sequence.output("> Inside, a micro power cell remains intact.\n>", True)
                sequence.output("> [VEIL-9] ENERGY: Energy levels increased a moderate amount: ")
                character = logic.update("current-EP", character, 3)
                energy_percent = (character['current-EP'] / 10) * 100
                energy = player_turn.make_bar(character['current-EP'])
                sequence.output(f'{energy} {energy_percent}%\n>', True)
            else:
                sound.play_sound(4)
                sequence.output("> [\033[31mARCHANGEL\033[0m] ACTION: Failure.\n> ", True)
                sequence.output("> You wrench the casing open — too forcefully. ", True)
                sequence.output("> The frozen plastic explodes in your grip, scattering useless shards.\n> ", True)
                sound.play_sound(2)
                sequence.output("> A few jagged edges bite into your fingertips.\n> ", True)
                sequence.output("> [VEIL-9] HEALTH: Health levels decreased a small amount: ", False)
                character = logic.update("current-HP", character, (-1))
                health_percent = (character['current-HP'] / 10) * 100
                health = player_turn.make_bar(character['current-HP'])
                sequence.output(f'{health} {health_percent}%', True)
                sequence.output("> [VEIL-9] ENERGY: Energy levels decreased a small amount: ", False)
                character = logic.update("current-EP", character, (-1))
                energy_percent = (character['current-EP'] / 10) * 100
                energy = player_turn.make_bar(character['current-EP'])
                sequence.output(f'{energy} {energy_percent}%\n>', True)
                character = logic.level_up(character)
        del has_interact[(1, 1)]
        return character

    def puddle(character):
        pass

    def crate(character):
        pass

    def hatch(character):
        pass

    def interface(character):
        pass

    def door(character):
        pass

    has_interact = {
        (1, 1): data_pad,
        (-1, 6): puddle,
        (1, 7): crate,
        (-5, 2): interface,
        (-4, 0): hatch,
        (-5, -1): door
    }
    return has_interact


def make_board():
    """
    Make board.

    Makes the playable map of the starship.

    :return: a well-formed board dictionary
    """

    board = {
        "goal": (-7, -22),
        (0, 0): ("Cryopod-05 (Scratched) - Deep, uneven gouges mark the inside walls. Some look metallic; others disturbingly biological.", "Stasis-Pods"),
        (1, 0): ("Overhead Conduit - The ceiling panel above is bowed and stained by a dark, dried drip. Something dripped here recently.", "Stasis-Pods"),
        (2, 0): ("Supply Cabinet - A waist-high storage cabinet. Its magnetic \033[34mlock\033[0m flickers weakly, and the metal is dented from the inside.", "Stasis-Pods"),
        (3, 0): ("Cryopod-01 (Fractured) - The viewport glass is shattered inward as though something forced its way inside. Frost spreads in jagged veins.", "Stasis-Pods"),
        (0, 1): ("Cryopod-02 (Offline) - The pod is dark. A faint human-shaped frost imprint remains on the window, but the pod is empty.", "Stasis-Pods"),
        (1, 1): ("Cryopod-03 (Your Pod) - The hatch is hanging sideways. Cracks in the interior ice suggest you thrashed free. A broken \033[31mdata-pad\033[0m lies on the platform.", "Stasis-Pods"),
        (2, 1): ("Terminal A - A flickering stasis control terminal. Lines of corrupted diagnostics scroll by too quickly to read.", "Stasis-Pods"),
        (3, 1): ("Cryopod-04 (Scorched) - The inner surface is warped and blackened by heat. Something inside burned violently before power failed.", "Stasis-Pods"),
        (0, 2): ("Entrance Hatch - The sliding hatch leads out into the hallway. Frost rims its seams, and a faint green exit strip glows beneath your feet.", "Stasis-Pods"),
        (1, 2): ("Cryopod-06 (Coolant Leak) - Coolant pools beneath the pod, unusually dark and viscous. It reeks of warm metal.", "Stasis-Pods"),
        (2, 2): ("Terminal B - A partially frozen backup \033[34mterminal\033[0m. Crew IDs flicker onscreen before dissolving into static.", "Stasis-Pods"),
        (3, 2): ("Drain Pit - A grated floor drain where melted ice gathers. Something metallic clatters deep beneath it when you move nearby.", "Stasis-Pods"),

        (0, 3): ("Corridor Junction - A narrow passage coated in thin frost. Emergency strips along the walls pulse a slow amber.", "Corridor"),
        (0, 4): ("Warped Bulkhead - The corridor bends slightly where the hull has bowed inward. Metal creaks softly with each shift of the ship.", "Corridor"),

        (0, 5): ("Cargo Lift Column - A central freight lift stands dark and unpowered. The railing is bent, as though something heavy struck it from below.", "Loading Bay"),
        (0, 6): ("Suspended Crates - Two cargo containers hang from magnetic hooks above. Their clamps flicker on and off, making the chains sway slightly.", "Loading Bay"),
        (0, 7): ("Forklift Station - A compact cargo-lifter sits dormant, its tines embedded in the floor plating.", "Loading Bay"),
        (-1, 5): ("Overturned Cart - A \033[34msupply cart\033[0m lies on its side. Several sealed nutrient packs are scattered across the floor.", "Loading Bay"),
        (-1, 6): ("Coolant Spill - A shallow \033[31mpuddle\033[0m spreads across the metal grate. It shines with a dark tint, though the coolant itself should not be so dark.", "Loading Bay"),
        (-1, 7): ("Loader Arm - A mechanical loading arm sits retracted, its claws dented and misaligned. Scorch marks climb the wall beside it, like something dragged along the metal.", "Loading Bay"),
        (1, 5): ("Tether Point - A pair of magnetic \033[34mtether lines\033[0m dangle from the ceiling, swaying gently. One line is frayed at the end.", "Loading Bay"),
        (1, 6): ("Wall Console - A freight \033[34mmanifest\033[0m console bolted to the bulkhead. Its screen is completely dark, but a steady clicking comes from inside the casing.", "Loading Bay"),
        (1, 7): ("Cargo Pallet - A heavy pallet sits abandoned mid-transfer. One \033[31mcrate\033[0m bears a painted warning glyph: FLUX HANDLING — DO NOT VIBRATE. Its bolts are partially loosened.", "Loading Bay"),

        (-2, 6): ("Corridor Junction - A smear of something dark drags along the wall at shoulder height, tapering off into shaky fingerprints.", "Corridor"),

        (-3, 6): ("Galley Counter – A serving tray lies overturned, coated with a dark, grainy film that flakes when disturbed.", "Galley"),
        (-4, 6): ("Preparation Table - Stainless surface scored by repeated impacts. A thin, dried reddish-brown film coats one corner in a circular arc.", "Galley"),
        (-5, 6): ("Hydration Unit - The \033[34mdispenser\033[0m's front panel is cracked. Condensed fluid inside has mixed with a particulate contaminant, forming clotted streaks along the drain channel.", "Galley"),
        (-3, 7): ("Serving Alcove - One tray remains, fused to the counter by a residue sample consistent with oxidized biofluid. Fork tines embedded in the wall suggest sudden kinetic force.", "Galley"),
        (-4, 7): ("Cold Storage Hatch - Door left ajar. Interior temperature has failed, allowing organic matter inside to collapse into an unidentifiable slurry coating the lower bins.", "Galley"),
        (-5, 7): ("Floor Drain - The \033[34mgrate\033[0m is obstructed by dried accumulation. Patterning indicates it originated from above rather than the floor level.", "Galley"),

        (-6, 6): ("Sealed Collapse – The route to the Crew Quarters is obstructed by a dense, fused mass of debris. Heat-scoring suggests the collapse occurred under extreme stress.", "Corridor"),

        (-4, 5): ("Ceiling Conduit - A ceiling conduit hangs open here. The interior wiring is stretched taut, as if something pulled it from within rather than from the outside.", "Corridor"),
        (-4, 4): ("Wall Scoring - The portside wall displays a sequence of parallel abrasions. Depth and spacing do not correspond to any maintenance tool recorded in Mnemosyne’s inventory.", "Corridor"),
        (-5, 4): ("Airflow Disturbance - The air in this junction is noticeably colder. VEIL-9 registers a localized pressure fluctuation, source undetermined.", "Corridor"),
        (-5, 3): ("Floor Imprint - A single indentation mars the deck plating. The force required exceeds the load capacity of any standard crew member. No debris accompanies the deformation.", "Corridor"),

        (-5, 2): ("Primary Console - The command \033[31minterface\033[0m is cold and unpowered. Several keys are pressed inward as if held too long.", "Bridge"),
        (-5, 1): ("Captain’s Chair - The restraint harness hangs open. The cushioning is indented, retaining the outline of recent occupation.", "Bridge"),
        (-5, 0): ("Nav-Panel Fragment - A cracked navigation \033[34mscreen\033[0m displays a fixed star-map coordinate that does not match Mnemosyne’s logged position.", "Bridge"),
        (-6, 2): ("Overhead Array — The sensor grid hums intermittently, emitting a low-band pulse inconsistent with any known scan pattern.", "Bridge"),
        (-6, 1): ("Chart Table — A \033[34mholoslate\033[0m lies inert. Finger streaks are visible in the dust, terminating abruptly at the table’s edge.", "Bridge"),
        (-6, 0): ("Auxiliary Station — A headset rests on the console. The audio jack shows heat warping, as though exposed to prolonged static surge.", "Bridge"),
        (-4, 2): ("Status Board — The ship \033[34mschematic\033[0m blinks between intact and fractured hull outlines. Neither version matches current conditions.", "Bridge"),
        (-4, 1): ("Internal Comms Unit — The speaker occasionally emits a soft intake-click, similar to someone preparing to speak but never continuing.", "Bridge"),
        (-4, 0): ("Vent Access Chamber - A recessed maintenance alcove with a square ventilation \033[31mhatch\033[0m secured by worn fasteners. Thin particulate dust drifts from the grille.", "Bridge"),

        (-5, -1): ("Security Bulkhead – A reinforced \033[34mdoor\033[0m marked MAINTENANCE ACCESS. The lock panel is dark, requiring manual power restoration before it can respond.", "Corridor"),
        (-5, -2): ("Inspection Alcove – A recessed area containing a dormant wall terminal. Dried particulate dust coats the screen.", "Corridor"),
        (-5, -3): ("Structural Rib – Ceiling struts narrow overhead, creating a compressed passage. Metallic flecks litter the floor in a thin line.", "Corridor"),
        (-5, -4): ("Pressure Metering Section – A wall-mounted gauge reads zero across multiple channels; its casing is dented but intact.", "Corridor"),
        (-5, -5): ("Corridor Junction – A simple curve leading downward toward maintenance. The air temperature drops perceptibly here.", "Corridor"),
        (-5, -6): ("Service Conduit Run – Wall panels hum faintly; the conduit labels are smeared and unreadable from heat exposure.", "Corridor"),

        (-5, -7): ("Support Struts - Exposed framing lined with frost; vibration hums faintly beneath the floor.", "Maintenance Access"),
        (-5, -8): ("Wiring Trench - A recessed floor channel filled with neatly bundled cables, some warm to the touch.", "Maintenance Access"),
        (-5, -9): ("Anchor Bolts - Heavy bolts securing a plate that has shifted slightly out of alignment.", "Maintenance Access"),
        (-6, -7): ("Coolant Runoff - A straight smear of dried coolant trails toward the lower levels.", "Maintenance Access"),
        (-6, -8): ("Sensor Node - A disabled motion sensor hangs from its mount, lens dark.", "Maintenance Access"),
        (-6, -9): ("Bulkhead Support - Thick reinforcement beams coated in a thin sheen of condensation.", "Maintenance Access"),
        (-4, -7): ("Panel Rack - Rows of closed access panels marked with faded maintenance codes.", "Maintenance Access"),
        (-4, -8): ("Utility Junction - A cluster of conduits merge here; the metal lightly ticks as temperatures shift.", "Maintenance Access"),
        (-4, -9): ("Floor Grate - The grate depresses slightly underfoot; airflow is steady below.", "Maintenance Access"),
        (-3, -7): ("Inspection Ladder - A short ladder leading to a sealed overhead hatch.", "Maintenance Access"),
        (-3, -8): ("Service Outlet - A universal port for diagnostic tools, currently inactive.", "Maintenance Access"),
        (-3, -9): ("Drain Runoff - Clear liquid gathers at the lowest point; no source is visible.", "Maintenance Access"),

        (-4, -10): ("Narrow Junction - The corridor contracts sharply, forcing movement in single file.", "Corridor"),
        (-4, -11): ("Overhead Housing - A loose ceiling panel gently sways with each hull tremor.", "Corridor"),
        (-5, -11): ("Strained Bulkhead - The wall plating is bowed inward from external pressure.", "Corridor"),
        (-6, -11): ("Pipe Array - Low-pressure pipes run along the wall; faint heat radiates from within.", "Corridor"),
        (-6, -12): ("Discolored Wall - A pale streak discolors the plating, origin unknown.", "Corridor"),

        (-6, -13): ("Reactor Perimeter - The shielding here hums softly, pulsing with slow energy cycles.", "Reactor"),
        (-5, -13): ("Reactor Cooling Rails - Parallel rails vent minimal heat; safe levels indicated.", "Reactor"),
        (-6, -14): ("Reactor Core Access - A secured control surface flashes intermittent warnings.", "Reactor"),
        (-5, -14): ("Control Conduit - Thick power conduits run floor-to-ceiling, vibrating faintly.", "Reactor"),

        (-7, -13): ("Outer Corridor - Long metal stretch with no points of interest detected.", "Corridor"),
        (-4, -14): ("Cross Way - Four corridor branches meet at a plain metal junction.", "Corridor"),
        (-6, -15): ("Transition Section - Floor plating changes texture, marking subsystem boundary.", "Corridor"),
        (-6, -16): ("Segment Divider - A narrow brace divides two hull sections; stable.", "Corridor"),

        (-8, -13): ("Signal Rack - Empty mount points for drone uplink modules.", "Relay"),
        (-9, -13): ("Data Spine - A vertical relay housing with low residual charge.", "Relay"),
        (-10, -13): ("Fiber Junction - Dozens of glass lines converge into a sealed hub.", "Relay"),
        (-9, -12): ("Repeater Coil - The coil is warm, maintaining minimal shipwide signal bounce.", "Relay"),
        (-10, -14): ("Relay Crossfeed - Two inactive nodes face each other across the narrow space.", "Relay"),
        (-8, -14): ("EM Shielding - Panels absorb stray electromagnetic output; slightly humming.", "Relay"),
        (-8, -15): ("Diagnostic Plinth - A raised platform for field analyzers, currently offline.", "Relay"),
        (-9, -15): ("Backup Array - Redundant wiring bundles arranged with exact precision.", "Relay"),
        (-10, -15): ("Signal Sink - A terminal used to nullify corrupted transmissions.", "Relay"),

        (-3, -14): ("Tool Bench - A fixed metal bench with empty brackets and tool outlines.", "Utility"),
        (-2, -14): ("Spare Parts Bin - Stacked trays of unused universal fasteners.", "Utility"),
        (-1, -14): ("Access Locker - A locked wall cabinet requiring a generic override.", "Utility"),
        (-3, -13): ("Fluid Reservoir - A sealed tank of coolant mixture at safe pressure.", "Utility"),
        (-2, -13): ("Wiring Spool - Multiple coils of insulated cabling, color-coded.", "Utility"),
        (-1, -13): ("Maintenance Cart - A wheeled cart with its drawers half-open and empty.", "Utility"),

        (-6, -17): ("Fabricator Arm - A large mechanical arm locked mid-motion.", "Fabrication Bay"),
        (-6, -18): ("Print Bed - A flat surface coated in cured polymer dust.", "Fabrication Bay"),
        (-7, -17): ("Assembly Track - The conveyor is frozen; residue clings to its joints.", "Fabrication Bay"),
        (-7, -18): ("Heat Vents - Low warmth radiates despite the system being off.", "Fabrication Bay"),
        (-5, -17): ("Parts Dispenser - Empty \033[34mchutes\033[0m arranged in a grid pattern.", "Fabrication Bay"),
        (-5, -18): ("Calibration Station - A lens flickers with intermittent blue light.", "Fabrication Bay"),
        (-4, -18): ("Inspection Rail - A narrow walkway raised slightly above the main floor.", "Fabrication Bay"),
        (-8, -18): ("Monitor Array - Blank screens arranged like an unblinking wall.", "Fabrication Bay"),
        (-4, -19): ("Auxiliary Feeder - A small mechanical funnel clogged with hardened composite.", "Fabrication Bay"),
        (-8, -19): ("Scrap Containment - A mesh cage full of metallic fragments.", "Fabrication Bay"),
        (-4, -20): ("Cooling Vent - A cold draft flows steadily from beneath the machine floor.", "Fabrication Bay"),
        (-8, -20): ("Pattern Buffer - A \033[31mchamber\033[0m meant for storing fabrication templates.", "Fabrication Bay"),
        (-5, -20): ("Material Hopper - A tall intake column with residue streaking downward.", "Fabrication Bay"),
        (-7, -20): ("Weld Frame - A rigid structure with blackened edges.", "Fabrication Bay"),
        (-6, -20): ("Mold Casting - A sealed mold with unreadable labeling.", "Fabrication Bay"),

        (-7, -21): ("Lower Corridor - Structural strain readings elevated but within tolerance.", "Corridor"),
        (-5, -21): ("Approach Hall - Air density fluctuates briefly without source.", "Corridor"),

        (-7, -22): ("Pod Chamber A - The launch rails emit intermittent static bursts.", "Emergency Pod Bay"),
        (-6, -22): ("Pod Chamber B - Escape pod clamps cycle through diagnostic patterns unscheduled.", "Emergency Pod Bay"),
        (-5, -22): ("Pod Chamber Access - The walkway trembles lightly; pressure variances logged.", "Emergency Pod Bay"),
    }
    return board


def describe_current_location(board, character):
    """
    Describe current location.

    Prints the associated description of the current character location.

    :param board: a dictionary.
    :param character: a dictionary.
    :precondition: board must be a dictionary in the proper format (i.e. {(0, 0): Room,... 'Goal': (1, 1)}.
    :precondition: character must be a dictionary with a "Y-coordinate" and "X-coordinate" key.
    :precondition: character["Y-coordinate"] and character["X-coordinate] must be integers.
    :postcondition: finds the associated description of the character's current location on the board.
    :return: None
    """
    player_coordinate = (character["X-coordinate"], character["Y-coordinate"])
    sequence.output('> ' + str(board[player_coordinate][0]), True, 0.03)