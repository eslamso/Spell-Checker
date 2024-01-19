from read_dictionary import dictionary
def add_word(alist,item):

            first = 0
            last = len(alist) - 1
            position=0
            while first <= last:
                midpoint = (first + last) // 2
                if alist[midpoint] == item:
                    position=midpoint
                    return position
                else:
                    if item < alist[midpoint]:  # compare the first with first and the second with second (a<z)
                        last = midpoint - 1
                    else:
                        first = midpoint + 1
                    if first==last :
                        if alist[first]<item:
                            return first+1
                        else:
                            return first

def write_file(path='edit.txt'):
    l=dictionary()
    x=input('the word you want to be added in dictionary: ')
    index=add_word(l,x)
    l.insert(index,x)
    with open(path,'w') as path:
        for i in range(len(l)):
            path.write(l[i])
            path.write('\n')


write_file()