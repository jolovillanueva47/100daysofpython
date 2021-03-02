with open("file1.txt") as data:
    file1=[int(line.strip()) for line in data]
file2=[int(line.strip()) for line in open("file2.txt")]
common=[num for num in file1 if num in file2]
print(common)


