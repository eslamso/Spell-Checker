
def selection_sort(alist,n):
    """The list is arranged in order of the highest in the percentage of similarity
    and returns only the highest 5 suggestions without the percentage
    """

    list_words = []
    for i in range(n):
        max = alist[i][0]
        maxposition = i
        for j in range(i + 1, len(alist)):
            if alist[j][0] > max:
                max = alist[j][0]
                maxposition = j
        alist[maxposition], alist[i] = alist[i], alist[maxposition]
        list_words.append(alist[i][1])
    return list_words[:n]
#l=[(1,'a'),(2,'b'),(3,'c'),(4,"d"),(5,'e'),(6,'f'),(7,'g')]
#n=int(input('enter the number of words you want to be suggested'))
#print(selection_sort(l,n))
