saldo = 1000000
while True:
    print("---Cajero Automatico---")
    print("1.Revisar Saldo")
    print("2.Realizar Deposito")
    print("3.Retirar Saldo")
    print("4.Salir")
    opcion = input("Elija una opcion")
    if opcion=="1":
        print("Su saldo actual es:",saldo)
    elif opcion =="2":
        deposito =float(input("Ingrese el valor a depositar "))
        if deposito > 0 :
            saldo =saldo + deposito
            print ("Deposito realizado con exito")
            print("Su nuevo saldo es:",saldo)
        else:
            print("transeferencia no realizada")
    elif opcion=="3":
        retiro =float(input("Ingrese el valor a retirar"))
        if retiro > saldo:
            print("Fondos Insuficientes")
        elif  retiro <= 0:
            print("Retiro no realizado")
        else:
            saldo-=retiro 
            print("Retiro realizado con exito")
            print("Su nuevo saldo es:",saldo)
    elif opcion=="4":
        print("Grasias por usar este cajero automatico")
        break
    else:
        print("Opcion no valida")
