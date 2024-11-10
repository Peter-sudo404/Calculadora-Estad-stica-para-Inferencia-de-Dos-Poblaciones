# Autor: Anonimo
# Fecha de última edición: 09/11/2024
# Dedicatoria: Para todos los que se quieren facilitar la vida
import math

iniciador = True
while iniciador:
    print("==CALCULADORA DE INFERENCIA ESTADISTICA A DOS POBLACIONES==")
    print("1. Diferencia de Medias con Varianzas Conocidas")
    print("2. Diferencia de Medias con Varianzas Desconocidas e Iguales")
    print("3. Diferencia de Medias con Varianzas Desconocidas y Diferentes")
    print("4. Prueba para muestras/datos pareadas")
    print("5. Prueba f para determinar si las Varianzas poblacionales son iguales")
    print("6. Prueba de igualdad de proporciones poblacionales")
    print("7. Salir")
    print()
    opcion = input("Ingrese una opcion: ")
    
    if opcion == "1":
        print("----------------------------------------------------------------------------")
        print()
        ## DIF de Medias VARIANZA CONOCIDAS
        # Datos
        n_1 = float(input("Ingrese tamaño de la muestra 1:"))
        x_1 = float(input("Ingrese media muestral 1:"))
        sigma_1 = float(input("Ingrese varianza poblacional 1:"))
        n_2 = float(input("Ingrese tamaño de la muestra 2:"))
        x_2 = float(input("Ingrese media muestral 2:"))
        sigma_2 = float(input("Ingrese varianza poblacional 2:"))
        delta_0 = float(input("Ingrese delta sub cero:"))
        
        # Para el valor de z_0
        z_0 = (x_1 - x_2 - delta_0) / math.sqrt((sigma_1) / n_1 + (sigma_2) / n_2)
        print("z_0 es:", z_0)
        print()
        
    elif opcion == "2":
        print("----------------------------------------------------------------------------")
        print()
        ## DIF de Medias DESCONOCIDAS PERO IGUALES
        # Datos
        n_1 = float(input("Ingrese tamaño de la muestra 1:"))
        x_1 = float(input("Ingrese media muestral 1:"))
        s_1 = float(input("Ingrese desvest muestral 1:"))
        n_2 = float(input("Ingrese tamaño de la muestra 2:"))
        x_2 = float(input("Ingrese media muestral 2:"))
        s_2 = float(input("Ingrese desvest muestral 2:"))
        delta_0 = float(input("Ingrese delta sub cero:"))
        
        # Para el valor de s_p^2
        s_p2 = ((n_1 - 1) * s_1**2 + (n_2 - 1) * s_2**2) / (n_1 + n_2 - 2)
        print("s_p^2 es:", s_p2)

        # Para el valor de t_0 usando s_p
        s_p = math.sqrt(s_p2)
        t_0 = (x_1 - x_2 - delta_0) / (s_p * math.sqrt(1 / n_1 + 1 / n_2))
        print("t_0 es:", t_0)
        print()
        
    elif opcion == "3":
        print("----------------------------------------------------------------------------")
        print()
        ## DIF de Medias VARIANZA DESCONOCIDAS Y DIFERENTES
        # Datos
        n_1 = float(input("Ingrese tamaño de la muestra 1:"))
        x_1 = float(input("Ingrese media muestral 1:"))
        s_1 = float(input("Ingrese desvest muestral 1:"))
        n_2 = float(input("Ingrese tamaño de la muestra 2:"))
        x_2 = float(input("Ingrese media muestral 2:"))
        s_2 = float(input("Ingrese desvest muestral 2:"))
        delta_0 = float(input("Ingrese delta sub cero:"))
        
        # Para el valor t_0
        t_0_2 = (x_1 - x_2 - delta_0) / math.sqrt((s_1**2) / n_1 + (s_2**2) / n_2)
        print("t_0 es:", t_0_2)

        # Para el valor Nu (V)
        V = ((s_1**2 / n_1 + s_2**2 / n_2) ** 2) / ((s_1**2 / n_1) ** 2 / (n_1 - 1) + (s_2**2 / n_2) ** 2 / (n_2 - 1))
        print("Nu (V) es:", V)
        print()
        
    elif opcion == "4":
        print("----------------------------------------------------------------------------")
        print()
        # Datos para datos pareados
        print("OJO: PARA LOS DATOS PAREADOS, LAS DIFERENCIAS SON: VARIABLE_2 - VARIABLE_1")
        print()
        n = float(input("Ingrese tamaño de la muestra:"))
        d_bar = float(input("Ingrese la media de las diferencias:"))  
        s_D = float(input("Ingrese la desvest de las diferencias:"))
        delta_0 = float(input("Ingrese delta sub cero:"))

        # Para el valor de t_0
        t_0 = (d_bar - delta_0) / (s_D / math.sqrt(n))
        print("t_0 es:", t_0)
        print()
        
    elif opcion == "5":
        print("----------------------------------------------------------------------------")
        print()
        # Datos para la prueba F
        s_1 = float(input("Ingrese desvest muestral 1:"))
        s_2 = float(input("Ingrese desvest muestral 2:"))

        # Para el valor de f_0
        f_0 = (s_1**2) / (s_2**2)
        print("f_0 es:", f_0)
        print()
        
    elif opcion == "6":
        print("----------------------------------------------------------------------------")
        print()
        # Datos para prueba de proporciones
        n_1 = float(input("Ingrese tamaño de la muestra 1:"))
        valor_x_1 = float(input("Ingrese numero de éxitos en la muestra 1:"))
        p_m_1 = valor_x_1 / n_1
        n_2 = float(input("Ingrese tamaño de la muestra 2:"))
        valor_x_2 = float(input("Ingrese numero de éxitos en la muestra 2:"))
        p_m_2 = valor_x_2 / n_2
        delta_0 = float(input("Ingrese delta sub cero:"))
        
        # Estimador puntual insesgado ponderado de proporcion
        ep_i_pp = (valor_x_1 + valor_x_2) / (n_1 + n_2)

        # Cálculo de z_0
        z_0_2 = (p_m_1 - p_m_2 - delta_0) / math.sqrt(ep_i_pp * (1 - ep_i_pp) * (1 / n_1 + 1 / n_2))
        print("z_0 es:", z_0_2)
        print()
        
    elif opcion == "7":
        iniciador = False
    
    else:
        print("Opción inválida... Inténtelo de nuevo")
        print()
