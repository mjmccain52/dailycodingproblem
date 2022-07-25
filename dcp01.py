"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def main():
    assert sum_check([10, 15, 3, 7], 17)
    assert not sum_check([10, 15, 3, 7], 20)
    assert sum_check([10, 15, 10, 7], 20)

def sum_check(numbers: list, k: int) -> bool:
    d = set()
    for n in numbers:
        if k - n in d:
            return True
        if n not in d:
            d.add(n)
        elif n*2 == k:
            return True
    return False
        

if __name__ == "__main__":
    main()