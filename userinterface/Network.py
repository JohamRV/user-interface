import os 
import time
import networkx as nx
import matplotlib.pyplot as plt
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
                    Network.list_topology()
                case "2":
                    # al momento de seleccionar una de las topologías
                    # por defecto, el administrador crea las topologías y
                    # las implementa con una red por defecto
                    # topología lineal - una sola red para todos los nodos
                    # topología de arbol - una red por cada nivel
                    # topología anillo - una red por cada enlace
                    # topología mesh - una sola red para todos los nodos
                    Network.create_topology()
                case "3":
                    # esta sección permite editar esta topología implementada
                    # por defecto, agregar nuevas redes subneting, agregar nodos, editar info
                    Network.edit_topology()
                case "4":
                    Network.search_topology()
                case "5":
                    Network.delete_topology()
                case "6":
                    print("\n[.] Regresando al home.")
                    SubMenu.return_admin_menu()
                    
                case ___:
                    print("\n[.] Opción inválida. Intente de nuevo.")
                    time.sleep(2)

    @staticmethod
    def list_topology():
        pass

    @staticmethod
    def edit_topology():
        pass

    @staticmethod
    def search_topology():
        pass

    @staticmethod
    def delete_topology():
        pass

    @staticmethod
    def create_topology():

        while True:
            print("\n+-----------------------------------------------------+\n"+
                    "|                Tipos de topologías                  |\n"+
                    "+-----------------------------------------------------+\n"+
                    "| 1>  Lineal                                          |\n"+
                    "| 2>  Malla                                           |\n"+
                    "| 3>  Árbol                                           |\n"+
                    "| 4>  Anillo                                          |\n"+
                    "| 5>  Regresar                                        |\n"+
                    "+-----------------------------------------------------+\n")
            option_topology = input("[.] Ingrese un tipo de topología: ")
            
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
                    print("\n[.] Regresando al módulo de networking.")
                    Network.menu()
                case ___:
                    print("\n[.] Opción inválida. Intente de nuevo.")
                    time.sleep(2)

        # Configuración de las máquinas virtuales

    @staticmethod
    def create_lineal_topology():

        n_nodes=int(input("[.] Ingrese la cantidad de nodos:"))
        print("+-----------------------------------------------------+")
        
        nodes = Network.create_linear_topology_grapho(1, n_nodes)
        
        network_id = Network.create_lineal_network(nodes)

        while True:
            option=input("¿Quiere crear todos los nodos iguales? (S/N)")

            if option=="S":
                    SubMenu.show_flavors()
                    flavor_id=int(input(f"[.] Ingrese el id del flavor para su vm de {i+1}° nivel: "))
                    SubMenu.show_images()
                    image_id=int(input(f"[.] Ingrese el id de la imagen para su vm de {i+1}° nivel: "))
                    SubMenu.show_security_groups()
                    security_group_id=int(input(f"[.] Ingrese el id del grupo de seguridad para su vm de {i+1}° nivel: "))
                    SubMenu.create_vm_by_level(network_id, flavor_id, image_id, security_group_id)
                    print("+-----------------------------------------------------+")

            elif option=="N":
                for i in range(0, n_nodes):
                    SubMenu.show_flavors()
                    flavor_id=int(input(f"[.] Ingrese el id del flavor para su vm de {i+1}° nivel: "))
                    SubMenu.show_images()
                    image_id=int(input(f"[.] Ingrese el id de la imagen para su vm de {i+1}° nivel: "))
                    SubMenu.show_security_groups()
                    security_group_id=int(input(f"[.] Ingrese el id del grupo de seguridad para su vm de {i+1}° nivel: "))
                    SubMenu.create_vm_by_level(network_id, flavor_id, image_id, security_group_id)
                    print("+-----------------------------------------------------+")
            else:
                print("[.] Opción inválida")

    @staticmethod
    def create_mesh_topology():
        
        n_rows=int(input("[.] Ingrese la cantidad de filas:"))
        n_columns=int(input("[.] Ingrese la cantidad de filas:"))
        print("+-----------------------------------------------------+")
        
        nodes=Network.create_mesh_topology_grapho(0, n_rows, n_columns)        



    @staticmethod
    def create_tree_topology():
        node=0
        level=int(input("[.] Ingrese el nivel  de la topología"))
        print("+-----------------------------------------------------+")
        
        nodes=Network.create_tree_topology_grapho(1, level)
        # nivel cantidad de redes a crear
        for i in range(0, level):
            network_id = Network.create_network_by_level(nodes, i+1)
            SubMenu.show_flavors()
            flavor_id=int(input(f"[.] Ingrese el id del flavor para su vm de {i+1}° nivel: "))
            SubMenu.show_images()
            image_id=int(input(f"[.] Ingrese el id de la imagen para su vm de {i+1}° nivel: "))
            SubMenu.show_security_groups()
            security_group_id=int(input(f"[.] Ingrese el id del grupo de seguridad para su vm de {i+1}° nivel: "))
            SubMenu.create_vm_by_level(network_id, flavor_id, image_id, security_group_id, node)
            print("+-----------------------------------------------------+")
        
        # se debe hacer el subneteo

    @staticmethod
    def create_ring_topology():
        n_nodes=int(input("[.] Ingrese la cantidad de nodos:"))
        nodes=Network.create_ring_topology_grapho(1, n_nodes)

    @staticmethod
    def create_lineal_network(nodes: dict):
        name = input(f"[.] Ingrese el nombre de la red: ")
        description = input(f"[.] Ingrese una descripción de la red: ")
        ip_addr_main = input(f"[.] Ingrese la IP de la red (0.0..0.0/24): ")
        status = True
        # enviar el request para crear la red princiapl lineal
        # a nuestro ms-networking
        # validar?
        # que el response de crear una network devuelva el id de la red creada

    @staticmethod 
    def create_network_by_level(topology:list, level:int):
        name = input(f"[.] Ingrese el nombre de la red de {level}° nivel: ")
        description = input(f"[.] Ingrese una descripción de la red de {level}° nivel: ")
        ip_addr_main = input(f"[.] Ingrese la IP de la red de {level}° nivel (1.1.1.1/24): ")
        status = True
        # enviar el request para crear la red princiapl
        # a nuestro ms-networking
        # validar?
        # que el response de crear una network devuelva el id de la red creada
    
    @staticmethod 
    def create_ring_topology_grapho(first_node:int, n_nodes):
        start = first_node
        nodes = [f"node-{i+start}" for i in range(n_nodes)]
        sub_grafo = {}

        for k in range(n_nodes):
            if k == 0:
                links = [nodes[1], nodes[n_nodes-1]]
            elif k == n_nodes-1:
                links = [nodes[k-1], nodes[0]]
            else:
                links = [nodes[k-1], nodes[k+1]]

            sub_grafo[nodes[k]] = {"links": links}

        return sub_grafo

    @staticmethod
    def create_linear_topology_grapho(first_node:int, n_nodes:int):
        nodes=[]
        for i in range(first_node-1, n_nodes):
            if i == n_nodes - 1:
                nodes.append(
                    {
                        f"node-{i+1}": {
                            "links": [ f"node-{i}" ]
                        }
                    }
                )
            elif i == 0:
                nodes.append(
                    {
                        f"node-{i+1}": {
                            "links": [ f"node-{i+2}" ]
                        }
                    }
                )
            else:
                nodes.append(
                    {
                        f"node-{i+1}": {
                            "links": [ f"node-{i}", f"node-{i+2}" ]
                        }
                    }
                )
        return nodes
    
    @staticmethod
    def create_tree_topology_grapho(first_node, level):
        start = first_node
        sub_grafo = {}
        node = 0
        for i in range(1, level+1):
            nodes_cant = 2**(i-1)
            for j in range(nodes_cant):
                node_name = f"node-{node+start}"
                if i == level:
                    enlaces = []
                else:
                    enlaces = [f"node-{node*2+1+start}", f"node-{node*2+2+start}"]
                if node != 0:
                    if node%2==0:
                        enlaces.append(f"node-{int((node-2)/2)+start}")
                    else:
                        enlaces.append(f"node-{int((node-1)/2)+start}")
                sub_grafo[node_name] = {"links": enlaces}
                node += 1
        return sub_grafo
    

    @staticmethod
    def create_mesh_topology_grapho(next_node: int, n_rows: int, n_columns: int):
        start = next_node
        nodes = []

        # los enlaces se hallan recorriendo cada fila
        # asumiendo que n_rows (0 - n_rows-1)
        # asumiendo que n_columns (0 - n_columns-1)
        for i in range(n_rows):
            temp = []
            for j in range(n_columns):
                nodo = "node-" + str(i + start) + "x" + str(j + start)
                temp.append(nodo)
            nodes.append(temp)

        sub_grafo = {}
        
        # ahora se vuelve a iterar por cada fila y columna asignando los enlaces al diccionario de grafos
        for k in range(n_rows):
            for j in range(n_columns):
                links = []
                if k > 0:
                    links.append(nodes[k - 1][j])
                if k < n_rows - 1:
                    links.append(nodes[k + 1][j])
                if j > 0:
                    links.append(nodes[k][j - 1])
                if j < n_columns - 1:
                    links.append(nodes[k][j + 1])

                sub_grafo[nodes[k][j]] = {"links": links}

        return sub_grafo

    @staticmethod               
    def draw_topology(topology):
        G = nx.Graph()
        # Add nodes to the graph
        for node in topology:
            G.add_node(node)

        # Add edges to the graph
        for node, connections in topology.items():
            for neighbor in connections['links']:
                G.add_edge(node, neighbor)

        # Plot the graph
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', font_weight='bold')
        plt.show()
