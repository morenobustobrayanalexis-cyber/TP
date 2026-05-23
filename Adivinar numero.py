import random
random.seed()    #Prepare random number generator

Nrandom = int(random.random() *  100)
i = 1
bandera = True

while bandera == True:
    print("digite el numero")
    Ndigitado = float(input())
    if Nrandom == Ndigitado:
        print("felicidades has adivinado el numero en " + str(i) + " intentos")
        bandera = False
    else:
        if Ndigitado > Nrandom:
            print("el numero es menor")
        else:
            print("el numero es mayor")
        i = i + 1    