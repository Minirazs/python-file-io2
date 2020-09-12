#open the file for reading
filename = input("please provide filename: ")
filepointer = open(filename)

for line in filepointer:
    print(line.strip()) #strip removes any special character /n /t, space from the strings (start and end only)