import os
import socket

def check_internet_connection() -> bool:
    state = False
    if not has_link() or not has_default_route():
        state = False
    else:
        state = _socket()

    if not state:
        print("NET: No connection")

    return state

def has_link() -> bool:
    try:
        for iface in os.listdir("/sys/class/net"):
            if iface == "lo":
                continue
            with open(f"/sys/class/net/{iface}/operstate", "r", encoding="utf-8") as file:
                if file.read().strip() == "up":
                    return True
        return False
    except Exception:
        return False

def has_default_route() -> bool:
    try:
        with open("/proc/net/route", "r", encoding="utf-8") as file:
            for line in file.readlines()[1:]:
                fields = line.split()
                if fields[1] == "00000000":
                    return True
        return False
    except Exception:
        return False
        
def _socket() -> bool:
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except OSError as e:
        print(f"NET: Socket error: {e}")
        return False