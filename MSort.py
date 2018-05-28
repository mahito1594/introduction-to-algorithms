'''
Merge sort
'''

def merge(seq, p, q, r):
    '''
    merge sorted sequence seq[p: q] and seq[q: r]
    where p <= q < r
    '''
    # divide the seqence[p: r] to left and right
    left = seq[p: q]
    right = seq[q : r]
    # set sentinel
    left.append(float('inf'))
    right.append(float('inf'))
    # merge loop
    i = 0
    j = 0
    for k in range(p, r):
        if left[i] <= right[j]:
            seq[k] = left[i]
            i = i + 1
        else:
            seq[k] = right[j]
            j = j + 1

def merge_sort(seq, p, r):
    '''
    sort by dividing seq to seq[p: q+1] and seq[q+1: r+1]
    where q = floor((r+p)/2)
    '''
    if r - p > 1:
        q = int((r + p) / 2)
        merge_sort(seq, p, q)
        merge_sort(seq, q, r)
        merge(seq, p, q, r)
    return

if __name__ == '__main__':
    MY_LIST = list(input('Enter some numbers: '))
    r = len(MY_LIST)
    # change MY_LIST to the list consists of int's
    for i in range(0, r):
        MY_LIST[i] = int(MY_LIST[i])
    # sort
    merge_sort(MY_LIST, 0, r)
    print(MY_LIST)
