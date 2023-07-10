import os
import time
import random
from userinterface.SubMenu import SubMenu

class Security:
    @staticmethod
    def menu():
        os.system("cls")
        while True:
            print("\n+-----------------------------------------------------+\n"+
                    "|               Módulo de Seguridad                   |\n"+
                    "+-----------------------------------------------------+\n"+
                    "| 1> Listar grupos de seguridad                       |\n"+
                    "| 2> Crear grupos de seguridad                        |\n"+
                    "| 3> Editar grupos de seguridad                       |\n"+
                    "| 4> Buscar grupos de seguridad                       |\n"+
                    "| 5> Borrar grupos de seguridad                       |\n"+
                    "| 6> Regresar                                         |\n"+
                    "+-----------------------------------------------------+\n")
            option=input("[.] Ingrese una opción:")

            match option:
                case "1":
                    Security.list_security_groups()
                case "2":
                    Security.create_security_groups()
                case "3":
                    Security.edit_security_group()
                case "4":
                    Security.search_security_group()
                case "5":
                    Security.delete_security_group()
                case "6":
                    SubMenu.return_admin_menu()
                    
                case ___:
                    print("\n[.] Invalid option. Try again.")
                    time.sleep(2)

    
    @staticmethod
    def list_security_groups():
        # este metodo llamara al meotod de ImageDao el cual realiza la consulta
        # este metodo formateo la respuesta de acuerdo al siguiente ejemplo
        print("\n+-----------------------------------------------------------------------------------------------------------------------------------+\n"+
                "|                                                         LISTA DE IMAGENES                                                         |\n"+
                "+-----------------------------------------------------------------------------------------------------------------------------------+\n"+
                "|    ID    |    NOMBRE       |   DESCRIPTION       |     RAM (MB) | DISK (GB) | vCPUs       |\n"+
                "|    1     |    my_flavor1   |    miembro          |     2048 | 2 | 2       |\n"+
                "|    2     |    my_flavor2   |    miembro          |     2048 | 2 | 2       |\n"+
                "|    3     |    my_flavor3   |    miembro          |     2048 | 2 | 1       |\n"+
                "|    4     |    my_flavor4   |    miembro          |     1024 | 1 | 1       |\n"+
                "|    5     |    my_flavor5   |    miembro          |     1024 | 1 | 1       |\n"+
                "+-----------------------------------------------------------------------------------------------------------------------------------+\n")
    
    @staticmethod
    def create_security_groups():
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
    def edit_security_group():
        
        Security.list_security_groups()
        username=input("[.] Ingrese el id del usuario que desee editar: ")

        print("\n+----------------------------------------------------------------------+\n"+
                "|                    EDITAR GRUPO DE SEGURIDAD                         |\n"+
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
    def search_security_group():
        while True:
            print("\n+----------------------------------------------------------------------+\n"+
                    "|                        BUSCAR GRUPO DE SEGURIDAD                                |\n"+
                    "+----------------------------------------------------------------------+")
            security_group_id=input("[.] Ingrese el id del grupo de seguridad: ")
            print("+----------------------------------------------------------------------+\n")
            
            # se hace el request al api de buscar grupo de seguridad
            if random.choice([True, False]):
                # si no se encuentra no muestra nada
                os.system("cls")
                print("[.] Grupo de seguridad encontrado exitosamente!")
                print("\n+--------------------------------------------------------------------+\n"+
                        "|                              GRUPO DE SEGURIDAD                      |\n"+
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
                print("[.] Grupo de seguridad no existe")


        
    @staticmethod
    def delete_security_group(): 
        Security.list_security_groups()
        image=input("[.] Ingrese el id del grupo de seguridad que desee borrar: ")
        
        while True:
            verification=input("[.] ¿Estás seguro de borrar el grupo de seguridad seleccionado? (S/N)")
            if verification=="S":
                # llama al api de borrar imagen
                print("[.] Grupo de seguridad borrado exitosamente!")
                break
            elif verification=="N":
                print("[.] Regresando al módulo de seguridad")
                Security.menu()
            else:
                print("[.] Ingrese una opción válida")

