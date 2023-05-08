import random

# Lista de personas , armas y lugares
personas = ["juan", "pedro", "maria", "luis", "ana"]
armas = ["cuchillo", "pistola", "soga", "veneno", "hacha"]
lugares = ["cocina", "sala", "terraza", "baño", "dormitorio"]

print(personas)
print(armas)
print(lugares)
# Seleccionamos al azar la solución del juego
locacion = random.choice(lugares)
personaje = random.choice(personas)
arma2 = random.choice(armas)

# Crear un diccionario vacío para las asignaciones de cada habitación
asignaciones = {}

# Ciclo para asignar una persona y un arma a cada habitación de manera aleatoria
for lugar in lugares:
    # Seleccionar aleatoriamente una persona y un arma sin repetición
    persona, arma = random.sample(personas, 1)[0], random.sample(armas, 1)[0]
    # Asignar la persona y el arma a la habitación
    asignaciones[lugar] = {"persona": persona, "arma": arma}
    # Eliminar la persona y el arma de las listas correspondientes
    personas.remove(persona)
    armas.remove(arma)

# Creamos un ciclo que permita al usuario hacer sus deducciones
for i in range(8): # El usuario tendrá 8 oportunidades para pedir una pista
    print("\n¿Qué evidencia quieres revisar?")
    print("1. Evidencia de una persona")
    print("2. Evidencia de un lugar")
    print("3. Evidencia de un arma")
    opcion = input("Ingresa tu elección (1, 2 o 3): ")

    if opcion == "1":
        # El usuario eligió revisar la evidencia de una persona
        print("\n¿A que personage quieres interrogar?")
        print("1. Juan")
        print("2. Maria")
        print("3. Pedro")
        print("4. Ana")
        print("5. Luis")
        persona_elegida = input("Ingresa el nombre de la persona que quieres investigar: ").lower()
            
        
        if persona_elegida == personaje:
            #print(f" A {personaje} estuvo en {lugar} pero no lo vio nadie ahi.")
            for clave in asignaciones:
                if asignaciones[clave]['persona'] == persona_elegida:
                    print(f"{persona_elegida} se encuentra en:")
                    print("--", clave)
            print(f" A {personaje} no se le vio por ninguna parte.")
        else:
            for clave in asignaciones:
                if asignaciones[clave]['persona'] == persona_elegida:
                    print(f"{persona_elegida} se encuentra en:")
                    print("--", clave)

    elif opcion == "2":
        # El usuario eligió revisar la evidencia de un lugar
        print("\n¿De que lugar quieres saber?")
        print("1. sala")
        print("2. cocina")
        print("3. baño")
        print("4. dormitorio")
        print("5. terraza")
        lugar_elegido = input("Ingresa el nombre del lugar que quieres investigar: ").lower()
        if lugar_elegido == locacion:
            for habitacion, datos in asignaciones.items():
                if habitacion == lugar_elegido:
                    print("El arma en la habitación", habitacion, "es:", datos['arma'])
                    print("Se detectó que las cámaras de seguridad en ese lugar fueron apagadas poco antes del crimen.")
        else:
            for habitacion, datos in asignaciones.items():
                if habitacion == lugar_elegido:
                    print("El arma en la habitación", habitacion, "es:", datos['arma'])
                    print(" No se encontraron pruebas adicionales en el lugar.")

    elif opcion == "3":
        # El usuario eligió revisar la evidencia de un arma
        print("\n¿Sobre que arma quieres saber?")
        print("1. cuchillo")
        print("2. pistola")
        print("3. veneno")
        print("4. soga")
        print("5. hacha")
        arma_elegida = input("Ingresa el nombre del arma que quieres revisar: ").lower()
        if arma_elegida == arma2:                                 
            for clave in asignaciones:
                if asignaciones[clave]['arma'] ==  arma_elegida:
                    print(f"El arma {arma_elegida} desaparecio de")
                    print("--", clave)
            
        else:   
             for clave in asignaciones:
                if asignaciones[clave]['arma'] ==  arma_elegida:
                    print(f"El arma {arma_elegida} desaparecio de")
                    print("--", clave)
                    print(f"No hay evidencia que sugiera que {arma_elegida} fue utilizada en el crimen.")

# Después de 5 rondas de pistas, el usuario tendrá la opción de hacer una suposición final
print("\n¿Quieres hacer una suposición final?")
print("1. Sí")
print("2. No")
opcion_final = input()

if opcion_final == '1':
    print("\n¿Quién cometió el crimen?")
    respuesta_personaje = input().lower()
    print("\n¿En qué locación ocurrió el crimen?")
    respuesta_locacion = input().lower()
    print("\n¿Qué arma se utilizó en el crimen?")
    respuesta_arma = input().lower()
    
    if respuesta_personaje == personaje and respuesta_locacion == locacion and respuesta_arma == arma2:
        print("¡Felicidades! ¡Has resuelto el crimen!")
    else:
        print("Lo siento, esa no es la solución correcta.")
        print(f"El culpable fue {personaje}, en la locación {locacion}, con el arma {arma2}.")

