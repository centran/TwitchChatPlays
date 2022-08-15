class gameCommands:
    START_MSG = "Time to play some GTA... Chat, you're in control"
    COMMAND_LIST = {
        # Name of action to perform
        "Walk": {
            # chat commands. must match lowercase exactly
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
            "keyboard": ['a'],
            "duration": 5
        },
        "Right": {
            "alias": ["d", "right"],
            "keyboard": ['d'],
            "duration": 5
        },
        "Back": {
            "alias": ["s", "back", "backward"],
            "keyboard": ['s'],
            "duration": 5
        },
        "Inventory1": {
            "alias": ["inv1", "inv 1", "inventory 1"],
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
    }
