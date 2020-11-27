import random
import csv

charactors = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','#','!','$','@','%','^','&','*','(',')','/',';',',','\\','|','/','-','_','+','=','?','<','>','\'','1','2','3','4','5','6','7','8','9','0','`','~','[',']','{','}']

def getPass(passArr, chars):
    for _ in range(chars):
        passArr.append(random.choice(charactors))

    return passArr

def arrToStr(arr):
    string = ""

    for char in arr:
        string += char
    
    return string

def savePass(toSave):
    password = {'password': toSave}
    with open('password.csv', 'w') as file:
        feildnames = ['password']
        csv_writer = csv.DictWriter(file, fieldnames=feildnames)

        csv_writer.writeheader()

        csv_writer.writerow(password)

password = []
numChars = input('Length of password: ')
password = getPass(password, int(numChars))

password = arrToStr(password)

print(password)
savePass(password)
