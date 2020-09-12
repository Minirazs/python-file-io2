filename = input("Enter filename: ")
filepointer = open(filename, 'r')
lines = list(filepointer)  #read each line and store into a list
print(lines)

line_delete = int(input("Which line to delete? "))
del lines[line_delete] #remove the line from the list by its index

filepointer.close()

filepointer = open(filename, 'w')
for l in lines: 
    filepointer.write(l)
filepointer.close()