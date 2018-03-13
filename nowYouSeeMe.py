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


print(Colors.Cyan + "                                             `:+ss/-`                                           ")
print("                                          ./osssssssso:.               ")
print("                                      `-+ssssssssssssssss+-`")
print("                                   .:+ssssssso+:..:+ooossssso/-`")
print("                               `-/oosoooooo/-`      `-/+oooooooo+:.")
print("                            .:+oooooooo+:.              .-/ooooooooo/-`")
print("                        `-/oooooooo+/-`                    `.:+oooooooo+:.`")
print("                     .:+oooooooo+:.`                           `-:+oooooooo+:.")
print("                `-/oosooooo+/-`                                   .-/+ooooosoo/-`")
print("              .:+osssoooo+:.`                                         `.:+oooosssso/-`")
print("          `./ossssssoo/:.                                                 `-/+oossssss+:.")
print("        .+ssyssssso/-`                          `````                        `.:+osssssyso/`")
print("        -yyysss+:.`                  `..-:/++ooooooooooo++/:-..`                 `-/osssyyy.")
print("        -yysss.                 `.:/oosssssssssssssssssssssssssoo/:.`               `-sssyy.")
print("        -yssss`             `.:+osssssssoo+//::-------:://+oossssssso+:.`            .ssssy.")
print("        -sssss`          `-/osssssso+:-```  ``........``   ```-:+ossssso+/-`         .sssss.")
print("        -sssso`        ./+osssso/-`` `..://+++++++oo+++++/:.`    ``-/+sssoo+/.       .ossss.")
print("        -sssoo`     `-+oooso+:.` `.:++ooooo++++++++++++++ooo+/-`     ``:+ooooo/-`    .oosss.")
print("        -sssoo`   `-+oooo+:`  .:+oooooooo++++/:-.....--:/++oooo+-`       `:+ooo+/-`  .oosss.")
print("        -ssooo`  -/+ooo+-` `:+ssssooooo+++:.`            `-/+oooo+.        `-/oo++/- .oooss.")
print("        -ssooo`./+++o/.  ./oyssssooooo++:`                  ./ooooo:          ./++++/:oooss.")
print("        -ssooo:+++++-  .+ssssso+-+ooo+/.         Now          -+oooo:           -+++++oooss.")
print("        -sooooo+++:` ./osssso:` :oooo+`                        .oooss.           `:++ooooss.")
print("        -sooooo++- `/ooosso:`  `ooooo.           You            :ooss+          `:--+ooooss.")
print("        -sooooo+. -+ooooo-`    -sooo+                           .oosss         -+++--+oooss.")
print("        -ssooo+. .++oooo.      -sooo/            See            `oosss`      ./o++++.-oooss.")
print("        -ssooo-   -+ooooo:`    -ssoo+                           .ossss     `:ooo++/. .oooss.")
print("        -ssooo`    `:+oooso:`   ossoo-            Me            /ssss/   ./oooo++-`  .oooss.")
print("        -sssoo`      ./ooosss/.`-sssoo.                        :sssss``-+ooooo+:`    .oosss.")
print("        -sssoo`        ./oosssso/:/+ooo-                     `/sso+/:/ossooo+:`      .ossss.")
print("        -sssso`          `:+ossssso/::/+/.`                `-++/:/+ossssoo+-`        .ossss.")
print("        -sssss`             ./osssssss+//:-`             `.-:/+osssssso+:.           .sssss.")
print("        -yssss`               `.:ossssssssso++//:::::///+oosssssssso+:.              .ssssy.")
print("        -yysss/.`                 `-/+osssssssssssssssssssssssso+:.`               `-/sssyy.")
print("        -syysssso/-`                  `.-:/+oosssssssssooo+/-.`                `.:+ossssyys.")
print("         -/ossssssso/:`                       `````````                     `-/+ossssssso:.")
print("            .:+sssssooo+:.`                                             `.:/oooosssso/-`")
print("               `-/osssoooo+/-`                                       `-/+ooooosso+:.")
print("                   .:+osoooooo+:.                                `.:+oooooooo+:.`")
print("                      `-/oooooooo+/-`                         .:/+oooooooo/-`")
print("                          .:+oooooooo/:.                  `-/+oooooooo/-.")
print("                             `-/oooooooo+/-`          `-:+oooooooo+:.")
print("                                 .:+ossooooo+:.    .:+ooooooooo/-`")
print("                                    `-+ossssssso//ossssssss+:.")
print("                                        ./osssssssssssso/-")
print("                                           .:+syyyys+:`")
print("                                              `-//.`     ")


def can_you_see(url):
    try:
        socket.create_connection((url, 80))
        print(Colors.OKGREEN + "Everything looks good with " + url)

    except OSError:
        pass
        print(Colors.Red + "Something's wrong with " + url)


can_you_see(input(Colors.OKBLUE + "Enter an URL:"))
