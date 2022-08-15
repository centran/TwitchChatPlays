from collections import Counter
import time
import keyboard
import mouse

from twitchio.ext import commands, routines
from configFile import TwitchAppCreds

from gta_controls import gameCommands
#from pokemon_controls import gameCommands


commandDelay = 5.0
stopStartKey = 'f6'
global commandsFromChat
commandsFromChat = {}
global running
running = False


class Bot(commands.Bot):
    def __init__(self):
        """Initialise our Bot

        Auths with Token,
        Sets prefex char (if using commands),
        List of channels to monitor.
        """
        super().__init__(
            token=TwitchAppCreds.APP_TOKEN,
            prefix='!',
            initial_channels=[TwitchAppCreds.CHANNEL]
        )

    async def event_ready(self):
        """This function is a coroutine.

        Event called when bot is logged in and ready
        """
        print(f'Logged in as | {self.nick} ({self.user_id})')

    async def event_message(self, message):
        """This function is a coroutine

        Event called when a chat message is received
        """
        # ignore ping/pong message
        if message.echo:
            return

        # check if chat message is in the commands list
        for k, v in gameCommands.COMMAND_LIST.items():
            if message.content.lower() in v['alias']:
                commandsFromChat[message.author.id] = k

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)


# can add chatbot commands if needed
#    @commands.command()
#    async def hello(self, ctx: commands.Context):
#        await ctx.send(f'Hello {ctx.author.name}!')


@routines.routine(seconds=commandDelay)
async def tally_commands():
    """Check for winning command

    Routine which calculates to most chat'ed command
    """
    global commandsFromChat
    command_list = Counter(commandsFromChat.values()).most_common(1)
    command = command_list
    print(
        str(len(commandsFromChat)) +
        " people voted for commands."
    )
    if len(command) > 0:
        print(
            command[0][0] + ' - won with ' +
            str(command[0][1]) + ' votes'
        )
        #message = commands.Context    
        run_command(command[0][0])
    commandsFromChat = {}


def run_command(command):
    """Runs the winning command

    Sends keypress/mouse to virutal keyboard.
    """
    # Set keypress delay less then command delay
    if gameCommands.COMMAND_LIST[command]['duration'] >= commandDelay:
        delay = commandDelay - 0.1
    else:
        delay = gameCommands.COMMAND_LIST[command]['duration']

    # Mouse commands
    # https://github.com/boppreh/mouse
    if gameCommands.COMMAND_LIST[command]['keyboard'][0] == 'mouse':
        mouse.press(button=gameCommands.COMMAND_LIST[command]['keyboard'][1])
        time.sleep(delay)
        mouse.release(button=gameCommands.COMMAND_LIST[command]['keyboard'][1])
    # Keyboard commands
    # https://github.com/boppreh/keyboard#api
    else:
        # Multi-key keyboard presses
        if len(gameCommands.COMMAND_LIST[command]['keyboard']) > 1:
            # Press the keys in list
            for x in gameCommands.COMMAND_LIST[command]['keyboard']:
                print(x)
                keyboard.press(x)

            time.sleep(delay)

            # Release the keys in list
            for x in reversed(gameCommands.COMMAND_LIST[command]['keyboard']):
                print(x)
                keyboard.release(x)
        # Single key press
        else:
            keyboard.press(gameCommands.COMMAND_LIST[command]['keyboard'][0])
            time.sleep(delay)
            keyboard.release(gameCommands.COMMAND_LIST[command]['keyboard'][0])


def startProgram(bot):
    global running
    if running:
        print(f"STOPing - Press {stopStartKey} to resume or ctrl+c to quit")
        tally_commands.stop()
        running = False
    else:
        running = True
        print(f"STARTing with {commandDelay} second delay between actions")
        tally_commands.start()


bot = Bot()
keyboard.add_hotkey(stopStartKey, lambda: startProgram(bot))
print(f"Waiting... press {stopStartKey} to start. (will also stop once started)")
bot.run()
