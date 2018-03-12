# nowYouSeeMe
A CLI tool to check if a site is up or down


```python
import socket

def is_connected(url):
    try:
        socket.create_connection((url, 80))
        print(Colors.OKGREEN + "Everything looks good with " + url)

    except OSError:
        pass
        print(Colors.Red + "Something's wrong with " + url)


is_connected(input(Colors.OKBLUE + "Enter an URL:"))
```