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
                    "| 2>  Crear Imágenes                                  |\n"+
                    "| 3>  Editar Imágenes                                 |\n"+
                    "| 4>  Buscar Imágenes                                 |\n"+
                    "| 5>  Borrar Imágenes                                 |\n"+
                    "| 6>  Regresar                                        |\n"+
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
                    print("\n[.] Regresando al home.")
                    SubMenu.return_admin_menu()
                    
                case ___:
                    print("\n[.] Opción inválida. Intente de nuevo.")
                    time.sleep(2)