"""
Given an array of integers, return a new array such that each element 
at index i of the new array is the product of all the numbers in the 
original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output 
would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the 
expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def main():
    assert get_product_array([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert get_product_array([3, 2, 1]) == [2, 3, 6]
    assert get_product_array([]) == []
    assert get_product_array([3, 0, 1]) == [0, 3, 0]
    print(get_product_array([3, 0, 1, 0]))
    assert get_product_array([3, 0, 1, 0]) == [0, 0, 0, 0]

def get_product_array(input: list) -> list:
    total_product = 1
    zero_count = 0
    zero_index = None
    for i, n in enumerate(input):
        if n == 0:
            zero_count += 1
            zero_index = i
            if zero_count >= 2:
                return [0] * len(input)
            continue      
        total_product *= n
    
    product_array = []
    if zero_count == 1:
        product_array = [0] * len(input)
        product_array[zero_index] = total_product
        return product_array

    for n in input:
        if n == 0:
            product_array.append(0)
        else:
            product_array.append(total_product / n)
    return product_array

if __name__ == "__main__":
    main()