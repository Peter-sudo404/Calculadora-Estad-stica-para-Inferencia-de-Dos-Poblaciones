
# Calculadora Estadística para Inferencia de Dos Poblaciones

Este programa en Python ofrece una **Calculadora Estadística para Inferencia de Dos Poblaciones** con un menú interactivo. Permite a los usuarios calcular varios estadísticos de prueba para comparar dos poblaciones, incluyendo diferencias en medias, varianzas y proporciones.

## Funcionalidades

El programa incluye las siguientes opciones:

1. **Diferencia de Medias con Varianzas Conocidas**: Calcula el estadístico \( z_0 \) para comparar las medias de dos poblaciones con varianzas conocidas.
2. **Diferencia de Medias con Varianzas Desconocidas e Iguales**: Calcula \( t_0 \) usando la varianza combinada para dos poblaciones con varianzas desconocidas pero iguales.
3. **Diferencia de Medias con Varianzas Desconocidas y Diferentes**: Calcula \( t_0 \) y los grados de libertad \( V \) para dos poblaciones con varianzas desconocidas y diferentes.
4. **Prueba para Datos Pareados**: Calcula \( t_0 \) para datos pareados, útil en estudios de antes y después.
5. **Prueba F para Igualdad de Varianzas**: Calcula \( f_0 \) para determinar si las varianzas de dos poblaciones son significativamente diferentes.
6. **Prueba de Igualdad de Proporciones**: Calcula \( z_0 \) para comparar las proporciones de dos poblaciones.
7. **Salir**: Cierra el programa.

## Instrucciones de Uso

1. Ejecuta el programa en un entorno de Python.
2. Selecciona una opción del menú según el tipo de prueba que deseas realizar.
3. Ingresa los datos requeridos cuando se te soliciten.
4. El programa mostrará el estadístico de prueba calculado para la opción seleccionada.

## Ejemplo de Uso

```
==CALCULADORA DE INFERENCIA ESTADISTICA A DOS POBLACIONES==
1. Diferencia de Medias con Varianzas Conocidas
2. Diferencia de Medias con Varianzas Desconocidas e Iguales
3. Diferencia de Medias con Varianzas Desconocidas y Diferentes
4. Prueba para Datos Pareados
5. Prueba F para Igualdad de Varianzas
6. Prueba de Igualdad de Proporciones
7. Salir

Ingrese una opción: 1
```

## Requisitos

- Python 3.x
- La biblioteca `math` (preinstalada con Python)

## Nota

Este programa incluye verificación de errores comunes, como división por cero, para asegurar un funcionamiento fluido.

## Licencia

Este proyecto es de código abierto y gratuito para su uso.
