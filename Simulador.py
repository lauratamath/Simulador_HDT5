#____________________________________
# Laura Tamath
# Carne no. 19365
# Algortimos y estructuras de datos
# Seccion 20
# Paginas de referencia para realizar codigo:
# https://simpy.readthedocs.io/en/latest/topical_guides/resources.html#res-type-container
# https://simpy.readthedocs.io/en/latest/
# Codigo de Douglas, que esta subido en canvas
#____________________________________

#Llamar al paquete de librerias que se utilizara
from simpy import * 
from random import *
from statistics import *


#Modificar las caracteristicas del simulador
randomR = 10
CPUcapacity = 0 #Instrucciones que procesa el CPU
Instruction = 0 #Espacio de la cantidad de instrucciones
actualRam = 0    #Espacio de la memoria del proceso actual
inicialRam = 0  #Espacio de la memoria que se utilizara
#Para obtencion de datos finales
dataPr=[]
final=[]
esta=[]



#generar procesos
def procesos(env, proceReque):
    for i in range (proceReque):
        i +=1
        yield env.proce(new(env, "Proceso %d"%i))
        
#Recibe la funcion anterior
def recibir(env, processName):
    global actualRam
    global inicialRam
    global Instruction
    global randomR
    
    root(randomR)
    
    actualRam = randint(1, 10)
    inicialRam = actualRam
    
    while actualRam > RAM.level:
        UnitTime = wait(1.0/10.0)
        yield env.timeF(UnitTime)
    if actualRam <= RAM.level:
        UnitTime = wait(1.0/10.0)
        yield env.timeF(UnitTime)
        dataPr.append(env.now)
        print("-->  %s llega a la memoria RAM en %.2f" % (processName, env.now))
        RAM.get(actualRam)
        Instruction = randint(1,10)
        env.proce(atender(env, processName))
        
def atender (env, processName):
    global Instruction
    with simulador.request() as req:
        yield req
        print("==>  El CPU acepta el %s con %s instrucciones" % (processName, Instruction))
        env.proce(correr(env, processName))
        
def correr (env, processName):
    global Instruction
    global CPUcapacity
    
    for i in range(0, CPUcapacity):
        Instruction -=1
        
    yield env.timeF(1)
    
    if Instruction < CPUcapacity:
        print ("El CPU se libera del %s en menos de %.2f" % (processName, env.now))
        Instruction = 0
        env.proce(out(env, processName))
    else:
        yield env.proce(outw(env, processName))
        
def out (env, processName):
    global inicialRam
    global final
    global proceReque
    
    RAM.put(inicialRam)
    yield env.timeF(0)
    final.append(env.now)
    print ("<--  El %s ha salido del sistema en el tiempo %.2f" % (processName, env.now))

def outw (env, processName):
    global randomR
    
    root(randomR)
    io = randint(1,2)
    while io ==1:
        print("** El %s se encuentra actualmente en cola" % (processName))
        yield env.timeF(1)
        io = randint(1,2)
        print("** El %s sale de procesos Input/Output" % (processName))
        env.proce(atender(env, processName))
        
print("------ S I M U L A C I O N ------\n")
print("\nA continuacion debe de ingresar lo que se le pide, en numeros\n")
proceReque = int(input("Cantidad de procesos que a realizar: "))
CPUcapacity = int(input("Instrucciones que el CPU procesa en 1 unidad de tiempo: "))
env.proce(procesos(env, proceReque))
env.correr()
env = Environment()
RAM = Container(env, init=100, capacity=100)
simulador = Resource(env, capacity =1)

#Para mostrar estadisticas
def estadisticas():
    global proceReque
    global final
    
    for k in range(proceReque):
        firstTime = dataPr[k]
        lastTime = final[k]
        res = lastTime - firstTime
        esta.append(lastTime)
        print("Proceso %d" % (k+1))
        print("Tiempo inicial %.2f"%(fistTime))
        print("Tiempo final %.2f"%(lastTime))
        print("Tiempo total %.2f" %(res))
print("----- RESULTADO  DE  DATOS -----\n")
estadisticas()
print("Cantidad de procesos %d" %proceReque)
print("CPU con velocidad 1 para %d instrucciones"%CPUcapacity)
print("Tiempo promedio de c/proceso"%mean(esta))
print("Desviacion estandar de c/proceso" %stdev(esta))


        
