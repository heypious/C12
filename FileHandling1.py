# Question 1 Read a file and 
name = "test.txt"

# 1) Display the size of the files in bytes
file = open(name, "r")
content = file.read()
print(f"{name} is of size {len(content)} bytes.")
file.close()

# 2) Display number of words avaiable in the file

file = open(name, "r")
content = file.readlines()
word_count = 0
for line in content:
    word_count += len(line.split(" "))
print(f"{name} has {word_count} words. ")
file.close()

# 3) Display number of lines avaiable

file = open(name,"r")
content = file.readlines()
line_count = len(content)
print(f"{name} has {line_count} lines.")
file.close()

# 4) Display number of sentences

file = open(name, "r")
content = file.readlines()
sentenses = 0
for line in content:
    sentenses += len(line.split("."))
print(f"{name} has {sentenses} sentences.")
file.close()

# 5) DIsplay number of sentences started with capital and not in capital

file = open(name,"r")
content = file.readlines()
cap = 0
not_cap = 0
for line in content:
    if line[0].isupper():
        cap += 1
    else:
        not_cap += 1
print(f"{name} has {cap} lines starting with Capital and {not_cap} lines starting with lowercase.")
file.close()

# Question 2 Copy one file into another

file = open(name, "r")
filecontent = file.read()
file.close()
newfile = open("newfile.txt", "w")
newfile.write(filecontent)
newfile.close()

# Question 3 Create a file
newfile = open("newfile.txt", "w")



