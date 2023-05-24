import os 
import time
from userinterface.SubMenu import SubMenu

class Network:
    
    @staticmethod
    def menu():
        os.system("cls")
        while True:
            print("\n+-----------------------------------------------------+\n"+
                    "|                Módulo de Networking                 |\n"+
                    "+-----------------------------------------------------+\n"+
                    "| 1>  Listar Topologías                               |\n"+
                    "| 2>  Crear Topologías                                |\n"+
                    "| 3>  Editar Topologías                               |\n"+
                    "| 4>  Buscar Topologías                               |\n"+
                    "| 5>  Borrar Topologías                               |\n"+
                    "| 6>  Regresar                                        |\n"+
                    "+-----------------------------------------------------+\n")
            option=input("[.] Ingrese una opción:")

            match option:
                case "1":
                    pass
                case "2":
                    Network.create_topology()
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
    def create_topology():

        cluster = SubMenu.go_to_cluster()

        while True:
            print("\n+-----------------------------------------------------+\n"+
                    "|                Tipos de topologías                  |\n"+
                    "+-----------------------------------------------------+\n"+
                    "| 1>  Lineal                                          |\n"+
                    "| 2>  Malla                                           |\n"+
                    "| 3>  Árbol                                           |\n"+
                    "| 4>  Anillo                                          |\n"+
                    "| 5>  Bus                                             |\n"+
                    "+-----------------------------------------------------+\n")
            option_topology = input("[.] Ingrese un tipo de topología")
            
            match option_topology:
                case "1":
                    Network.create_lineal_topology()
                    break
                case "2":
                    Network.create_mesh_topology()
                    break
                case "3":
                    Network.create_tree_topology()
                    break
                case "4":
                    Network.create_ring_topology()
                    break
                case "5":
                    Network.create_bus_topology()
                    break
                case "6":
                    print("\n[.] Regresando al módulo de networking.")
                    Network.menu()
                case ___:
                    print("\n[.] Opción inválida. Intente de nuevo.")
                    time.sleep(2)

        # Configuración de las máquinas virtuales

    @staticmethod
    def create_lineal_topology():
        n_nodes=input("[.] Ingrese la cantidad de nodos:")


    @staticmethod
    def create_mesh_topology():
        n_nodes=input("[.] Ingrese la cantidad de nodos:")

    @staticmethod
    def create_tree_topology():
        n_nodes=input("[.] Ingrese la cantidad de nodos por rama:")
        level=input("[.] Ingrese la cantidad de nodos por rama:")

    @staticmethod
    def create_ring_topology():
        n_nodes=input("[.] Ingrese la cantidad de nodos:")
        

    @staticmethod
    def create_bus_topology():
        n_nodes=input("[.] Ingrese la cantidad de nodos:")
        

