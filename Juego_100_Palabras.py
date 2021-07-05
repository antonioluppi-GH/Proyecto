import csv
import random


def palabras_del_dia():
    vocabulario = open('vocabulario.csv')
    data = list(csv.DictReader(vocabulario))
    print('¿cuántas palabras vas a aprender hoy?')
    cantidad_hoy = int(input())
    contador = 0
    
    aprendidas = []
    for i in data:
        palabra = random.choice(data)
        print(palabra['español'], '=', palabra['esperanto'])
        contador += 1
        aprendidas.append(palabra)
        data.remove(palabra)
        
        
        if contador == cantidad_hoy:
            contador = 0 
            break
    
    vocabulario.close()
    
    return aprendidas


def repaso(aprendidas):
    print('Repasemos    ¿Cómo se dice...')
    while True:
        repaso_actual = random.choice(aprendidas)
        print(repaso_actual['español'], '?')
        respuesta = str(input())
        if respuesta == repaso_actual['esperanto']:
            print('Bien!')
        else:
            print('¡@^@! Respuesta correcta:', repaso_actual['esperanto'])
        
        
        print('¿Continuar repasando (C) o Salir (S)?')
        orden = str(input())
        if orden.upper() == 'C':
            continue
        elif orden.upper() == 'S':
            break
        else:
            print('la orden no corresponde a ninguna opción (C/S)')
            continue
    

dias = 0


if __name__ == '__main__':
    print('Bienvenido al desafío de las 100 palabras')
    print('¿Cuál es tu nombre?')
    usuario = str(input())
    
    while True:
    
        print('¡Listo para aprender nuevas palabras!')
    
        aprendidas = palabras_del_dia()
    
        repaso(aprendidas)
    
        dias += 1

        if len(aprendidas) == 100:
            print('¡Felicitaciones', usuario, '! completaste 100 palabras')
            print('Te llevó', dias, 'días')
            break

