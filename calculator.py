import math

def perimetro_quadrato(lato):
    return lato * 4

def circonferenza_cerchio(raggio):
    return 2 * math.pi * raggio

def perimetro_rettangolo(base, altezza):
    return 2 * (base + altezza)

def calcola_perimetro():
    print("Scegli la figura geometrica per la quale vuoi calcolare il perimetro:")
    print("1. Quadrato")
    print("2. Cerchio")
    print("3. Rettangolo")
    
    scelta = input("Inserisci il numero corrispondente alla tua scelta: ")
    
    if scelta == '1':
        lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
        print(f"Il perimetro del quadrato è: {perimetro_quadrato(lato)}")
    
    elif scelta == '2':
        raggio = float(input("Inserisci il raggio del cerchio: "))
        print(f"La circonferenza del cerchio è: {circonferenza_cerchio(raggio)}")
    
    elif scelta == '3':
        base = float(input("Inserisci la base del rettangolo: "))
        altezza = float(input("Inserisci l'altezza del rettangolo: "))
        print(f"Il perimetro del rettangolo è: {perimetro_rettangolo(base, altezza)}")
    
    else:
        print("Scelta non valida! Riprova.")

calcola_perimetro()