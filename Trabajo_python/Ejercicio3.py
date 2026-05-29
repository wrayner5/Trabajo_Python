productos=[]
while True : 
    print("---Control de Inventario")
    print("1. Reguistrar productos ")
    print("2.Consultar productos ")
    print("3.Buscar Productos")
    print("4.Calcular Valor Total del Inventario")
    print("5. Salir")
    opcion = (input("Seleciona una opcion"))
    if opcion =="1":
        nombre = input("Colocar en nombre del producto:")
        precio = float(input("Coloca en precio del producto:"))
        cantidad = int(input("Coloca la cantidad de los productos:"))
        producto ={
            "nombre":nombre,
            "precio":precio,
            "cantidad":cantidad,
        }
        productos.append(producto)
        print("Productos Registrado con Exito")
    elif opcion=="2":
        if len(productos)==0:
            print("No hay productos registrados.")
        else :
            print("---Listado de productos---")
            for producto in productos:
                print("Nombre:",producto["nombre"])
                print("Precio:",producto["precio"])
                print("Cantidad:",producto["cantidad"])
                print("------------------------")
    elif opcion=="3":
        buscar= input("Ingrese el nombre del producto a buscar")
        encontrado=False
        for producto in productos:
            if producto["nombre"].lower()==buscar.lower():
                print("---Producto Encontrado")
                print("Nombre:",producto["nombre"])
                print("Precio:",producto["precio"])
                print("Cantidad:",producto["cantidad"])
            encontrado= True
        if encontrado==False:
            print("Producto no encontrado")
    elif opcion=="4":
        total = 0
        for producto in productos:
            total +=producto["precio"]*producto["cantidad"]
            print("El valor del inventario es : ",total)
    elif opcion=="5":
        print("Saliendo del sistema ")
        break
    else :
        print("Opcion no valida")
         