### This is a test for GitHub

def print_even(x):
    # print even number from 0 up and include x
    for i in range(0, x+2, 2):
        print(i, end=", ")

def main():
    print ("Hello World!")
    print ("What a beautiful day!")
    print_even(10)
    # added this in github
    print()

if __name__ == "__main__":
    main()