''' Insertion sort'''

def insertion_sort_increasing(given_list):
    '''
    sort to no-decreasing order(insertion sort)
    '''
    for j in range(0, len(given_list)):
        key = given_list[j]
        i = j - 1
        # insertion loop
        while i >= 0 and key < given_list[i]:
            given_list[i + 1] = given_list[i]
            i = i - 1
        given_list[i + 1] = key

def insertion_sort_decreasing(given_list):
    '''
    sort to non-increasing order
    '''
    for j in range(0, len(given_list)):
        key = given_list[j]
        i = j - 1
        # insertion loop
        while i >= 0 and key > given_list[i]:
            given_list[i + 1] = given_list[i]
            i = i - 1
        given_list[i + 1] = key

if __name__ == '__main__':
    INPUT_NUMBERS = input('Enter some numbers: ')
    my_list = list(INPUT_NUMBERS)
    print('Before sorting: ', my_list)
    insertion_sort_increasing(my_list)
    print('Sorted to non-decreasing order: ', my_list)
    insertion_sort_decreasing(my_list)
    print('Sorted to non-increasing order: ', my_list)
