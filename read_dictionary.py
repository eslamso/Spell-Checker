def dictionary(path='Dictionary.txt'):
    """ open the dictionary and read it and return list of its words
    """
    with open(path, 'r') as path:
        return path.read().split()
