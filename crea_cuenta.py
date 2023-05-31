#import usuarios
#import programa0
import contrasena

#********** FUNCION QUE DEVUELVA: NUMERO DE CUENTA, PASSWORD, Y TELEFONO

def creando(x, y):  
    n_cuenta = y + 1000
    p_cuenta = contrasena.password_generator(8)

    a = 0
    while a == 0:
        print("")
        print(f"Ingrese numero telefonico de el Sr. o Sra. {x}")
        print("-----------------------------------------------------------------")
        telefono = input("Telefono  (8 digitos) : ")
        if any([c.isdigit() for c in telefono]) == True:
            if len(telefono) == 8:
                f_cuenta = telefono
                a = 1
            else:
                print("Please, numero telefonico debe contener 8 numeros")
        else:
            print("Please, numero telefonico debe ser solo numeros")
        print("")
        
    return [n_cuenta, p_cuenta, f_cuenta]

