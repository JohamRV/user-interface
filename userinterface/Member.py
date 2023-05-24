import os
import sys
import time
from userinterface.Slice import Slice
from userinterface.Network import Network

class Member:
    
    def __init__() -> None:
        pass

    def __init__(self, username) -> None:
        self.username = username

    @staticmethod
    def menu():
        os.system("cls")
        
        while True:
            print("\n+-----------------------------------------------------+\n"+
                "|                 Home del Miembro                    |\n"+
                "+-----------------------------------------------------+\n"+
                "| 1> Ver slices                                       |\n"+
                "| 2> Módulo de networking                             |\n"+
                "| 3> Cerrar sesión                                    |\n"+
                "+-----------------------------------------------------+\n")
        
            option=input("[.] Ingrese una opción: ")

            match option:
                case "1":
                    # must list slices for an specific user
                    Slice.list_slices_by_username() # str: username
                case "2":
                    
                    pass
                case "3":
                    print("\n[.] Cerrando sesión.")
                    sys.exit()
                    break
                case __:
                    print("\n[.] Opción inválida. Intente de nuevo.")
                    time.sleep(2)