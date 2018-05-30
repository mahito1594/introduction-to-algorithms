'''
Recursive insertion sort
'''

def insert(seq, n):
    '''
    insert seq[n] to sorted sequence seq[:n]
    n must be < len(seq)
    '''
    key = seq[n]
    i = n - 1
    while i >= 0 and seq[i] > key:
        seq[i + 1] = seq[i]
        i = i - 1
    seq[i + 1] = key

def r_insert_sort(seq, n):
    '''
    sort seq[:n] recursive
    '''
    if n > 1:
        r_insert_sort(seq, n-1)
        insert(seq, n-1)
    return

if __name__ == '__main__':
    MY_LIST = list(input('Enter some numbers: '))
    n = len(MY_LIST)
    # change MY_LIST to the list consists of int's
    for i in range(0, n):
        MY_LIST[i] = int(MY_LIST[i])
    # sort
    r_insert_sort(MY_LIST, n)
    print(MY_LIST)
