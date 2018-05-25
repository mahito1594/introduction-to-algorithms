''' Insertion sort'''

def insertion_sort(given_list):
    '''
    insertion sort algorithm
    '''
    for j in range(0, len(given_list)):
        key = given_list[j]
        i = j - 1
        while i >= 0 and key < given_list[i]:
            given_list[i + 1] = given_list[i]
            i = i - 1
        given_list[i + 1] = key

if __name__ == '__main__':
    INPUT_NUMBERS = input('Enter some numbers: ')
    my_list = list(INPUT_NUMBERS)
    print('Before sorting: ', my_list)
    insertion_sort(my_list)
    print('After sorting: ', my_list)
