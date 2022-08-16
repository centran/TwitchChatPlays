class gameCommands:
    START_MSG = "Time to play some GTA... Chat, you're in control"
    COMMAND_LIST = {
        # Name of action to perform
        "Walk": {
            # chat commands. must match these lowercase exactly
            "alias": ['w', 'walk', 'forward'],
            # keyboard key to issue
            "keyboard": ['w'],
            # how long to press down key
            "duration": 5
        },
        "Run": {
            "alias": ['run', 'sprint', 'shift+w'],
            # can press multiple keys
            "keyboard": ['shift', 'w'],
            "duration": 5
        },
        "Left": {
            "alias": ['a', "left"],
            "keyboard": ['a','c'],
            "duration": 1
        },
        "Right": {
            "alias": ["d", "right"],
            "keyboard": ['d','c'],
            "duration": 1
        },
        "Back": {
            "alias": ["s", "back", "backward"],
            "keyboard": ['s'],
            "duration": 5
        },
        "Inventory1": {
            "alias": ["1", "inv1", "inv 1", "inventory 1"],
            "keyboard": ['1'],
            "duration": 0.1
        },
        "Inventory2": {
            "alias": ["2", "inv2", "inv 2", "inventory 2"],
            "keyboard": ['1'],
            "duration": 0.1
        },
        "Inventory3": {
            "alias": ["3", "inv3", "inv 3", "inventory 3"],
            "keyboard": ['1'],
            "duration": 0.1
        },
        "Inventory4": {
            "alias": ["4", "inv4", "inv 4", "inventory 4"],
            "keyboard": ['1'],
            "duration": 0.1
        },
        "LeftClick": {
            "alias": ["click", "left click", "mouse", "left mouse", "shoot"],
            # If first item in list is 'mouse' then will be issued as mouse
            # https://github.com/boppreh/mouse
            "keyboard": ["mouse", "left"],
            "duration": 1
        },
        "Jump": {
            "alias": ["space", "jump"],
            "keyboard": ['space'],
            "duration": 0.1
        },
        "Q": {
            "alias": ["q"],
            "keyboard": ['q'],
            "duration": 0.1
        },
        "f": {
            "alias": ["f"],
            "keyboard": ['f'],
            "duration": 0.1
        },
        "Y": {
            "alias": ["y"],
            "keyboard": ['y'],
            "duration": 0.1
        },
        "i": {
            "alias": ["i"],
            "keyboard": ['i'],
            "duration": 0.1
        },
        "o": {
            "alias": ["o"],
            "keyboard": ['o'],
            "duration": 0.1
        },
        "c": {
            "alias": ["c"],
            "keyboard": ['c'],
            "duration": 0.1
        },
        "f2": {
            "alias": ["f2"],
            "keyboard": ['f2'],
            "duration": 0.1
        },
        "f3": {
            "alias": ["f3"],
            "keyboard": ['f3'],
            "duration": 0.1
        },
        "f5": {
            "alias": ["f5"],
            "keyboard": ['f5'],
            "duration": 0.1
        },
        "f6": {
            "alias": ["f6"],
            "keyboard": ['f6'],
            "duration": 0.1
        },
        "f7": {
            "alias": ["f7"],
            "keyboard": ['f7'],
            "duration": 0.1
        },
        "h": {
            "alias": ["h"],
            "keyboard": ['space'],
            "duration": 0.1
        },
        "Buckle": {
            "alias": ["b", "buckle", "seatbelt", "belt"],
            "keyboard": ['b'],
            "duration": 0.1
        },
        "Select/Horn": {
            "alias": ["e","honk"],
            "keyboard": ['e'],
            "duration": 0.1
        },
    }
