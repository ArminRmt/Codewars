
# solution 1

def move_zeros(lst):

    num = lst.count(0)
    list1 = [i for i in lst if i != 0]
    for i in range(num):
        list1.append(0)

    return list1


# solution 2


def move_zeros(array):
    return [x for x in array if x] + [0]*array.count(0)

# Any expression after an 'if' is evaluated as a bool.
# If x is an integer, then null is False and any other value is True.
# So [x for x in A if x] means 'filter out any null value'.


# solution 3

def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)

# OR


def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and type(x) is not bool)
