#Valid Parentheses
from re import S


s = "([{}])"

def isValid(s):

    if len(s) % 2 != 0:
        return False

    dict = {'(' : ')', '[' : ']', '{' : '}'}
    stack = []

    for i in s:
        if i in dict.keys():
            stack.append(i)
        else:
            if stack == []:
                return False
            a = stack.pop()
            if i!= dict[a]:
                return False
    return stack == []

print(isValid(s))