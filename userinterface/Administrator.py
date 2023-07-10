import os
import sys
import time
from userinterface.SubMenu import SubMenu
#from userinterface.User import User
#from userinterface.Network import Network
#from userinterface.Security import Security
#from userinterface.Monitor import Monitor

class Administrator:
    
    @staticmethod
    def menu():
        while True:
            os.system("cls")
            # This home must request the user permission and in order of that
            # list all the availables modules
            print("\n+-----------------------------------------------------+\n"+
                    "|              Home del Administrador                 |\n"+
                    "+-----------------------------------------------------+\n"+
                    "| 1> Modulo de slices                                 |\n"+
                    "| 2> Modulo de usuarios                               |\n"+
                    "| 3> Módulo de networking                             |\n"+
                    "| 4> Módulo de VMs                                    |\n"+
                    "| 5> Módulo de imágenes                               |\n"+
                    "| 6> Módulo de seguridad                              |\n"+
                    "| 7> Gestión de recursos                              |\n"+
                    "| 8> Cerrar sesión                                    |\n"+
                    "+-----------------------------------------------------+\n")
            option=input("[.] Ingrese una opción: ")

            match option:
                case "1":
                    SubMenu.go_slice_menu()

                case "2":
                    SubMenu.go_user_menu()

                case "3":
                    SubMenu.go_topology_menu()

                case "4":
                    SubMenu.go_compute_menu()

                case "5":
                    SubMenu.go_image_menu()

                case "6":
                    SubMenu.go_security_menu()

                case "7":
                    SubMenu.go_monitor_menu()

                case "8":
                    print("\n[.] Cerrando sesión.")
                    sys.exit()
                    
                case __:
                    print("\n[.] Opción inválida. Intente de nuevo.")
                    time.sleep(3)