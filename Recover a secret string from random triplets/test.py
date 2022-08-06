
def recoverSecret(triplets):
    secret = ''
    secret_dict = {}
    # any better way to build a dictionary based on relationship of triplets?
    for x in triplets:
        for y in x:
            secret_dict.setdefault(y, set()).update(
                x[x.index(y) - 1]) if x.index(y) != 0 else secret_dict.setdefault(y, set())

    def removeChar(c) -> dict:
        '''find first char in secret'''
        # any better way to remove element from set that is value of dictionary when value in set?
        {v.remove(c) for k, v in secret_dict.items() if c in v}

    def findChar() -> str:
        '''find first char in secret when there is no char in front of it'''
        # any better way to find character when value is dictionary is empty?
        return next(k for k, v in secret_dict.items() if not v)

    while secret_dict:
        first_char = findChar()
        # any better way to rebuild dictionary when key == k?
        secret_dict = {k: v for k, v in secret_dict.items() if k != first_char}
        removeChar(first_char)
        secret = secret + first_char
    return secret


2


def recoverSecret(triplets):
    r = list(set([i for l in triplets for i in l]))
    for l in triplets:
        fix(r, l[1], l[2])
        fix(r, l[0], l[1])
    return ''.join(r)


def fix(l, a, b):
    """let l.index(a) < l.index(b)"""
    if l.index(a) > l.index(b):
        l.remove(a)
        l.insert(l.index(b), a)


3


def recoverSecret(triplets):
    # out =  [(all first letters), (all second), (all third)]
    out = list(zip(*triplets))

    # first letter of secret in a list
    first = list(set(out[0])-set(out[1]+out[2]))

    # delete first letter from triplets
    for triplet in triplets:
        if triplet[0] in first:
            triplet[:2], triplet[2] = triplet[1:], ''

    # get next letter of secret
    return first[0]+recoverSecret(triplets) if first else ''
