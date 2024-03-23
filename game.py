#nombre y apellido: brandon suarez, numero de alumno:19562/0
import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]
vocal=["a","e","i","o","u"]
# Elegir una palabra al azar 
secret_word = random.choice(words)
# Número máximo de intentos permitidos
max_attempts = 10
# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
word_displayed = "_" * len(secret_word)
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")
letra=input("ingrese la dificultad, facil ,medio, dificil")
fallo=0
letters=[]
if letra=="facil":
     # Iterar sobre cada letra en la palabra secreta
     letters=[]
     for l in secret_word:
         # Si la letra es una vocal, agregarla a la lista de letras
         if l in vocal:
             letters.append(l)
         else:
             letters.append("_")
     word_displayed = "".join(letters)
     print(f"Palabra: {word_displayed}")
     while fallo<3:
         # Pedir al jugador que ingrese una letra
    
         letter = input("Ingresa una letra: ").lower()
         # Verificar si la letra ya ha sido adivinada
         if letter == "":
             print(f'error {fallo}')
             fallo=fallo+1
         else:
             if letter in guessed_letters:
                 print("Ya has intentado con esa letra. Intenta con otra.")
                 fallo=fallo+1
                 continue
             
             # Agregar la letra a la lista de letras adivinadas 
             guessed_letters.append(letter)
             # Verificar si la letra está en la palabra secreta
             if letter in secret_word:
                 print("¡Bien hecho! La letra está en la palabra.")
             else:
                 print("Lo siento, la letra no está en la palabra.")
                 fallo=fallo+1
             # Mostrar la palabra parcialmente adivinada
             letters=[]
             for letter in secret_word:
                 if letter in guessed_letters:
                     letters.append(letter)
                 elif letter in vocal:
                     letters.append(letter)    
                 else:
                     letters.append("_")
             word_displayed = "".join(letters)
             print(f"Palabra: {word_displayed}")
             # Verificar si se ha adivinado la palabra completa
             if word_displayed == secret_word:
                 print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
                 break
     else:        
         print(f"¡Oh no! Has agotado tus {3} intentos.")
         print(f"La palabra secreta era: {secret_word}")


elif letra=="medio":
     cont=0
     for letter in secret_word:
         if cont ==0 or cont== (len(secret_word)-1):
             letters.append(letter)
         else:
             letters.append("_")
         cont +=1   
     word_displayed = "".join(letters)    
     print(f"Palabra: {word_displayed}")       
     while fallo<3:
         # Pedir al jugador que ingrese una letra
    
         letter = input("Ingresa una letra: ").lower()
         # Verificar si la letra ya ha sido adivinada
         if letter == "":
             print(f'error {fallo}')
             fallo=fallo+1
         else:
             if letter in guessed_letters:
                 print("Ya has intentado con esa letra. Intenta con otra.")
                 fallo=fallo+1
                 continue
             
             # Agregar la letra a la lista de letras adivinadas 
             guessed_letters.append(letter)
             # Verificar si la letra está en la palabra secreta
             if letter in secret_word:
                 print("¡Bien hecho! La letra está en la palabra.")
             else:
                 print("Lo siento, la letra no está en la palabra.")
                 fallo=fallo+1
             # Mostrar la palabra parcialmente adivinada
             letters = []
             cont=0
             for letter in secret_word:
                 if letter in guessed_letters:
                     letters.append(letter)
                 elif cont ==0 or cont== (len(secret_word)-1):
                     letters.append(letter)
                 else:
                     letters.append("_")
                 cont +=1    
             word_displayed = "".join(letters)
             print(f"Palabra: {word_displayed}")
             # Verificar si se ha adivinado la palabra completa
             if word_displayed == secret_word:
                 print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
                 break
     else:        
         print(f"¡Oh no! Has agotado tus {3} intentos.")
         print(f"La palabra secreta era: {secret_word}")




elif letra=="dificil":
     while fallo<3:
         # Pedir al jugador que ingrese una letra
    
         letter = input("Ingresa una letra: ").lower()
         # Verificar si la letra ya ha sido adivinada
         if letter == "":
             print(f'error {fallo}')
             fallo=fallo+1
         else:
             if letter in guessed_letters:
                 print("Ya has intentado con esa letra. Intenta con otra.")
                 fallo=fallo+1
                 continue
             
             # Agregar la letra a la lista de letras adivinadas 
             guessed_letters.append(letter)
             # Verificar si la letra está en la palabra secreta
             if letter in secret_word:
                 print("¡Bien hecho! La letra está en la palabra.")
             else:
                 print("Lo siento, la letra no está en la palabra.")
                 fallo=fallo+1
             # Mostrar la palabra parcialmente adivinada
             letters = []
             for letter in secret_word:
                 if letter in guessed_letters:
                     letters.append(letter)
                 else:
                     letters.append("_")
             word_displayed = "".join(letters)
             print(f"Palabra: {word_displayed}")
             # Verificar si se ha adivinado la palabra completa
             if word_displayed == secret_word:
                 print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
                 break
     else:        
         print(f"¡Oh no! Has agotado tus {3} intentos.")
         print(f"La palabra secreta era: {secret_word}")