def binary_search(alist, item):
    """does binary search and return true if item is exists or false if item doesn't exist """
    first = 0
    last = len(alist) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:  # compare the first with first and the second with second (a<z)
                last = midpoint - 1
            else:
                first = midpoint + 1
    return False
