
# solution 1


def alphanumeric(password):
    if password == '':
        return False
    else:
        for s in password.lower():
            if s not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
                         ]:
                return False
    return True


# solution 2

def alphanumeric(string):
    return string.isalnum()


# solution 3

import re

pattern = re.compile('^[0-9a-zA-Z]+$')


def alphanumeric(string):
    return pattern.match(string) is not None

# OR


def alphanumeric(string):
    return bool(re.search(r'^[0-9a-zA-Z]+$', string))


# solution 4

def alphanumeric(password):
    return True if password.isalnum() and False not in {(48 <= ord(i) <= 127)for i in password}else False


# solution 5

import string

def alphanumeric(strng):
    return all(ord(element) > 47 and ord(element) < 58 or element in string.ascii_letters for element in strng)
