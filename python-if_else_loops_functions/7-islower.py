#!/usr/bin/python3
def islower(c):
    """Vérifie si un caractère est en minuscule."""
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
