def find_smallest(arr):
    smallest, idx_smallest = arr[0], 0

    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest, idx_smallest = arr[i], i
    
    return idx_smallest


def selection_sort(arr):
    """
        Selection Sort - we are sorting the array.
        In the sample below, we are sorting from the smallest to largest.
        
        The algorithm consists in check the array of elements finding the smallest value,
        adding in a new array and removing from the existing one.
        This will repeat `n` times, since we need to check all the elements in the array,
        for all the elements.
        That means, we need to check `n` elements, `n` times.

        Complexity: O(n²)

        Obs.: As you can see, I created the find_smallest isolated function
        helping the reading of the code (and coz the sources did kinda the same 
        and I thought it's better), but some algorithms will bem all together.
    """
    sorted_arr = []

    for i in range(len(arr)):
        smallest_idx = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest_idx)) # pop removes the index from array and return the element
        
    return sorted_arr

print(selection_sort([4, 8, 12, 9, 3, 67, 5, 75])) # [3, 4, 5, 8, 9, 12, 67, 75]