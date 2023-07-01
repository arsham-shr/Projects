usr_input = int(input("Enter Base Of Pyramid : "))
for i in range(0, usr_input, 2):
    print((" " * int(((20-i)/2)))+("*" * i))    