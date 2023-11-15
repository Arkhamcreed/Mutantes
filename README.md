# Mutantes
*Nombre y Apellido:  Emiliano García
*Legajo:  51543
*Email:  emifacherogarcia@gmail.com

## De qué trata el código

El código desarrollado en el archivo "HallarMutantes.py" consiste en la detección de segmentos de caracteres similares contenidos en una matriz estática cuadrada 6x6.
El usuario va a ingresar por consola secuencias de bases nitrogenadas que serán incluidas en la matriz a modo de filas, para luego, mediante diversas operaciones,
ser capaces de concluir si hay almenos 2 secuencias de 4 bases nitrogenadas consecutivas (en cualquier dirección) contenidas en la matriz.

## Cómo lo resolvimos

Al principio del proyecto, surgieron múltiples ideas posibles para afrontar el problema. Se pensó luego de mucha meditación, que la opción más lógica era la de desarrollar diferentes anlisis por separado, cada uno asignado a cada direccion posible que podia adoptar un segmento de 4 elementos similares:

. Dirección oblicua con pendiente Positiva
. Dirección oblicua con pendiente Negativa
. Dirección Horizontal
. Dirección Vertical

El primer problema que surgió fue el hecho de salir de rango constantemente en los análisis de las direcciones direccionales. La primera medida que se me ocurrió fue la de agregar a la matriz 3 filas nulas arriba y abajo de la matriz, así como también 3 columnas nulas a cada lado de la matriz. Hay pruebas de ésta primera versión del código en el archivo llamado borrador.py

Teniendo la anterior premisa, se crearon un total de 3 funciones incluidas en el programa:

"def RecorrerDirecciónOblicuaNegativa (matriz):"  Recorre la matriz trazando diagonales de pendiente negativa como su nombre lo indica. Recibe como parámetro la matriz a analizar.

"def RecorrerDirecciónOblicuaPositiva (matriz):"  Recorre la matriz trazando diagonales de pendiente positiva como su nombre lo indica. Recibe como parámetro la matriz a analizar.

"def RecorrerDireccionHorizontalYVertical (matriz , direccion):" Recibe como parámetros la matriz a analizar,  así como una variable de tipo String que determinaría qué recorrido analizar, ya sea horizontal o vertical.

Una vez que se pudo hacer funcionar cada una de las anteriores funciones, surgió el nuevo problema: Permitir al usuario la introducción de los datos, ya que hasta ese momento, se estaba trabajando con una matriz de prueba ya creada en el editor. La raíz del problema era que era muy difícil mantener la estructura de "matriz rodeada de elementos vacíos", por lo que, manteniendo la lógica ya implementada hasta ése momento, y luego de múltiples errores y dificultades relacionadas con la determinación de los rangos de recorrido de la matriz, se pudo adaptar el programa a una matriz sin celdas vacías alrededeor.

Una vez finalizado el problema del correcto recorrido de la matriz, tocó trabajar en la interfaz del programa y en la interacción con el usuario.

Se creó una función para que el usuario pudiese ingresar los datos de la matriz: "def crearMatriz():", seguida de una función para mostrar dicha matriz en la consola: "def imprimirMatriz(matriz):"

Luego de analizar la matriz en todas sus posibles direcciones, se determina si el sujeto analizado es o no mutante, y se deja explícito al usuario.




## Cómo correrlo

Debe ejecutar el archivo HallarMutantes.py, el cual está diseñado para ser operado mediante una ventana de comandos. 
```

py HallarMutantes.py

```
No se preocupe por no entender lo que se debe hacer en el programa, ya que hay muchas indicaciones que se mostrarán por pantalla, contemplando incluso casos en los que ingrese valores incorrectos para el proceso a realizar.

De todas formas, aquí va una breve explicación de lo que el operador debe hacer: Ingresar sin espacios 6 caracteres los cuales serán las 4 iniciales de las bases nitrogenadas existentes en el genoma humano: Adenina (A), Citosina (C), Timina (T), Guanina (G). Hasta ahí llega la intervención del operador, el resto lo hace el programa. 