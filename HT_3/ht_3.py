from random import randint
import time

#a = [34, 23, 56, 4]
test_list = []
for i in range(10):
    test_list.append(randint(0, 99))


def native_sort(list):
    list.sort()
    return list


def compare_lists(first_list, second_list):
    if first_list == second_list:
        return True
    else:
        return False


def calculate_time(sort_title):

    if sort_title == 'bubble':
        start_time = time.time()
        bubble_sort(test_list)
        time_diff = time.time() - start_time

    elif sort_title == 'insertion':
        start_time = time.time()
        insertion_sort(test_list)
        time_diff = time.time() - start_time

    return time_diff



def bubble_sort(list_for_bubble):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(list_for_bubble) - 1):
            if list_for_bubble[i] > list_for_bubble[i + 1]:
                temp = list_for_bubble[i]
                list_for_bubble[i] = list_for_bubble[i + 1]
                list_for_bubble[i + 1] = temp
                sorted = False

    #print(list)
    return list_for_bubble


def insertion_sort(list):
    for i in range(len(list) - 1):

        curr_value = list[i]
        curr_index = i

        while curr_index > 0 and list[curr_index - 1] > curr_value:
            list[curr_index] = list[curr_index - 1]
            curr_index = curr_index - 1

    list[curr_index] = curr_value

    return list


#print("{0:.4f}".format(bubble_sort(a)))
#bubble_sort(test_list)
#native_sort(a)



#print('bubble sort: time = ' + str("{0:.4f}".format(calculate_time('bubble'))))
#print(list)
print('The list is sorted correctly - ' + str(compare_lists(list_for_bubble), native_sort(test_list)))
#print('The list is sorted correctly - ' + str(compare_lists(insertion_sort(test_list), native_sort(test_list))))
