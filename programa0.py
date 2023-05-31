import usuarios
import crea_cuenta
import time

cuenta = 100000
clientes_virtual = []
for i in range(len(usuarios.super_heroes)):  
    salida = crea_cuenta.creando(usuarios.super_heroes[i][1], cuenta)  
    cuenta = salida[0]
    clientes_virtual.append([
        usuarios.super_heroes[i][0], 
        usuarios.super_heroes[i][1], 
        usuarios.super_heroes[i][2], 
        usuarios.super_heroes[i][3], 
        usuarios.super_heroes[i][4], 
        usuarios.super_heroes[i][5], 
        usuarios.super_heroes[i][6], 
        usuarios.super_heroes[i][7], 
        salida[0],
        salida[1],
        salida[2]
        ])

print("")
print("                                                                                                     USUARIOS, Super heroes y heroinas")
print("+------+-------------------------+-------------------------------------+--------------------------------------+---------------------------------------+------------+------+-------------+------------+----------+----------+")
print("|Codigo| Nombre                  |  Ocupación                          | Correo                               | Direccion                             | Nacimiento | Edad |Clave Usuario| N° cuenta  | password | Telefono |")
print("+------+-------------------------+-------------------------------------+--------------------------------------+---------------------------------------+------------+------+-------------+------------+----------+----------+")
for i in range(len(clientes_virtual)):  
    #limite_prod = len(clientes_virtual)
    cadena = "|{:6}|{:25}|{:37}|{:38}|{:39}|{:12}|{:6}|{:13}|{:12}|{:10}|{:10}|".format(
        clientes_virtual[i][0], 
        clientes_virtual[i][1], 
        clientes_virtual[i][2],
        clientes_virtual[i][3], 
        clientes_virtual[i][5], 
        clientes_virtual[i][6],
        clientes_virtual[i][7], 
        clientes_virtual[i][4], 
        clientes_virtual[i][8],
        clientes_virtual[i][9], 
        clientes_virtual[i][10]
        )
    print(cadena)
    print("+------+-------------------------+-------------------------------------+--------------------------------------+---------------------------------------+------------+------+-------------+------------+----------+----------+")
    time.sleep(1)

print("")
print("")
#'{:10,.0f}'.format(clientes_virtual[i][3]), '{:10,.0f}'.format(clientes_virtual[i][4])
