import time
import os
from userinterface.SubMenu import SubMenu
import random

class Slice:
    
    @staticmethod
    def menu():
        os.system("cls")
        while True:
            print("\n+-----------------------------------------------------+\n"+
                "|                  Módulo de Slices                   |\n"+
                "+-----------------------------------------------------+\n"+
                "| 1> Listar slices                                    |\n"+
                "| 2> Crear slices                                     |\n"+
                "| 3> Editar slices                                    |\n"+
                "| 4> Buscar slices                                    |\n"+
                "| 5> Borrar slices                                    |\n"+
                "| 6> Regresar                                         |\n"+
                "+-----------------------------------------------------+\n")
    
            option=input("[.] Ingrese una opción:")

            match option:
                case "1":
                    Slice.list_slices()
                case "2":
                    Slice.create_slice()
                case "3":
                    Slice.edit_slice()
                case "4":
                    Slice.search_slice()
                case "5":
                    Slice.delete_slice()
                case "6":
                    print("\n[.] Regresando al home.")
                    SubMenu.return_admin_menu()
                    
                case ___:
                    print("\n[.] Opción inválida. Intente de nuevo.")
                    time.sleep(2)

    @staticmethod
    def list_slices():
        # this method call the function list slices
        # and format the response into text to show
        print("\n+---------------------------------------------+\n"+
              "|                    SLICES                   |\n"+
              "+---------------------------------------------+\n"+
              "|    ID    |    PROYECTO   |      ESTADO      |\n"+
              "|    1     |      Cloud    |        ON        |\n"+
              "|    2     |       SDN     |       OFF        |\n"+
              "|    3     |     Tráfico   |        ON        |\n"+
              "+---------------------------------------------+")
    
    @staticmethod
    def list_slices_by_username():
        print("\n+---------------------------------------------+\n"+
              "|                    SLICES                   |\n"+
              "+---------------------------------------------+\n"+
              "|    ID    |    PROYECTO   |      ESTADO      |\n"+
              "|    1     |      Cloud    |        ON        |\n"+
              "|    2     |       SDN     |       OFF        |\n"+
              "|    3     |     Tráfico   |        ON        |\n"+
              "+---------------------------------------------+")

    @staticmethod
    def delete_slice():
        Slice.list_slices()
        slice=input("[.] Ingrese el id del slice que desee borrar: ")

        while True:
            verification=input("[.] ¿Estás seguro de borrar el proyecto seleccionado? (S/N)")
            if verification=="S":
                # llama al api de borrar SLICE 
                # Borrado automático independientemente del cluster
                print("[.] Slice borrado exitosamente!")
                break
            elif verification=="N":
                print("[.] Regresando al módulo de slices")
                Slice.menu()
            else:
                print("[.] Ingrese una opción válida")

    @staticmethod
    def search_slice():
        while True:
            print("\n+----------------------------------------------------------------------+\n"+
                    "|                        BUSCAR SLICE                                  |\n"+
                    "+----------------------------------------------------------------------+")
            id_slice=input("[.] Ingrese el id del slice: ")
            slice=input("[.] Ingrese el nombre de la slice: ")
            print("+----------------------------------------------------------------------+\n")
            
            if random.choice([True, False]):
                # si no se encuentra no muestra nada
                os.system("cls")
                print("[.] Slice encontrada exitosamente!")
                print("\n+----------------------------------------------------------------------+\n"+
                        "|                              SLICE                                   |\n"+
                        "+----------------------------------------------------------------------+\n"+
                        "| [.] ID de slice: 1                                                   |\n"+
                        "| [.] Nombre de la slice: Cloud                                        |\n"+
                        "| [.] Descripción de la slice: Creada para el curso de Cloud           |\n"+
                        "| [.] Estado de la slice: ON                                           |\n"+
                        "| [.] Dueño de la slice: melanie                                       |\n"+
                        "| [.] Fecha de creación: 15/05/2022                                    |\n"+
                        "+---------------------------------------------------------------------+\n")
                break
            else:
                print("[.] Slice no existe")

    @staticmethod
    def edit_slice():
        Slice.list_slices()
        slice=input("[.] Ingrese el id del slice que desee editar: ")

        print("\n+----------------------------------------------------------------------+\n"+
                "|                        EDITAR SLICE                                  |\n"+
                "+----------------------------------------------------------------------+")
        new_name=input("[.] Ingrese el nuevo nombre de la slice: ")
        new_desc=input("[.] Ingrese la nueva descripción: ")
        new_state=input("[.] Ingrese el nuevo estado: ")
        print("+----------------------------------------------------------------------+\n")
        
        print(f"[.] Slice {new_name} editado exitsoamente!")

    @staticmethod
    def create_slice():
        print("\n+----------------------------------------------------------------------+\n"+
                "|                        CREAR SLICE                                   |\n"+
                "+----------------------------------------------------------------------+")
        name=input("[.] Ingrese el nombre de la slice: ")
        desc=input("[.] Ingrese la descripción: ")
        state=input("[.] Ingrese el estado: ")
        print("+----------------------------------------------------------------------+\n")
        
        SubMenu.show_users()
        user_id=input("[.] Ingrese el id del usuario al que se le asignará: ")


        print(f"[.] Slice {name} editado exitsoamente!")