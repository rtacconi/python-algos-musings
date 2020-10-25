def swap_positions(list,l):
    list[l], list[l+1] = list[l+1], list[l]

def bubble_sort(data):
    for x in range(len(data)):
        swapped = False

        for i in range(len(data)-1):

            if data[i] > data[i + 1]:
                swap_positions(data,i)
                swapped = True

        if swapped == False:
            break
    return data

list = [1,3,2,7,6,5,4,8,9]
assert bubble_sort(list) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
