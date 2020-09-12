filename = input("Enter the filename: ")
#open a file and append information
filepointer = open(filename, 'a')

line = input("Enter text, type lq to quit: ")

while line != 'lq':
    filepointer.write(line + "\n")
    line = input("Enter text, type lq to quit: ")
filepointer.close()