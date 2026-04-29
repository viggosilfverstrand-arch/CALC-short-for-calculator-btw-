def add(a,b):
    return(a + b)

def sub(a,b):
    return(a - b)

def mult(a,b):
    return(a * b)

def div(a,b):
    return(a / b)
while True:
    try:
        calc = int(input("""Vad vill du göra?
   
    1. Addera           2. Subtrahera
    
    3. Multiplicera     4. Dividera
      """))
        break
    except ValueError:
        print("Det fungerade inte, prova om.")

if calc == 1:
    while True:
        try:
            addition1 = float(input("Vad är det första talet vill du addera?"))
            addition2 = float(input("Vad är det andra talet vill du addera?"))
            break
        except ValueError:
            print("Glöm inte att du bara kan skriva nummer, prova om.")
    
    
    print(f"Summan av talen {addition1} och {addition2} blir", add(addition1, addition2))

if calc == 2:
    while True:
        try:
            Subtrahering1 = float(input("Vilket tal vill du subtrahera?"))
            Subtrahering2 = float(input("Vilket tal vill du subtrahera med?"))
            break
        except ValueError:
            print("Glöm inte att du bara kan skriva nummer, prova om.")
    
    
    print(f"Diffirensen av talen {Subtrahering1} och {Subtrahering2} blir", sub(Subtrahering1, Subtrahering2))
if calc == 3:
    while True:
        try:
            Multiplication1 = float(input("Vad är det första talet vill du multiplicera?"))
            Multiplication2 = float(input("Vad är det andra talet vill du multiplicera?"))
            break
        except ValueError:
            print("Glöm inte att du bara kan skriva nummer, prova om.")
    
    
    print(f"Produkten av talen {Multiplication1} och {Multiplication2} blir", mult(Multiplication1, Multiplication2))
if calc == 4:
    while True:
        try:
            division1 = float(input("Vilket tal vill du dividera?"))
            division2 = float(input("Vilket tal vill du dividera med?"))
            if division2 == 0:
                ValueError
                print("Du kan inte ha 0 som nämnare! Skriv om.")
            else:
                break
        except ValueError:
            print("Glöm inte att du bara kan skriva nummer, prova om.")
    
    
    print(f"Kvoten av talen {division1} och {division2} blir", div(division1, division2))