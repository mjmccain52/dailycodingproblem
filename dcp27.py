"""
Given a string of round, curly, and square open and closing brackets, 
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""


def test_1(): assert is_balanced("([])[]({})")
def test_2(): assert not is_balanced("([)]")
def test_3(): assert not is_balanced("((()")

def is_balanced(bracket_str: str) -> bool:
    stack = []
    balancers = {
        "}": "{", 
        ")": "(", 
        "]": "["
    }
    for ch in bracket_str:
        if ch in balancers.values():
            stack.append(ch)
        elif len(stack) == 0 or stack.pop() != balancers[ch]:
            return False
    if len(stack) > 0:
        return False

    return True
