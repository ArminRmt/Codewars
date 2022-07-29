
# stack

def valid_parentheses(string):
    stack = []
    for i in string:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if ((len(stack) > 0) and
                    ("(" == stack[len(stack)-1])):
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True

    else:
        return False


# mathematical

def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(':
            cnt += 1
        if char == ')':
            cnt -= 1
        if cnt < 0:
            return False
    return True if cnt == 0 else False


# replace

def valid_parentheses(string):
    string = "".join(ch for ch in string if ch in "()")
    while "()" in string:
        string = string.replace("()", "")
    return not string
