'''
Binary Search
'''

def i_bin_search(seq, value, low, high):
    '''
    Iterative Binary Search:
    find the value in seq[low: high]
    '''
    while low < high:
        mid = (low + high) // 2
        if seq[mid] == value:
            return mid
        elif value > mid:
            low = mid
        else:
            high = mid
    return None

def r_bin_search(seq, value, low, high):
    '''
    Recursive Binary Search:
    find the value in seq[low: high]
    '''
    if high - low < 1: # case: seq[low: high] = []
        return None
    # search for the given value recursive
    mid = (high + low) // 2
    if seq[mid] == value:
        return mid
    elif seq[mid] > value:
        return r_bin_search(seq, value, low, mid)
    else:
        return r_bin_search(seq, value, mid + 1, high)
    # return None

if __name__ == '__main__':
    MY_LIST = list(input('Enter sorted sequance: '))
    # change MY_LIST to the list consists of int'
    HIGH = len(MY_LIST)
    for i in range(0, HIGH):
        MY_LIST[i] = int(MY_LIST[i])
    VALUE = int(input('Enter your value: '))
    INDEX = r_bin_search(MY_LIST, VALUE, 0, HIGH)
    print('The position of your value {0} is {1}'.format(VALUE, INDEX))
