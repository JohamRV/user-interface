import os
import time
from userinterface.SubMenu import SubMenu
class Image:
    
    @staticmethod
    def menu():
        os.system("cls")
        while True:
            print("\n+-----------------------------------------------------+\n"+
                    "|                  Módulo de Imágenes                 |\n"+
                    "+-----------------------------------------------------+\n"+
                    "| 1>  Listar Imágenes                                 |\n"+
                    "| 2>  Importar Imágenes                               |\n"+
                    "| 3>  Editar Imágenes                                 |\n"+
                    "| 4>  Buscar Imágenes                                 |\n"+
                    "| 5>  Borrar Imágenes                                 |\n"+
                    "| 6>  Regresar                                        |\n"+
                    "+-----------------------------------------------------+\n")
            option=input("[.] Ingrese una opción:")

            match option:
                case "1":
                    Image.list_images()
                case "2":
                    Image.create_image()
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case "6":
                    print("\n[.] Regresando al home.")
                    SubMenu.return_admin_menu()
                    
                case ___:
                    print("\n[.] Opción inválida. Intente de nuevo.")
                    time.sleep(2)

    @staticmethod
    def list_images():
        # este metodo llamara al meotod de ImageDao el cual realiza la consulta
        # este metodo formateo la respuesta de acuerdo al siguiente ejemplo
        print("\n+-----------------------------------------------------------------------------------------------------------------------------------+\n"+
                "|                                                         LISTA DE IMAGENES                                                         |\n"+
                "+-----------------------------------------------------------------------------------------------------------------------------------+\n"+
                "|    ID    |    NOMBRE    |   DESCRIPTION       |     RAM (MB) | DISK (GB) | vCPUs       |\n"+
                "|    1     |    my_flavor1   |    miembro          |     2048 | 2 | 2       |\n"+
                "|    2     |    my_flavor2   |    miembro          |     2048 | 2 | 2       |\n"+
                "|    3     |    my_flavor3   |    miembro          |     2048 | 2 | 1       |\n"+
                "|    4     |    my_flavor4   |    miembro          |     1024 | 1 | 1       |\n"+
                "|    5     |    my_flavor5   |    miembro          |     1024 | 1 | 1       |\n"+
                "+-----------------------------------------------------------------------------------------------------------------------------------+\n")
    
    @staticmethod
    def import_image():
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
    def edit_image():
        
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
    def search_image():
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
    def delete_image(): 
        Image.list_images()
        image=input("[.] Ingrese el id del flavor que desee borrar: ")
        
        while True:
            verification=input("[.] ¿Estás seguro de borrar la imagen seleccionado? (S/N)")
            if verification=="S":
                # llama al api de borrar imagen
                print("[.] Imagen borrada exitosamente!")
                break
            elif verification=="N":
                print("[.] Regresando al módulo de imágenes")
                Image.menu()
            else:
                print("[.] Ingrese una opción válida")

