def selection_sort(data):

    for scan_index in range(0, len(data)):
        # one loop per item in the list
        min_index = scan_index

        for comp_index in range(scan_index + 1, len(data)):
            # scan from next item until the end
            if data[comp_index] < data[min_index]:
                min_index = comp_index

        if min_index != scan_index:
            # after the loop above if indexes are not the same
            # swap items
            data[scan_index], data[min_index] = data[min_index], data[scan_index]

    return data

list = [1,3,2,7,6,5,4,8,9]
assert selection_sort(list) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
