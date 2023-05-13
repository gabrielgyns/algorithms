def binary_search(expected_value, llist):
    """
        Binary search - we are looking for a value inside a list.
        If we find the value, return its position/index.
        If we didn't find the value, return `None`.

        The algorithm consists in track the lowest and highest position/index and check if the middle value matches our `expected_value`.
        We update the `low` and `high` variables as needed.  

        Complexity: O(log n)
    """
    low = 0
    high = len(llist) - 1
    
    while low <= high:
        mid = (high + low) // 2
        mid_value = llist[mid]

        if expected_value == mid_value:
            return mid
        
        if expected_value > mid_value:
            low = mid + 1
        else:
            high = mid - 1
    return None


# Checking
list_of_values = [5, 7, 12, 15, 23, 33, 35, 44, 65, 68, 78, 122, 465]

print(binary_search(78, list_of_values))    # 10
print(binary_search(5, list_of_values))     # 0
print(binary_search(23, list_of_values))    # 4
print(binary_search(465, list_of_values))   # 12
print(binary_search(2000, list_of_values))  # None