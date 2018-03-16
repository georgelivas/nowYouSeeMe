import socket


class Colors:
    PINK = '\033[90.5m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[90.5m'
    ENDC = '\033[0m'
    BOLD = '\033[0.5m'
    UNDERLINE = '\033[4m'
    Red = '\033[91m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Grey = '\033[90m'
    Black = '\033[90m'
    Default = '\033[99m'


print(Colors.Cyan + "                            .-`")
print("                             `-/sssso/.")
print("                          .:+ssso+/+ssso+:.")
print("                      `.:oooo+:.`   `-/+oooo/-`")
print("                   `-/oooo/-`           `-/+ooo+:.")
print("                .:+ooo+:-`                 `.:/oooo/-.")
print("            `-/osso+:.                         `-/+osoo/-`")
print("          :ossso/-`            ```...```          `.:+osss+-")
print("          oss+.`        `.-:+oooossssssoo+/:.`        `-+syo")
print("          oss:       .-+osso+/::-------:/+osso+/.`      /sso")
print("          oss:    `-+oso/-..--:///+++//:.```.:+oo+/.    :ss+")
print("          oso:  `:+o+:..-/+ooo++//::://+o+/.   `-/oo/-  :os+")
print("          oso:`-+o+-`-+osooo+/-``     ``-/oo/`    `:++/.:os+")
print("          ooo//++-`:osso/oo+-`           `:oo+`     `:+++oo+")
print("          oooo+:`-+ss+-`/oo:               :os/      `:+ooo+")
print("          oooo:`/oo+.   ooo`               `oss     -++-+oo+")
print("          oso/ `/oo+.   ooo`               `oss   ./o+/`:os+")
print("          oso:   -+os+-`/so/               /ss/`-+oo+-  :os+")
print("          oso:    `-+oso+/+o:`           `/oo+/oso+-`   :ss+")
print("          oss:       ./osso++/.``     ``-/+oosso/.      :ss+")
print("          oss/`        `.:ossssoo+++++oossso+:.`       `/sso")
print("          +ssso/-`         `.-:/++ooo++/:-.`        `-/osss+")
print("           .:+ssso/-`                           `.:+osso+-.")
print("              `-/oooo+:.`                    `-/oooo+:.")
print("                  .:+ooo+/-`             `-:+ooo+/-`")
print("                     `-/oooo+:.       .:+oooo/-`")
print("                         .:+osoo/-.:/oooo+:.")
print("                            `-+sssssso/-`")
print("                               `-/+:.      ")


print("\n\n _   _                __   __            _____            ___  ___    ")
print("| \ | |               \ \ / /           /  ___|           |  \/  |     ")
print("|  \| | _____      __  \ V /___  _   _  \ `--.  ___  ___  | .  . | ___ ")
print("| . ` |/ _ \ \ /\ / /   \ // _ \| | | |  `--. \/ _ \/ _ \ | |\/| |/ _ \\")
print("| |\  | (_) \ V  V /    | | (_) | |_| | /\__/ /  __/  __/ | |  | |  __/")
print("\_| \_/\___/ \_/\_/     \_/\___/ \__,_| \____/ \___|\___| \_|  |_/\___|\n\n\n")


def can_you_see(url):
    try:
        socket.create_connection((url, 80))
        print(Colors.OKGREEN + "Everything looks good with " + url)

    except OSError:
        pass
        print(Colors.Red + "Something's wrong with " + url)


run = 'y'

while run == 'y':
    can_you_see(input(Colors.OKBLUE + "Enter a URL:"))
    run = input(Colors.Magenta + "wanna go again? [y/n]")
