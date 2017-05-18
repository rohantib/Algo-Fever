def binary_search(A, n, x):
    """
    Use binary search to find a value in a sorted array.
    
    Args:
        A: any sorted array.
        n: the number of elements in A to search through.
        x: the value being searched for.
    Returns:
        the index of an element that is equal to x (zero-based), or the string "NOT-FOUND"
        to show that x is not in the array.
    """
    p = 0
    r = n - 1
    while p <= r:
        q = (p + r) // 2
        if A[q] == x:
            return q
        elif A[q] > x:
            r = q - 1
        elif A[q] < x:
            p = q + 1
    return "NOT-FOUND"

