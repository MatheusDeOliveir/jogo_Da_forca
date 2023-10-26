from funcoes_jogo_da_forca import *
import time
import os 
word = gera_palavra()
secret_word = gera_asteriscos(word)

print ("Jogo da forca! \n\n")
print (f"Você tem {vidas} tentativas restantes. \n\n")



while True:
   
    while True:
        tentativa = input ("Digite uma letra: \n\n")
        if len(tentativa) > 1:
            print ("Digite apenas um caractere. \n")  
            continue  
        else:
            break
    
    teste = verifica_letra(tentativa, word, secret_word)
    if teste == False:
        break
    time.sleep(3)
    os.system("cls")
    
    if '*' not in secret_word:
        print (f"Você venceu!! A palavra secreta era {word}")
        time.sleep(3)
        os.system("cls")
        break
        