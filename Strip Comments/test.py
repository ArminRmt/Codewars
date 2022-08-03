
# solution 1

def strip_comments(strng, markers):
    return strip_comments2(strng, markers)


def strip_comments2(strng, markers):
    for x in strng.split('\n'):
        list1 = []
        index = []
        for marker in markers:
            list1.append(x.find(marker))

        index = [i for i in list1 if i > 0]

        if len(index) > 0:
            print(x[:min(index)].rstrip())
        else:
            print(x.rstrip())


# solution 2

def solution(string, markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)


# solution 3

def strip_line(line, markers):
    for m in markers:
        if m in line:
            line = line[:line.index(m)]
    return line.rstrip()


def solution(string, markers):
    stripped = [strip_line(l, markers) for l in string.splitlines()]
    return '\n'.join(stripped)


# solution 4

# import itertools as it
# from string import whitespace

def solution(string, markers):
    def inner():
        for line in string.split('\n'):
            yield ''.join(it.takewhile(lambda char: char not in markers, line)).rstrip(whitespace)
    return '\n'.join(inner())
