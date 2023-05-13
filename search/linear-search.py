def linear_search(expected_value, llist):
    """
        Linear search - we are looking for a value inside a list.
        If we find the value, return its position/index.
        If we didn't find the value, return `None`.

        The algorithm consists in look into each elemento inside the list until find the correct element.

        Complexity: O(n)
    """
    for idx, val in enumerate(llist):
        if expected_value == val:
            return idx
    return None


# Checking
list_of_values = [5, 7, 12, 15, 23, 33, 35, 44, 65, 68, 78, 122, 465]

print(linear_search(78, list_of_values))    # 10
print(linear_search(5, list_of_values))     # 0
print(linear_search(23, list_of_values))    # 4
print(linear_search(465, list_of_values))   # 12
print(linear_search(2000, list_of_values))  # None