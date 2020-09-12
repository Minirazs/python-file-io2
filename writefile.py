#open the file in the write mode
#1. if the file does not exist, Python will create it
#2. if the file exists, Python will overwrite all will existing
#3. can only do write and append. no edit mode
filepointer = open("info.txt", "w") 
filepointer.write("Chicken Thigh\n")
filepointer.write("Fresh Milk\n")
filepointer.write("Eggs\n")
filepointer.close()

