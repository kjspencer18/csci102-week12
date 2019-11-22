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

