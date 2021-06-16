''' El proyecto es un juego en modo de aplicación que sirve para
aprender vocabulario en un idioma. Este prototipo consta de un
archivo de 100 palabras en español y esperanto. El usuario elige 
cada día cuántas palabras nuevas aprenderá, éstas se guardan en 
la lista de aprendidas y se remueven de las pendientes. Hay exámenes 
diarios (con fines lúdicos) Al final se puede ver cuánto le llevó 
completar el desfío.'''


import csv
import random


def palabras_del_dia():
    vocabulario = open('vocabulario.csv')
    data = list(csv.DictReader(vocabulario))
    print('¿cuántas palabras vas a aprender hoy?')
    cantidad_hoy = int(input())
    contador = 0
    
    for i in data:
        palabra = random.choice(data)
        print(palabra)
        contador += 1
        aprendidas.append(palabra)
        data.remove(palabra)
        
        if contador == cantidad_hoy:
            contador = 0 
            break
    
    return aprendidas and data


#def repaso(): .....
    



print('Bienvenido al desafío de las 100 palabras')
print('¿Cuál es tu nombre?')
usuario = str(input())

dias = 0
aprendidas = []

 

while True:
    
    print('¡Listo para aprender nuevas palabras!')
    
    palabras_del_dia()
    
    #acá iría la llamada a la función repaso o examen
    
    dias += 1

    if len(aprendidas) == 100:
        print('¡Felicitaciones', usuario, '! completaste 100 palabras')
        print('Te llevó', dias, 'días')
        break
