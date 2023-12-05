def runInputFile (filename):
    with open(filename) as inputfile :
        validSum = 0
        powerSum = 0
        for line in inputfile:
            id, power = getlineinfo(line)
            validSum = validSum + id
            powerSum = powerSum + power 
    return validSum, powerSum

def getlineinfo(line):
    rmin, gmin, bmin = 0,0,0
    r,g,b = 12, 13, 14
    split = line.split(':')
    game, sets = split[0], split[1]
    id = int(game[5:])
    for i in range(len(sets)):
        if sets[i] == ' ' :
            if sets[i+1] == 'r':
                num = int(sets[i-2:i+1])   
                if num > r:  
                    id = 0
                if num > rmin:
                    rmin = num
            if sets[i+1] == 'g':
                num = int(sets[i-2:i+1])   
                if num > g:  
                    id = 0
                if num > gmin:
                    gmin = num
            if sets[i+1] == 'b':
                num = int(sets[i-2:i+1])   
                if num > b:  
                    id = 0
                if num > bmin:
                    bmin = num
    power = rmin*gmin*bmin 
    return id, power

def main():
    ans1, ans2 = runInputFile('day2input.txt')  
    print(f'ID sum is: {ans1}\nPower Sum is: {ans2}')
main()