import pprint
import string

for i in range (6):
  print('*'*4)

  
def ThreeD(a, b, c):
    lst = [[ ['*' for col in range(a)] for col in range(b)] for row in range(c)]
    return lst
      
pprint.pprint(ThreeD(4,6,3))


list2=[i**2 for i in range(2,20)]
print(list2)

list3=[i for i in range(1,6)]
import itertools
print(list(itertools.permutations(list3)))

def substractLists():
  list4=[]
  for _ in range (10):
    value=float(input("Podaj wartosc do pierwszej listy: "))
    list4.append(value)
  list5=[]
  for _ in range (10):
    value=float(input("Podaj wartosc do drugiej listy: "))
    list5.append(value)
  print("Lista pierwsza to: ",list4,"\nLista druga to: ", list5)
  list6=[]
  for i in range (10):
    list6.append(list4[i]-list5[i])
  print("Lista wyników odejmowania liczb z listy2 od listy1 o tych samych indeksach to: ", list6)
# substractLists()

def multiplyLists(word,x):
  list7=[]
  for _ in word:
    for i in range(x):
      list7.append(_ + str(i + 1))
  print(list7)
multiplyLists('kot',2)

def numberFromList(a,b,c):
  list8 = []
  list8.append(a)
  list8.append(b)
  list8.append(c)
  print(list8)
  print(str(a) + str(b) + str(c))
numberFromList(5, 8, 60)

def cutAlphabetIntoLists(n):
  list9=string.ascii_lowercase
  x = [list9[i:i + n] for i in range(0, len(list9), n)]
  print (x)
cutAlphabetIntoLists(5)
