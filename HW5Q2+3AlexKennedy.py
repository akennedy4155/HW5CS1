#ak's new changes test
#Q2
def extractColumnI(m, i):
    return [row[i] for row in m]

#Q3
def countNumsWithDigit(upperNumber,digit):
    return len([x for x in range(upperNumber+1) if str(digit) in str(x)])
