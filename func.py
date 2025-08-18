
def datos():
    sexo = input("Por favor ingrese su sexo (hombre/mujer): ").lower()
    if sexo == "hombre":
        edad = int(input("Ingrese su edad: "))
        if edad >= 60:
            print("Ingreso permitido")
            print("Ingrese sus datos personales para acceder a su cuenta")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            domicilio = input("Domicilio: ")
            print(f"Datos guardados: {nombre} {apellido}, DNI: {dni}, Domicilio: {domicilio}")
            print("Bienvenido al PAMI señor jubilado")
        else:
            print("Ingreso no permitido, debe ser mayor o igual a 60 años")
    elif sexo == "mujer":
        print("No esta permitido sexo femenino en el equipo masculino")
    else:
        print("Sexo no reconocido. Por favor ingrese 'hombre' o 'mujer'.")
def decir_nombre():
    print ("Tu sueldo de Jubilado es de 1000000 ARS")
datos()
decir_nombre()



