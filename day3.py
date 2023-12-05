def runInputFile (filename):
    lines = []
    with open(filename) as inputfile :
        for line in inputfile:
            ln = '.' + line[:-1] + '.'
            lines.append(ln)
    blank  = '.' * len(lines[0])
    lines.insert(0, blank)
    lines.append(blank)
    return lines

def checkneighbors (neighborhood):         
    for m in neighborhood :
        for n in m :
            if n != '.' and not n.isdigit():
                # found a special character
                return True 
            else :
                pass
    return False

def main():       
    lines = runInputFile('day3input.txt')
    for x in lines :
        print(x)
    validnums = []
    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            if line[j].isdigit() and not line[j-1].isdigit(): # find digit preceeded by nondigit
                # small loop to capture number
                valid = False
                num = ''
                runloop = True
                x = j
                while runloop == True :
                    if line[x].isdigit() :
                        num = num + line[x]
                        neighborhood = []
                        neighborhood.extend([ line[x-1], line[x+1], lines[i-1][x-1:x+2], lines[i+1][x-1:x+2] ])
                        x += 1
                        if checkneighbors(neighborhood) == True :
                            valid = True 
                    else:
                        runloop = False
                if valid == True:
                    validnums.append(int(num))
                    valid = False

    print(sum(validnums))
                
main()