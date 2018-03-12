import socket





def is_connected(url):
    try:
        socket.create_connection((url, 80))
        return True
    except OSError:
        pass
    return False


print(is_connected("google.com"))

