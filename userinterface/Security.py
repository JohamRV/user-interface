import os
import time
from userinterface.SubMenu import SubMenu

class Security:
    @staticmethod
    def menu():
        os.system("cls")
        while True:
            print("\n+-----------------------------------------------------+\n"+
                    "|               Módulo de Seguridad                   |\n"+
                    "+-----------------------------------------------------+\n"+
                    "| 1> Grupos de seguridad                              |\n"+
                    "| 2> Crear slices                                     |\n"+
                    "| 3> Editar slices                                    |\n"+
                    "| 4> Buscar slices                                    |\n"+
                    "| 5> Borrar slices                                    |\n"+
                    "| 6> Regresar                                         |\n"+
                    "+-----------------------------------------------------+\n")
            option=input("[.] Ingrese una opción:")

            match option:
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case "6":
                    SubMenu.return_admin_menu()
                    
                case ___:
                    print("\n[.] Invalid option. Try again.")
                    time.sleep(2)