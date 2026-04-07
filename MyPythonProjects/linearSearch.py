def linearSearch(a, list1):
    count = 0
    found = False
    
    for i in list1:
        count+=1
        if a == i:
            print(f"Number {a} found in position #{count}")
            found = True
    if found == False:
        print("Number not found in the list")
          

def main():
    my_list = [2, 19, 8, 26, 5, 100, 29]

    key = 100

    linearSearch(key, my_list)


if __name__ == "__main__":
    main()

    
    
'''
simpler way to write linearSearch function:

def linear_search(my_list, key):
    for index in range(0, len(my_list)):
        if key == my_list[index]:
            return index
    return -1

list1 = [2, 19, 8, 26, 5, 100, 29]
print(linear_search(list1, 89))
'''
