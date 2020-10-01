def merge_sort(number_list):
    ''' Merge sort the list of integers in descending order,
    influenced from https://www.geeksforgeeks.org/merge-sort/ '''

    if len(number_list) > 1:
        # get midpoint of number list
        mid = len(number_list) // 2
        # get left & right of mid point
        left_sub_array = number_list[:mid]
        right_sub_array = number_list[mid:]

        # recurse the left and right 
        left = merge_sort(left_sub_array)
        right = merge_sort(right_sub_array)

        number_list = []

        while len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                number_list.append(left[0])
                left.pop(0)
            else:
                number_list.append(right[0])
                right.pop(0)

        for i in left:
            number_list.append(i)

        for i in right:
            number_list.append(i)

    return number_list

# list to hold all sorted numbers per line in data.txt
master_list = []

# read each line of the text.
with open('data.txt', 'r') as data_file:
    for line in data_file:
        # turn each line into a list of strings.
        number_list = line.split()
        # slice from 1st index to end
        number_list = number_list[1:]
        # list comrephension to convert string to int
        number_list = [int(number) for number in number_list]
        # append to master list after sorting the numbers.
        master_list.append(merge_sort(number_list))

# close the file.
data_file.close()

# write to the file merge.out, the contents of the list in master_list
with open('merge.out', 'w') as outfile:
    for list in master_list:
        for i in range(0, len(list)):
            if i == len(list) - 1:
                outfile.write(str(list[i]))
            else:
                outfile.write(str(list[i]) + ' ')          
        outfile.write('\n')

# close the file
outfile.close()