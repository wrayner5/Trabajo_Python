contactos=[]
while True:
    print("===Agenda de Contactos===")
    print("1.Reguistrar contactos")
    print("2.Buscar contactos")
    print("3.Lista de contactos")
    print("4.Eliminar contactos")
    print("5.Salir")
    opcion=input("Ingrese su opcion:")
    if opcion == "1":
        nombre = input("Ingrese su nombre:")
        telefono = input("Ingrese su telefono:")
        contacto={
            "nombre":nombre,
            "telefono":telefono
        }
        contactos.append(contacto)
        print("Contacto registrado con exito")
    elif opcion =="2":
        buscar = input("Ingrese nombre a buscar:")
        encontrado = False
        for contacto in contactos:
            if contacto["nombre"].lower()==buscar.lower():
                print("Contacto Encontrado")
                print("Nombre:",contacto["nombre"])
                print("Telefono:",contacto["telefono"])
                encontrado= True
        if encontrado==False:
            print("Contacto no encontrado")
    elif opcion=="3":
        if len(contactos)== 0:
            print("No hay contactos")
        else:
            print("===lista de contactos===")
            for contacto in contactos:
                print("Nombre:",contacto["nombre"])
                print("Telefono:",contacto["telefono"])
    elif opcion=="4":
        eliminar = input("Nombre del contacto a eliminar:")
        eliminando = False
        for contacto in contactos:
            if contacto["nombre"].lower()==eliminar.lower():
                contactos.remove(contacto)
                print("Contacto eliminado correctamente")
                eliminando=True
                break
        if eliminando== False:
            print("Contacto no encontrado")
    elif opcion=="5":
        print("Saliendo del sistema")
        break
    else :
        print("Opcion no valida")
