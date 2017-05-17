def linear_search(A, n, x):
    """
    Use linear search to find a value in an array.
    
    Args:
        A: any array.
        n: the number of elements in A to search through.
        x: the value being searched for.
    Returns:
        the index of an element that is equal to x, or the string "NOT-FOUND"
        to show that x is not in the array.
    """
    i = 0
    index = "NOT-FOUND"
    while i < n:
        if A[i] == x:
            index = i
        i += 1
    return index


def better_linear_search(A, n, x):
    """
    Use optimized linear search to find a value in an array.
    
    Args:
        A: any array.
        n: the number of elements in A to search through.
        x: the value being searched for.
    Returns:
        the index of the first element equal to x, or the string "NOT-FOUND"
        to show that x is not in the array.
    """
    i = 0
    while i < n:
        if A[i] == x:
            return i
        i += 1
    return "NOT-FOUND"


def sentinel_linear_search(A, n, x):
    """
    Use optimized linear search with a sentinel to find a value in an array.

    Args:
        A: any array.
        n: the number of elements in A to search through.
        x: the value being searched for.
    Returns:
        the index of the first element equal to x, or the string "NOT-FOUND"
        to show that x is not in the array.
    """
    last = A[n-1]
    A[n-1] = x
    i = 0
    while A[i] != x:
        i += 1
    A[n-1] = last
    if i < n-1 or A[n-1] == x:
        return i
    return "NOT-FOUND"


def factorial(n):
    """
    Use recursion to compute the factorial of a non-negative integer

    Args:
        n: an integer greater than or equal to 0 to compute the factorial of
    Returns:
        the value of n! (n-factorial)
    """
    if n == 0:
        return 1
    return n * factorial(n-1)


