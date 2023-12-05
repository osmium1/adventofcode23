def getCalibrationTotal (filename):
    with open(filename) as inputfile :
        sumOfall = 0
        for line in inputfile:
            val = getCalibration_fromLine(line)
            sumOfall = sumOfall + val
    return sumOfall 

def getCalibration_fromLine(line):
    val = ''
    for i in range(len(line)):
        if line[i].isdigit():
            val = val + line[i]
        else:
            num = ''
            try:
                 num = checkForNumber(i,line)
                 # num stores a string
            except IndexError:
                 pass
            if num != '' and num !=  None:
                val = val + str(num)
    calib = val[0] + val[-1]
    return int(calib)

def checkForNumber (index,line) :
    str = False
    if line[index] == 'o':
        str = line[index:index+3]
    if line[index] == 'e':
        str = line[index:index+5]
    if line[index] == 'n':
        str = line[index:index+4]
    if line[index] == 't':
        if line[index+1] == 'h':
            str = line[index:index+5]
        if line[index+1] == 'w':
            str = line[index:index+3]
    if line[index] == 'f':
        str = line[index:index+4]    
    if line[index] == 's':
        if line[index+1] == 'i':
            str = line[index:index+3]
        if line[index+1] == 'e':
            str = line[index:index+5]
    if getDigit(str) !=  False:
        return getDigit(str)

def getDigit(string):
    digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    if string in digits:
                return digits[string]
    else: 
         return False

def main():
    answer = getCalibrationTotal('day1input.txt')
    print(answer)

main()