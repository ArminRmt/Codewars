
# Karatsuba Algorithm O(digits^1.58) way faster than n ** p % m  O(digits^2)

def last_digit(n1, n2):
    return pow(n1, n2, 10)


# I noticed empirically that pow(number, x) % 10 == pow(number % 10, x) % 10.
# Also, I noticed that pow(number, x) % 10 == pow(number, x % 4 + 4) % 10, with the exception of x == 0.

# 4 happens to be the least common multiple of the number of times before
# which the same last-digit repeats for each digit between 0 and 9

def last_digit(n1, n2):
    return (n1 % 10) ** (n2 % 4 + 4 * bool(n2)) % 10


# use a dictionary to store the last digit of each reminder

digits = {
    0: [0, 0, 0, 0],
    1: [1, 1, 1, 1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6, 4, 6],
    5: [5, 5, 5, 5],
    6: [6, 6, 6, 6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1, 9, 1]
}


def last_digit(n1, n2):
    return digits[n1 % 10][(n2-1) % 4] if n2 else 1
