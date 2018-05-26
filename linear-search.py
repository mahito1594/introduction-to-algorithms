'''Linear search'''

def linear_search(sequence, value):
    '''
    search the index which value is equal to given one(by linear search)
    '''
    for i in range(0, len(sequence)):
        if sequence[i] == value:
            return i
    return None

if __name__ == '__main__':
    MY_LIST = list(input('Enter your sequance: '))
    VALUE = input('Enter your value: ')
    INDEX = linear_search(MY_LIST, VALUE)
    print('The position of your value {0} is {1}'.format(VALUE, INDEX))
