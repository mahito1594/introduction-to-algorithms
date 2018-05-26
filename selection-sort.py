'''Selection sort'''

def selection_sort(given_list):
    '''
    sort to non-decreasing order(by selection sort)
    '''
    for j in range(0, len(given_list) - 1):
        temp = given_list[j]
        smallest = j
        # selection loop
        for i in range(j + 1, len(given_list)):
            if given_list[i] < given_list[smallest]:
                smallest = i
        given_list[j] = given_list[smallest]
        given_list[smallest] = temp

if __name__ == '__main__':
    MY_LIST = list(input('Enter some numbers: '))
    selection_sort(MY_LIST)
    print(MY_LIST)
