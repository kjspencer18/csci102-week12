#https://github.com/kjspencer18/csci102-week12
#Kate Spencer
#CSCI 102 - Section B
#Week 11 - Part B

def PrintOutput(str):
    print('OUTPUT', str)
    
def LoadFile(file_name):
    lines = []
    with open(file_name) as file:
        for line in file:
            line = line.strip()
            lines.append(line)
    return lines

def UpdateString(str_1, str_2, num):
    new_str = ""
    for i in range(len(str_1)):
        if i == num:
            new_str += str_2
        else:
            new_str += str_1[i]
    print(new_str)
    
def FindWordCount(my_list, my_str):
    count = 0
    for i in my_list:
        for j in i:
            if my_str in j:
                count += 1
    return count

def ScoreFinder(l1, l2, s):
    k = []
    for i in range(len(l1)):
        if s.lower() == l1[i].lower():
            print("OUTPUT", l1[i], "got a score of", l2[i])
            return
    print("OUTPUT player not found")

def Union(l1, l2):
    l3 = []
    l4 = []
    for i in l1:
        if i not in l3:
            l3.append(i)
    for j in l2:
        if j not in l3:
            l3.append(j)   
    return l3

def Intersection(l1, l2):
    l3 = []
    for i in l1:
        if i in l2:
            l3 += [i]
    return l3

def NotIn(l1, l2):
    l3 = []
    for i in l1:
        if i not in l2:
            l3 += [i]
    return l3