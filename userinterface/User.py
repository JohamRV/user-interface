import os
import time
import random
from userinterface.SubMenu import SubMenu
class User:

    @staticmethod
    def menu():
        os.system("cls")
        while True:
            print("\n+-----------------------------------------------------+\n"+
                    "|                  Módulo de Usuarios                 |\n"+
                    "+-----------------------------------------------------+\n"+
                    "| 1>  Listar Usuario                                  |\n"+
                    "| 2>  Crear Usuario                                   |\n"+
                    "| 3>  Editar Usuario                                  |\n"+
                    "| 4>  Buscar Usuario                                  |\n"+
                    "| 5>  Borrar Usuario                                  |\n"+
                    "| 6>  Regresar                                        |\n"+
                    "+-----------------------------------------------------+\n")
            option=input("[.] Ingrese una opción:")

            match option:
                case "1":
                    User.list_users()
                case "2":
                    User.create_user()
                case "3":
                    User.edit_user()
                case "4":
                    User.search_user()
                case "5":
                    User.delete_user()
                case "6":
                    print("\n[.] Regresando al home.")
                    SubMenu.return_admin_menu()
                    
                case ___:
                    print("\n[.] Opción inválida. Intente de nuevo.")
                    time.sleep(3)

    @staticmethod
    def list_users():
        # este metodo llamara al meotod de UserDao el cual realiza la consulta
        # este metodo formateo la respuesta de acuerdo al siguiente ejemplo
        print("\n+-----------------------------------------------------------------------------------------------------------------------------------+\n"+
                "|                                                         LISTA DE USUARIOS                                                         |\n"+
                "+-----------------------------------------------------------------------------------------------------------------------------------+\n"+
                "|    ID    |    NOMBRE    |    ROL              |               EMAIL                |                   DESCRIPTION                |\n"+
                "|    1     |    melanie   |    miembro          |        melanie@pucp.edup.pe        |        Usuario para el curso de Cloud        |\n"+
                "|    2     |    joham     |    administrador    |        jromucho@pucp.edu.pe        |        Usuario para el curso de Redes        |\n"+
                "|    3     |    emerson   |    miembro          |        emerson@pucp.edu.pe         |        Usuario para el curso de Cloud        |\n"+
                "|    4     |    fernando  |    administrador    |          fguzman@pucp.pe           |        Usuario para el curso de SDN          |\n"+
                "|    5     |    luis      |    miembro          |          luis@gmail.com            |        Usuario para el curso de Cloud        |\n"+
                "|    6     |    josé      |    administrador    |            jose@gmail.com          |                Administradro de red          |\n"+
                "+-------------------------------------------------------------------------------------------------------------- --------------------+\n")
    
    @staticmethod
    def create_user():
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
    def edit_user():
        
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
    def search_user():
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
    def delete_user(): 
        User.list_users()
        username=input("[.] Ingrese el id del usuario que desee borrar: ")
        
        while True:
            verification=input("[.] ¿Estás seguro de borrar el usuario seleccionado? (S/N)")
            if verification=="S":
                # llama al api de borrar usuario
                print("[.] Usuario borrado exitosamente!")
                break
            elif verification=="N":
                print("[.] Regresando al módulo de usuarios")
                User.menu()
            else:
                print("[.] Ingrese una opción válida")