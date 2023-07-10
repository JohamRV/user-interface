import os
import time
from userinterface.SubMenu import SubMenu

class Flavor:
    
    @staticmethod
    def menu():
        os.system("cls")
        while True:
            print("\n+-----------------------------------------------------+\n"+
                    "|                  Módulo de Flavors                  |\n"+
                    "+-----------------------------------------------------+\n"+
                    "| 1>  Listar Flavors                                  |\n"+
                    "| 2>  Crear Flavors                                   |\n"+
                    "| 3>  Editar Flavors                                  |\n"+
                    "| 4>  Buscar Flavors                                  |\n"+
                    "| 5>  Borrar Flavors                                  |\n"+
                    "| 6>  Regresar                                        |\n"+
                    "+-----------------------------------------------------+\n")
            option=input("[.] Ingrese una opción:")

            match option:
                case "1":
                    Flavor.list_users()
                case "2":
                    Flavor.create_user()
                case "3":
                    Flavor.edit_user()
                case "4":
                    Flavor.search_user()
                case "5":
                    Flavor.delete_user()
                case "6":
                    print("\n[.] Regresando al home.")
                    SubMenu.return_admin_menu()
                    
                case ___:
                    print("\n[.] Opción inválida. Intente de nuevo.")
                    time.sleep(3)

    @staticmethod
    def list_flavors():
        # este metodo llamara al meotod de FlavorDao el cual realiza la consulta
        # este metodo formateo la respuesta de acuerdo al siguiente ejemplo
        print("\n+-----------------------------------------------------------------------------------------------------------------------------------+\n"+
                "|                                                         LISTA DE FLAVORS                                                         |\n"+
                "+-----------------------------------------------------------------------------------------------------------------------------------+\n"+
                "|    ID    |    NOMBRE    |   DESCRIPTION       |     RAM (MB) | DISK (GB) | vCPUs       |\n"+
                "|    1     |    my_flavor1   |    miembro          |     2048 | 2 | 2       |\n"+
                "|    2     |    my_flavor2   |    miembro          |     2048 | 2 | 2       |\n"+
                "|    3     |    my_flavor3   |    miembro          |     2048 | 2 | 1       |\n"+
                "|    4     |    my_flavor4   |    miembro          |     1024 | 1 | 1       |\n"+
                "|    5     |    my_flavor5   |    miembro          |     1024 | 1 | 1       |\n"+
                "+-----------------------------------------------------------------------------------------------------------------------------------+\n")
    
    @staticmethod
    def create_flavor():
        print("\n+----------------------------------------------------------------------+\n"+
                "|                        CREAR USUARIO                                 |\n"+
                "+----------------------------------------------------------------------+")
        username=input("[.] Ingrese el nombre del usuario: ")
        email=input("[.] Ingrese el email del usuario: ")
        description=input("[.] Ingrese una descripción para el usuario: ")
        password=input("[.] Ingrese una contraseña para el usuario: ")
        print("+----------------------------------------------------------------------+\n") 
        
        #SubMenu.show_slices()
        #proyect=input("[.] Ingrese el id del proyecto: ")

        print("\n+-----------------------------------------------------------------------------------------------------------------------------------+\n"+
                "|                                                         LISTA DE USUARIOS                                                         |\n"+
                "+-----------------------------------------------------------------------------------------------------------------------------------+\n"+
                "|    ID    |    NOMBRE    |    ROL              |               EMAIL                |                   DESCRIPTION                |\n"+
                "|    1     |    melanie   |    miembro          |        melanie@pucp.edup.pe        |        Usuario para el curso de Cloud        |\n"+
                "|    2     |    joham     |    administrador    |        jromucho@pucp.edu.pe        |        Usuario para el curso de Redes        |\n"+
                "+-------------------------------------------------------------------------------------------------------------- --------------------+\n")
    

        enabled=True
        print(f"[.] Usuario {username} creado exitsoamente!")

    @staticmethod
    def edit_flavor():
        
        User.list_users()
        username=input("[.] Ingrese el id del usuario que desee editar: ")

        print("\n+----------------------------------------------------------------------+\n"+
                "|                        EDITAR USUARIO                                 |\n"+
                "+----------------------------------------------------------------------+")
        username=input("[.] Ingrese el nuevo nombre del usuario: ")
        email=input("[.] Ingrese el nuevo email del usuario: ")
        description=input("[.] Ingrese una nueva descripción para el usuario: ")
        print("+----------------------------------------------------------------------+\n")
        
        SubMenu.show_slices()
        proyect=input("[.] Ingrese el id del proyecto: ")
        
        enabled=True
        print(f"[.] Usuario {username} editado exitsoamente!")

    @staticmethod
    def search_flavor():
        while True:
            print("\n+----------------------------------------------------------------------+\n"+
                    "|                        BUSCAR USUARIO                                |\n"+
                    "+----------------------------------------------------------------------+")
            username=input("[.] Ingrese el nombre del usuario: ")
            email=input("[.] Ingrese el email del usuario: ")
            print("+----------------------------------------------------------------------+\n")
            
            if random.choice([True, False]):
                # si no se encuentra no muestra nada
                os.system("cls")
                print("[.] Usuario encontrado exitosamente!")
                print("\n+--------------------------------------------------------------------+\n"+
                        "|                              USUARIO                                 |\n"+
                        "+----------------------------------------------------------------------+\n"+
                        "| [.] ID de usuario: 1                                                 |\n"+
                        "| [.] Nombre de usuario: melanie                                       |\n"+
                        "| [.] Rol de usuario: miembro                                          |\n"+
                        "| [.] Email de usuario: melanie@pucp.edup.pe                           |\n"+
                        "| [.] Descripción de usuario: Usuario perteneciente al grupo de cloud  |\n"+
                        "| [.] Estado del usuario: Activo                                       |\n"+
                        "+---------------------------------------------------------------------+\n")
                break
            else:
                print("[.] Usuario no existe")


        
    @staticmethod
    def delete_flavor(): 
        Flavor.list_flavors()
        flavor=input("[.] Ingrese el id del flavor que desee borrar: ")
        
        while True:
            verification=input("[.] ¿Estás seguro de borrar el flavor seleccionado? (S/N)")
            if verification=="S":
                # llama al api de borrar flavor
                print("[.] Flavor borrado exitosamente!")
                break
            elif verification=="N":
                print("[.] Regresando al módulo de usuarios")
                Flavor.menu()
            else:
                print("[.] Ingrese una opción válida")

