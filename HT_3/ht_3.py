'''This variant contains universal function for time calculation - calculate_time(sort_func, sort_name)
Argument for this function - function for sorting and list for sorting
'''

from random import randint, uniform
import time

test_list = []
test_list_float = []


for i in range(100000):
    test_list.append(randint(0, 99))            #create random list of int


for j in range(100000):
    test_list_float.append(uniform(0, 99.9))  #create random list of float


def bubble_sort(list_for_bubble):
    sorted = False          # set initial status

    while not sorted:   # check bool value
        sorted = True
        for i in range(len(list_for_bubble) - 1):       # select each element in a list
            if list_for_bubble[i] > list_for_bubble[i + 1]:     # compare current value with the next value
                temp = list_for_bubble[i]   # change value if true. use temporary value
                list_for_bubble[i] = list_for_bubble[i + 1]
                list_for_bubble[i + 1] = temp
                sorted = False  # status False if changes were made

    return list_for_bubble      # return sorted list


def insertion_sort(list_for_ins):

    for i in range(1, len(list_for_ins)):   # select each element in a list

        curr_value = list_for_ins[i]        # wrire current value in a variable
        curr_index = i                  # write current index in a variable

        while curr_index > 0 and list_for_ins[curr_index - 1] > curr_value:     # check condition for part
            list_for_ins[curr_index] = list_for_ins[curr_index - 1]     # change values while loop is true
            curr_index = curr_index - 1

        list_for_ins[curr_index] = curr_value   # set current value as position

    return list_for_ins     # return sorted list


def selection_sort(list_for_sel):

    for i in range(len(list_for_sel)):
        min_value = min(list_for_sel[i:])   # find minimum value
        min_index = list_for_sel[i:].index(min_value)   # find min value index
        list_for_sel[i + min_index] = list_for_sel[i]       # change min index element and firls element
        list_for_sel[i] = min_value                  # change first element with min element

    return list_for_sel # return sorted list


def calculate_time(sort_func, sort_name):       # argements are func name and it argument
    start_time = time.time()        # record time before sorting
    custom_sorted_list = sort_func(sort_name)   # call sort function
    time_diff = time.time() - start_time    # find time execution
    return time_diff, custom_sorted_list    # return time execution and sorted list


def native_sort(initial_list):
    new_list = list(initial_list)       #make list copy, because func changes initial list
    new_list.sort()             # use native Python sort method
    return new_list


def compare_lists(first_list, second_list):
    if first_list == second_list:       # compare sorted lists with custom and native sort
        return True     # return True if lists are equal
    else:
        return False    # return False if lists aren't equal


def print_result (test_list, sort_type ):

    native_sorted_list = native_sort(test_list)     # sort list by native sort
    sorting_time, sorted_list = calculate_time(sort_type, test_list)    # sort list by custom sort and get time execution

    return print(str(sort_type) + ' : time = ' + str("{0:.4f}".format(sorting_time)) +  # display sort algorithm time, used .format for 4 digits after point,
          ', The list is sorted correctly - ' + str(compare_lists(sorted_list, native_sorted_list)))  # return True if native and custom sorting results are equal

'''
For run:
- use func :  print_result(test_list, sort_type )
- test_list : test_list - list of integers, test_list_float - list of floats
- sort_type : bubble_sort, insertion_sort, selection_sort

'''

print_result(test_list, bubble_sort)
#print_result(test_list, insertion_sort)
#print_result(test_list, selection_sort)
#print_result(test_list_float, bubble_sort)
#print_result(test_list_float, insertion_sort)
#print_result(test_list_float, selection_sort)