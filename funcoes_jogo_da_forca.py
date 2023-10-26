import random as rand
import time
import os 
 
PALAVRAS = ['computador', 'casa', 'helicoptero', 'elefante', 'apartamento', 'substituto', 'dor'] 
palavra = ''
vidas = 5
acerto = False

def gera_palavra(lista=PALAVRAS): 
    palavra_misteriosa = rand.choice(PALAVRAS)
    
    return palavra_misteriosa
    
    
def gera_asteriscos(palavra):
    for l in palavra:
        palavra = palavra.replace(l, '*')
        
    palavra_asterisco = [*palavra]
    
    return palavra_asterisco


def verifica_letra(letra, palavra, asteriscos):
    word = [*palavra]
    c = 0
    global acerto
    global vidas 
    for l in word:
        letra.lower()
        if l == letra: 
            asteriscos[c] = letra
            print (asteriscos)
            acerto = True       
        c += 1
    if acerto == False:
        vidas -= 1
        print (asteriscos)
        print (f"Ainda te restam {vidas} tentativas")
        
    if vidas == 0:
        print ("Você Perdeu! ")
        time.sleep(3)
        os.system("cls")
        return False