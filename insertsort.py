def insertion_sort(string_list):
    '''insertion sort the integers in list in descending order'''
    # convert each string in array to a number
    number_list = [int(number) for number in string_list]

    for j in range(1, len(number_list)):
        # current_value and prior index
        value = number_list[j]
        prior_index = j - 1
        # loop backwards and sort any numbers not in descending order.
        while prior_index >= 0 and number_list[prior_index] < value:
            number_list[prior_index + 1] = number_list[prior_index]
            prior_index -= 1
        number_list[prior_index + 1] = value

    # return the sorted list in descending order.
    return number_list

# list to hold all sorted numbers per line in data.txt
master_list = []

# read each line of the text.
with open('data.txt', 'r') as data_file:
    for line in data_file:
        # turn each line into a list of strings.
        number_list = line.split()
        # append to master list after sorting the numbers.
        master_list.append(insertion_sort(number_list[1:]))

# close the file.
data_file.close()

# write to the file insert.out, the contents of the list in master_list
with open('insert.out', 'w') as outfile:
    for list in master_list:
        for i in range(0, len(list)):
            if i == len(list) - 1:
                outfile.write(str(list[i]))
            else:
                outfile.write(str(list[i]) + ' ')          
        outfile.write('\n')

# close the file
outfile.close()