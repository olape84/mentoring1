from math import floor
from collections import Counter

dict1={} #czy to ma być zmienna globalna?
def addNewElemToDict (key,value):
    dict1[key]=value
    print(dict1)

addNewElemToDict('slowo', 'czternascie')

zwierzetaDict={'krowa': 1, 'sowa': 2.6, 'kot': 15}
warzywaDict={'cukina': 14, 'marchewka': 3, 'ogorek': 8, 'pomidor': 4}
owoceDict={'jablko': 18, 'gruszka': 6, 'morela': 19.8}
metaDict={}
def joinDictionaries():
    metaDict.update(zwierzetaDict)
    metaDict.update(warzywaDict)
    metaDict.update(owoceDict)
    print(metaDict)
joinDictionaries()

def keyExistsInDictionary(key):
    if key in metaDict:
        print("Podany klucz jest już w słowniku")
    else:
        print("Podanego klucza nie ma w słowniku")
keyExistsInDictionary('kon')
keyExistsInDictionary('krowa')

myDict={}
def generateDict(n):
    x=1-n
    myDict[x]=x**2
    print(myDict)
generateDict(8)

def floorInDict():
    print(floor(max(metaDict.values())))
floorInDict()

def sumOfDictValues ():
    print(sum(metaDict.values()))
sumOfDictValues()

dict10 = {
        'produkt1': 23.3,
        'produkt2': 2.8,
        'produkt3': 3.3,
        'produkt4': 12.78,
        'produkt5': 5.13,
        'produkt6': 2.89,
        'produkt7': 16.47,
        'produkt8': 7.78,
        'produkt9': 23.5,
        'produkt10': 18.8
}
def counting3highestAnd3LowestPricesPlusMean():
    k = Counter(dict10)
    high = k.most_common(3)
    print("Dictionary with 3 highest values:")
    for i in high:
        print(i[0]," :",i[1]) #dlaczego tak?
    my_keys = sorted(dict10, key=dict10.get, reverse=False)[:3]
    print("Dictionary with 3 lowest values:")
    for j in my_keys:
        print(j[0]," :",j[1])
    print("Average price of the product is:", (sum(dict10.values()))/len(dict10)) 
counting3highestAnd3LowestPricesPlusMean()

def userDictionary():
    word = input('Podaj klucz w słowniku: ')
    if word in metaDict.keys():
        print("Wartosc dla klucza", word, "to ", metaDict[word])
    else:
        print('Brak klucza w słowniku')    
userDictionary()

def numberOfCharacters(x,n):
    list1=[] 
    n=len(list1)
    1-x 