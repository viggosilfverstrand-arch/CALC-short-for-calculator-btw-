import math

def add(a,b):
    return(a + b)

def sub(a,b):
    return(a - b)

def mult(a,b):
    return(a * b)

def div(a,b):
    return(a / b)

def exp(a,b):
    return (a**b)

def rot(a):
    return a**0.5

def log(a):
    return math.log10(a)

def nlog(a):
    return math.log(a)

e = math.e 
pi = math.pi

i = 0
while i == 0:
    while True:
        try:
            calc = int(input("""Vad vill du göra?
   
    1. Addera           2. Subtrahera
    
    3. Multiplicera     4. Dividera
                         
    5. Exponera         6. Tar roten ur
      
    7. Logaritm         8. Naturlogaritm
                             
    ------>"""))
            break
        except ValueError:
            print("Det fungerade inte, prova om.")

    if calc == 1:
        while True:
            addition1 = input("Vad är det första talet vill du addera?")
            addition2 = input("Vad är det andra talet vill du addera?")
            if addition1 == "e":
                addition1 = math.e
            elif addition1 == "pi":
                addition1 = math.pi
            if addition2 == "e":
                addition2 = math.e
            elif addition2 == "pi":
                addition2 = math.pi
            
            try:
                addition1 = float(addition1)
                addition2 = float(addition2)
                break
            except ValueError:
                print("Glöm inte att du bara kan skriva nummer, prova om.")
    
    
        print(f"\nSumman av talen {addition1} och {addition2} blir", add(addition1, addition2))

    if calc == 2:
        while True:
            Subtrahering1 = input("Vilket tal vill du subtrahera?")
            Subtrahering2 = input("Vilket tal vill du subtrahera med?")
            if Subtrahering1 == "e":
                Subtrahering1 = math.e
            elif Subtrahering1 == "pi":
                Subtrahering1 = math.pi
            if Subtrahering2 == "e":
                Subtrahering2 = math.e
            elif Subtrahering2 == "pi":
                Subtrahering2 = math.pi

            try:
                Subtrahering1 = float(Subtrahering1)
                Subtrahering2 = float(Subtrahering2)
                break
            except ValueError:
                print("Glöm inte att du bara kan skriva nummer, prova om.")
    
    
        print(f"\nDiffirensen av talen {Subtrahering1} och {Subtrahering2} blir", sub(Subtrahering1, Subtrahering2))

    if calc == 3:
        while True:
            Multiplication1 = input("Vad är det första talet vill du multiplicera?")
            Multiplication2 = input("Vad är det andra talet vill du multiplicera?")
            if Multiplication1 == "e":
                Multiplication1 = math.e
            elif Multiplication1 == "pi":
                Multiplication1 = math.pi
            if Multiplication2 == "e":
                Multiplication2 = math.e
            elif Multiplication2 == "pi":
                Multiplication2 = math.pi
            try:
                Multiplication1 = float(Multiplication1)
                Multiplication2 = float(Multiplication2)
                break
            except ValueError:
                print("Glöm inte att du bara kan skriva nummer, prova om.")
    
    
        print(f"\nProdukten av talen {Multiplication1} och {Multiplication2} blir", mult(Multiplication1, Multiplication2))

    if calc == 4:
        while True:
            division1 = input("Vilket tal vill du dividera?")
            division2 = input("Vilket tal vill du dividera med?")
            if division1 == "e":
                division1 = math.e
            elif division1 == "pi":
                division1 = math.pi
            if division2 == "e":
                division2 = math.e
            elif division2 == "pi":
                division2 = math.pi
            try:
                division1 = float(division1)
                division2 = float(division2)

                if division2 == 0:
                    ValueError
                    print("Du kan inte ha 0 som nämnare! Skriv om.")
                else:
                    break
            except ValueError:
                print("Glöm inte att du bara kan skriva nummer, prova om.")
        print(f"\nKvoten av talen {division1} och {division2} blir ", div(division1, division2))

    if calc == 5:
        while True:
            exponent1 = input("Vilket tal vill du ha i basen?")
            exponent2 = input("Vilket tal vill du ha i exponenten?")
            if exponent1 == "e":
                exponent1 = math.e
            elif exponent1 == "pi":
                exponent1 = math.pi
            if exponent2 == "e":
                exponent2 = math.e
            elif exponent2 == "pi":
                exponent2 = math.pi
            try:
                exponent1 = float(exponent1)
                exponent2 = float(exponent2)
                break
            except ValueError:
                print("Glöm inte att du bara kan skriva nummer, prova om.")
    
    
        print(f"\n{exponent1} upphöjt till {exponent2} blir", exp(exponent1, exponent2))

    if calc == 6:
        while True:
            rot1 = input("Vilket tal vill du ta roten ur?")
            if rot1 == "e":
                rot1 = math.e
            elif rot1 == "pi":
                rot1 = math.pi
            try:
                rot1 =float(rot1)
                break
            except ValueError:
                print("Glöm inte att du bara kan skriva nummer, prova om.")
    
    
        print(f"\nRoten ur talet {rot1} blir", rot(rot1))

    if calc == 7:
        while True:
            Logaritm = input("Vilket tal vill du logaritmera?")
            if Logaritm == "e":
                Logaritm = math.e
            elif Logaritm == "pi":
                Logaritm = math.pi
            try:
                Logaritm = float(Logaritm)
                break
            except ValueError:
                print("Glöm inte att du bara kan skriva nummer, prova om.")
    
    
        print(f"\nLogaritmen av talet {Logaritm} blir", log(Logaritm))

    if calc == 8:
        while True:
            Naturlog = float(input("Vilket tal vill du Naturlogaritmera?"))
            if Naturlog == "e":
                Naturlog = math.e
            elif Naturlog == "pi":
                Naturlog = math.pi
            try:
                Naturlog =float(Naturlog)
                break
            except ValueError:
                print("Glöm inte att du bara kan skriva nummer, prova om.")
    
    
        print(f"\nNaturlogaritmen av talet {Naturlog} blir", nlog(Naturlog))

    fråga = input("""
    Vill du räknar någonting mer?
         1. Ja   2. Nej             
    ----> """)
    if fråga =="2" or fråga.upper() == "NEJ":
        print("Avslutar")
        i+=1
    elif fråga =="1" or fråga.upper() == "JA":
        print("Okej, du får fortsätta!")