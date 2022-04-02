aOne = float(input('enter assignment 1 grade'))
aTwo = float(input('enter assignment 2 grade'))
aThree = float(input('enter assignment 3 grade'))
aFour = float(input('enter assignment 4 grade'))
aFive = float(input('enter assignment 5 grade'))
aSix = float(input('enter assignment 6 grade'))
midTest = float(input('enter midterm exam grade'))
finalEx = float(input('enter final exam grade'))

aWeight = .45
testWeight = .55

aAvg = (aOne + aTwo + aThree + aFour + aFive + aSix) / 6
testAvg = (midTest + finalEx) / 2

aAdjusted = aAvg * aWeight
testAdjusted = testAvg * testWeight

finalGrade = aAdjusted + testAdjusted

print('The final grade is', format(finalGrade, '.1f'))

#Anthony Secreti, asecreti, A201, assignment 1
#asecreti_chapter2.py, 2/13
