# nowYouSeeMe
A CLI tool writen in Python to check if a site is up or down. 

## System requirements
* Python > ``3.1``
* unix terminal (i.e. ``bash``)

## Installation
Open a ```Terminal```

```javascript
~ ❯❯❯ git clone https://github.com/georgelivas/nowYouSeeMe
~ ❯❯❯ cd nowYouSeeMe/
~/nowYouSeeMe ❯❯❯ sh nysm.sh
```
## Code

```python
import socket

def can_you_see(url):
    try:
        socket.create_connection((url, 80))
        print(Colors.OKGREEN + "Everything looks good with " + url)

    except OSError:
        pass
        print(Colors.Red + "Something's wrong with " + url)


can_you_see(input(Colors.OKBLUE + "Enter an URL:"))
```

> I am developing this project in order to learn python. More features will come soon.

## You may also like

| Project | Description |
|---------|-------------|
| [CodeGen](https://github.com/georgelivas/CodeGen) | A Java indenter for the 21st century. |
| [Codyfier](https://github.com/georgelivas/Codyfier) | A lightweight, secure, and cross-platform, password generator. |

## Licence
This project is licensed under the MIT License - see the [LICENSE](https://github.com/giorgoslivas/Codyfier/blob/master/LICENSE) file for details