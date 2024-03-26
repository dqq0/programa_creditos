import time
import datetime
 
#definir clase contador con hora minutos y segundos
def contador(h, m, s):
 
    #calcula la cantidad total de segundos
    total_segundos = h * 3600 + m * 60 + s
 
    #Mientras los segundos sean mayores a 0 se restara un segundo 
    while total_segundos > 0:
 
        # contador representa el tiempo restante del contador
        timer = datetime.timedelta(seconds = total_segundos)
        
        # escribe el tiempo restante del contador
        print(timer, end="\r")
 
        # retrasa el programa un segundo
        time.sleep(1)
 
        # reduce el tiempo en un segundo cada segundo
        total_segundos -= 1
 
    print("El contador ha terminado")
 
#Ingresar la hora
h = input("Ingresa el tiempo en horas: ")
m = input("Ingresa el tiempo en minutos: ")
s = input("Ingresa el tiempo en segundos: ")
contador(int(h), int(m), int(s))