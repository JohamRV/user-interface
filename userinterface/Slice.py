import time
import os
from userinterface.SubMenu import SubMenu
from dao.SliceDao import SliceDao
from prettytable import PrettyTable
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
        slice = SliceDao()
        slices=slice.list_slices().json()
        print(slices)
        print("\n+---------------------------------------------+\n"+
              "|                    SLICES                   |\n"+
              "+---------------------------------------------+")
        for slice in slices:
            if not slice["status"] : 
                status = "INACTIVO"
            else:
                status = "ACTIVO"
            print("| ID: "+str(slice["sliceId"])) 
            print("| NOMBRE : "+slice["sliceName"]) 
            print("| DESCRIPCIÓN : "+slice["description"]) 
            print("| ESTADO : "+ status)
            print("+---------------------------------------------+")
    
    @staticmethod
    def list_slices_by_username():
        slice = SliceDao()
        try:
            slice_found = slice.list_slice_by_username().json()
            
            if not slice_found["status"] : 
                status = "INACTIVO"
            else:
                status = "ACTIVO"
            print("\n+---------------------------------------------+\n"+
                "|                    SLICES                   |\n"+
                "+---------------------------------------------+")
            print("| ID: "+str(slice_found["sliceId"])) 
            print("| NOMBRE : "+slice_found["sliceName"]) 
            print("| DESCRIPCIÓN : "+slice_found["description"]) 
            print("| ESTADO : "+ status)
            print("+---------------------------------------------+")
        except KeyError:
            print("[.] Usuario no tiene slices")


    @staticmethod
    def delete_slice():
        Slice.list_slices()
        sliceId=input("[.] Ingrese el id del slice que desee borrar: ")
        
        while True:
            verification=input("[.] ¿Estás seguro de borrar el proyecto seleccionado? (S/N)")
            if verification=="S":
                # llama al api de borrar SLICE 
                # Borrado automático independientemente del cluster
                slice = SliceDao()
                slice_delte_res = slice.delete_slice_by_id(sliceId)
                if slice_delte_res.status_code == 200:
                    print("[.] Slice borrado exitosamente!")
                    break
                else:
                    print("[.] Hubo un error al borrar la slice. Intente nuevamente.")
                    continue
            elif verification=="N":
                print("[.] Regresando al módulo de slices")
                Slice.menu()
            else:
                print("[.] Ingrese una opción válida")

    @staticmethod
    def search_slice():
        print("\n+----------------------------------------------------------------------+\n"+
                "|                        BUSCAR SLICE                                  |\n"+
                "+----------------------------------------------------------------------+")
        slice_id=input("[.] Ingrese el id del slice: ")
        print("+----------------------------------------------------------------------+\n")
            
        slice = SliceDao()
        try:
            slice_found = slice.list_slices_by_id(slice_id).json()
            if not slice_found["status"] : 
                status = "INACTIVO"
            else:
                status = "ACTIVO"
            print("\n+---------------------------------------------+\n"+
                "|                    SLICES                   |\n"+
                "+---------------------------------------------+")
            print("| ID: "+str(slice_found["sliceId"])) 
            print("| NOMBRE : "+slice_found["sliceName"]) 
            print("| DESCRIPCIÓN : "+slice_found["description"]) 
            print("| ESTADO : "+ status)
            print("+---------------------------------------------+")
        except KeyError :
            print("[.] Slice no existe")

    @staticmethod
    def edit_slice():
        Slice.list_slices()
        sliceId = input("[.] Ingrese el id del slice que desee editar: ")

        print("\n+----------------------------------------------------------------------+\n"+
                "|                        EDITAR SLICE                                  |\n"+
                "+----------------------------------------------------------------------+")
        new_name=input("[.] Ingrese el nuevo nombre de la slice: ")
        new_desc=input("[.] Ingrese la nueva descripción: ")
        print("+----------------------------------------------------------------------+\n")
        slice = SliceDao()
        i = 0
        while i < 3:
            edit_slice_res = slice.edit_slice(sliceId, new_name, new_desc)
            print(edit_slice_res.json())
            if edit_slice_res.status_code == 200:
                print(f"[.] Slice {new_name} editado exitsoamente!")
                break
            else:
                print(f"[.] Ocurrió un error al editar la slice. ")
                i = i + 1
                continue
            
    @staticmethod
    def create_slice():
        print("\n+----------------------------------------------------------------------+\n"+
                "|                        CREAR SLICE                                   |\n"+
                "+----------------------------------------------------------------------+")
        name=input("[.] Ingrese el nombre de la slice: ")
        description=input("[.] Ingrese la descripción: ")
        print("+----------------------------------------------------------------------+\n")
        
        slice = SliceDao()
        slice_res = slice.create_slice(name, description)
        slice_id = slice_res.json()["sliceId"]

        # lista usuarios 
        SubMenu.show_users()
        user_id=input("[.] Ingrese el id del usuario al que se le asignará: ")

        assign_slice_res = slice.assign_slice(user_id, slice_id).json()

        print(assign_slice_res)

        SubMenu.go_topology_menu()

        print(f"[.] Slice {name} creado exitosamente!")  