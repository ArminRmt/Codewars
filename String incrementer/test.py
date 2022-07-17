import re


# first solution

def increment_string(strng):
    head = strng.rstrip('0123456789')  # remove numbers from right
    tail = strng[len(head):]
    if tail == "":
        return strng+"1"
    # add 1 to tail and pad with zeros
    return head + str(int(tail) + 1).zfill(len(tail))


# second solution   !!!!!!

def increment_string(s):
    if s and s[-1].isdigit():
        return increment_string(s[:-1]) + "0" if s[-1] == "9" else s[:-1] + `int(s[-1]) + 1`
    return s + "1"


# third  solution


def increment_string(strng):
    m = re.match('^(.*?)(\d+)$', strng)
    name, num = (m.group(1), m.group(2)) if m else (strng, '0')
    return '{0}{1:0{2}}'.format(name, int(num)+1, len(num))


# forth  solution  without notice of leading zeroes

def result(strng):
    number = [int(s) for s in strng if s.isdigit()]
    int_number = int("".join(str(x) for x in number))
    final_num = str(int_number + 1)
    strng = strng.replace(str(int_number), "")
    return str(strng + final_num)


def increment_string(strng):
    for m in strng[::-1]:
        if m.isdigit():
            print(result(strng))
            break
        else:
            print(strng + '1')
            break
