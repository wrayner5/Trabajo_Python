while True:
    print("----Analizador de Texto----")
    print("1.Analizar el texto")
    print("2.Salir")
    opcion = input("Selecione una opcion")
    if opcion=="1":
        texto= input("Ingrese el texto")
        caracteres = len(texto)
        palabras = len(texto.split())
        vocales = 0 
        for letra in texto.lower():
            if letra =="a" or letra=="e" or letra =="i" or letra =="o" or letra =="u":
                vocales += 1
        print("Resultado de Analizis")
        print("Cantidad de caracteres:",caracteres)
        print("Cantidad de palabras:",palabras)
        print("Cantidad de vocales:",vocales)
        print("Palabra en Mayuscula:",texto.upper())
        print("Palabra en Miniscula:",texto.lower())
    elif opcion=="2":
        print("Saliendo del programa....")
        break
    else:
        print("Opcion no valida")
