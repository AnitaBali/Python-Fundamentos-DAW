nombre=input("Tu nombre:")

for letra in nombre:
    if letra=='r':
        break
    print(letra)

contesta=input("Tu nombre es:")

for letra in contesta:
    if letra=='r':
       continue
    print(letra)