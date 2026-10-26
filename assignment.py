# You can remove 'pass' if you written code in the function
# Exercise 1

def read_line(filename, line_number):
    if line_number <= 0:
        return ""
    file = open(filename, "r")
    line = ""
    for i in range(line_number):
        line = file.readline()
    file.close()
    if line == "":
        return ""
    else:
        return line.strip()

# Exercise 2
def reverse_lines(source, destination):
    file = open(source, "r")
    lst = file.readlines()
    file.close()
    file = open(destination, "w")
    s=0
    for i in range (len(lst)-1,-1,-1):
        file.write(f"{lst[i].strip()}\n")
        s += 1
    file.close()
    return s

# Exercise 3
def merge_files(first, second, destination):
    file1 = open(first, "r")
    file2 = open(second, "r")
    lst1 = file1.readlines()
    lst2 = file2.readlines()
    file1.close()
    file2.close()
    file = open(destination, "w")
    s=0
    for i in lst1:
        file.write(f"{i.strip()}\n")
        s += 1
    for i in lst2:
        file.write(f"{i.strip()}\n")
        s += 1
    file.close()
    return s

# Exercise 4
def find_score(filename, name):
    file = open(filename, "r")
    lst = file.readlines()
    for i in lst:
        parts = i.strip().split(",")
        if(parts[0] == name):
            file.close()
            return int(parts[1])
    file.close()
    return -1
# Exercise 5
def update_score(filename, name, new_score):
    file = open(filename, "r")
    lst = file.readlines()
    file.close()
    find = False
    for i in lst:
        parts = i.strip().split(",")
        if(parts[0] == name):
            find = True
    if (find):
        file = open(filename, "w")
        for i in lst:
            parts = i.strip().split(",")
            if(parts[0] == name):
                file.write(f"{name},{new_score}\n")
            else:
                file.write(f"{i.strip()}\n")
        return True
    else:
        return False
