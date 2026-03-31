#Learn to combine different list methods.
#Given two lists, list_1 and list_2, create a new list named diff_list that
#contains all the elements from list_1 that are not in list_2. Make sure there
#are no duplicates in diff_list, and use the sort function to arrange it in
#ascending order.

def main():
    list_1 = [1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 9]
    list_2 = [2, 4, 6, 7]

    diff_list = []

    for i in range(len(list_1)):
        if list_1[i] not in list_2 and diff_list.count(list_1[i]) == 0:
            diff_list.insert(i, list_1[i])

    diff_list.sort()

    print(diff_list)

if __name__ == "__main__":
    main()
