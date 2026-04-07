#Bubble Sort algorithm

def bubble_sort(my_list):
    n = len(my_list)
    
    for p in range(1, n):

        to_continue = False
        for index in range(0, n-p):
            if my_list[index] > my_list[index+1]:
                temp = my_list[index]
                my_list[index] = my_list[index+1]
                my_list[index+1] = temp

                to_continue = True
        if not to_continue:
            break

list1 = [11, 23, 156, 34, 89, 10]
bubble_sort(list1)
print(list1)
