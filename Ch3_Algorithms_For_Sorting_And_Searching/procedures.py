def linear_search(A, n, x):
    """
    Use linear search to find a value in an array.
    
    Args:
        A: any array.
        n: the number of elements in A to search through.
        x: the value being searched for.
    Returns:
        the index of an element that is equal to x (zero-based), or the string "NOT-FOUND"
        to show that x is not in the array.
    """
    i = 0
    index = "NOT-FOUND"
    while i < n:
        if A[i] == x:
            index = i
        i += 1
    return index

