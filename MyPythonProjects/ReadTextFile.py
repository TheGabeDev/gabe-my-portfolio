#Write a program that reads the name of a text file from the keyboard and
#searches an integer in the file. The value to search is also read from
#the keyboard.
#If the searched value exists in the file or it cannot be found in the file
#a proper message is displayed on the screen.
#It is assumed that the input files are a sequence of integers
#separated by a newline character.

def main():
    name = input('Enter the file name: ')
    try:
        myFile = open(name, 'r')
    except FileNotFoundError:
        print("Error: The file doesn't exist")
    else:
        try:
            n = int(input("Enter an integer to search in the file: "))
            for line in myFile:
                if int(line) == n:
                    print(n, 'exists in the file!')
                    break
            else:
                print(n, 'does not exist in the file!')
        except ValueError:
            print('An invalid integer was found!')
        finally:
            myFile.close()

if __name__ == "__main__":
    main()
