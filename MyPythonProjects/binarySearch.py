#Binary search written using recursion

def binarySearch(my_list, low, high, key):
    if low > high:
        return -1
    mid = (low + high) // 2

    if key == my_list[mid]:
        return mid
    if key < my_list[mid]:
        #continue the search in the first half
        return binarySearch(my_list, low, mid-1, key)
    else:
        return binarySearch(my_list, mid+1, high, key)
    

#Binary search written without recursion

def binary_search(my_list, low, high, key):
    while low <= high:
        mid = (low + high) // 2

        if key == my_list[mid]:
            return mid
        if key < my_list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def main():
    list1 = [1, 23, 56, 134, 189, 1000]
    print(binary_search(list1, 0, 5, 189))

if __name__ == "__main__":
    main()
