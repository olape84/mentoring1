import math
from functools import reduce
import statistics

def func(line, n):
    return(line*n)
func('Hi',12)

def circle(r):
    if (r < 0):
        print('Promień powinien być wiekszy od zera')
        return
    else:
        area= math.pi*r**2
        print("Pole koła o promieniu r= ", r, 'wynosi', area)
        perimeter= 2*math.pi*r
        print("Obwód koła o promieniu r= ", r, 'wynosi', perimeter)

circle(9)

lista = [2, 4, 8, 16, 32]
def geoMean(lista):
    geometricMean=statistics.geometric_mean(lista)
    print(geometricMean)
    return geometricMean
geoMean(lista)
print(geoMean(lista))

strList=['kot', 'slowo', 'dom', 'kioski', 'domestika', 'ksenofobia', 'konstantynotanczykowianeczka']
strDict={}
def countWords(strList):
    for word in strList:
        strDict[word]= len(word)
   # print(sorted(strDict.values()))
    longestWord=max(strDict, key=strDict.get)
    print("Najdłuższe słowo to", longestWord, 'i ma', strDict[longestWord], 'znaków')
countWords(strList)


register=["Marcin##3,4,5,6,6", "Agata##5, 1,1,3,4"]
grades={}
for pupil in register:
    student_data=pupil.split('##')
    grades[student_data[0]]=statistics.mean([int(ocena) for ocena in student_data[1].split(',')])

print(grades)


x = []
for i in range(1, 101):
    if i % 2 == 0:
        x.append(i)
print(x)
skladane_x = [i for i in range(1, 101) if i % 2 == 0] # co się dzieje z funkcją append w liście składanej? 
print(skladane_x)