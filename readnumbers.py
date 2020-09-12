filepointer = open("numbers.txt")   #reading
total = 0

for line in filepointer:
    total += int(line)

print("The total is", total)