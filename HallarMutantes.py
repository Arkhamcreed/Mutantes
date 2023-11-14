

# Creación de la matriz
def crearMatriz():
    matriz = []
    for i in range(6):
        fila = input(f"Ingresa la secuencia número {i+1} (sin espacios) que será almacenada y ordenada en forma de fila: ").upper()
        while not validarEntrada(fila):
            print("Por favor, ingresa solo A, C, G o T (Bases Nitrogenadas), y recuerda que deben ser 6 las bases ingresadas por fila")
            fila=input("Intenta nuevamente: ").upper()
        matriz.append(list(fila))
    return matriz


# Función para validar la entrada del usuario

def validarEntrada(entrada):
    basesValidas=set("ACTG")
    return len(entrada) == 6 and all (base in basesValidas for base in entrada)


#Mostramos la matriz construida por pantalla
def imprimirMatriz(matriz):
    for fila in matriz:
        print(" ".join(fila))
    print()


## Debemos establecer un orden para poder analizar la matriz.


#Recorrido de la matriz en caso  de que la dirección sea oblicua

        #*          Definimos las siguientes funciones para cubrir ambos casos de dirección oblicua, con pendientes positiva y negativa       
#                                   \               /
#                    (negativa)      \      y      /      (positiva)  
#                                     \           /
# *# 


def RecorrerDirecciónOblicuaNegativa (matriz):

##Caso pendiente negativa:
    resultado=0
    for i in range(0,3,1):
        for j in range(0,3,1):
            cont=0
            for x in range(0,3,1):
                elementoActual=matriz[i+x][j+x]
                elementoPróximo=matriz[i+1+x][j+1+x]
                if elementoActual==elementoPróximo:
                    cont+=1
                else:
                    cont=0
                if cont>=3 :
                    resultado+=1
    return resultado



def RecorrerDirecciónOblicuaPositiva (matriz):


##Caso pendiente negativa:
    resultado=0
    for i in range(0,3,1):
        for j in range(5,2,-1):
            cont=0
            for x in range(0,3,1):
                elementoActual=matriz[i+x][j-x]
                elementoPróximo=matriz[i+1+x][j-1-x]
                if elementoActual==elementoPróximo:
                    cont+=1
                else:
                    cont=0
                if cont>=3 :
                    resultado+=1
                    
    return resultado


def RecorrerDireccionHorizontalYVertical (matriz , direccion):

## Recorrido de la matriz en los casos de que la dirección sea horizontal o vertical
    resultado=0
    for i in range(0,6,1):
        #Recorrermos la matriz fila por fila (caso dirección horizontal) o columna por columna (caso dirección vertical)
            cont=0
            for j in range (0,5,1):
                
                if direccion=="horizontal":
                    elementoActual=matriz[i][j]
                    elementoPróximo=matriz[i][j+1]
            
                elif (direccion=="vertical"):
                    elementoActual=matriz[j][i]
                    elementoPróximo=matriz[j+1][i]
            
                if (elementoActual==elementoPróximo):
                    cont+=1
                else:
                    cont=0
                if cont>=3 :
                    resultado+=1
        
    return resultado


print("Iniciando Programa de análisis genético...")
print(" \n \nADVERTENCIA\n \n No ejecute éste programa más allá de los límites preestablecidos. Es imperativo no acceder a  ésta información en un área que no esté protegida del alcance del Charles Xavier")


print("A continuación, Introduzca la secuencia genética completa del sujeto a analizar según se especifique: ")
dna =crearMatriz()

#Procedemos a mostrar la matriz ingresada por pantalla:
print("Ordenamiento de la secuencia de ADN ingresada: ")
imprimirMatriz(dna)

## Análisis de Segmentos Horizontales:  ---------------

#                  y

#* Análisis de Segmentos Verticales : |
#                                     |
#                                     |
#                                     |  
#                                     |
#  
# *#
horizontal= RecorrerDireccionHorizontalYVertical(dna, "horizontal")
print("Segmento/s de código genético horizontal/es: ",horizontal)
vertical= RecorrerDireccionHorizontalYVertical(dna , "vertical")
print("Segmento/s de código genético vertical/es: ",vertical)
#* Análisis de Segmentos Oblicuos : \        /
#                                    \      /
#                                     \    /  
# *#
oblicua1= RecorrerDirecciónOblicuaNegativa(dna)
print("Segmento/s de código genético oblicuo/s con pendiente negativa: ",oblicua1)
oblicua2=RecorrerDirecciónOblicuaPositiva(dna)
print("Segmento/s de código genético oblicuo/s con pendiente positiva: ",oblicua2)

##Sumo los resultados obetnidos en cada análisis direccional
GenM=horizontal+vertical+oblicua1+oblicua2
print("Cantidad de secuencias de bases nitrogenadas mutadas: ",GenM)
#Una vez obtenido todo el análisis en cada dirección, decidiremos si el sujeto es Mutante o no


if GenM>=2:
    EsMutante=True
else:
    EsMutante=False

##Le mostramos al operador los datos obtenidos:

if EsMutante==True:
    print("El sujeto es mutante. Orden de búsqueda ya emitido.")
elif EsMutante==False:
    print("El sujeto no es mutante")

print("Cerrando programa de análisis genético...")