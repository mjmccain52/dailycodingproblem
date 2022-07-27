"""Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a 
single count and character. For example, the string "AAAABBBCCDAA" 
would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string 
to be encoded have no digits and consists solely of alphabetic 
characters. You can assume the string to be decoded is valid.
"""

def encode(s: str) -> str:
    if not s:
        return s
    current_count = 1
    curr_ch = s[0]
    encoded = ""
    for i in range(1, len(s)):
        if s[i] == curr_ch:
            current_count += 1
        else:
            encoded += f"{current_count}{curr_ch}"
            current_count = 1
            curr_ch = s[i]

    encoded += f"{current_count}{curr_ch}"

    return encoded

def test_1():
    assert encode("AAAABBBCCDAA") == "4A3B2C1D2A"
def test_2():
    assert encode("AAAA") == "4A"
def test_3():
    assert encode("AB") == "1A1B"