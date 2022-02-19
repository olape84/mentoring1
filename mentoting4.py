print([i for i in range (1000) if i % 7 ==0])

print([ i for i in range (1000) if str(3) in str(i)])

x= "Yellow Yaks like yelling and yawning and yesterday they yodled while eating yuky yams"
spaces = [s for s in x if s == ' ']
print("The number of spaces in the given string is: ", len(spaces))

print([i for i in x if i in ['a', 'e', 'i', 'o', 'u']])

#poniższe rozwiązanie znalazłam w necie. da się je przerobić na comprehention list?
count=0
line="Codespeedy Technology Private Limited"
for i in line:
    if(i.isspace()):
        count=count+1
print("The number of blank spaces is: ",count)

