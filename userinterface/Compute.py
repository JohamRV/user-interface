
class Compute:

    @staticmethod
    def menu():
        print("\n+-----------------------------------------------------+\n"+
                "|                     Módulo de VMs                   |\n"+
                "+-----------------------------------------------------+\n"+
                "| 1>  Listar Imágenes                                 |\n"+
                "| 2>  Editar Imágenes                                 |\n"+
                "| 3>  Buscar Imágenes                                 |\n"+
                "| 4>  Borrar Imágenes                                 |\n"+
                "| 5>  Regresar                                        |\n"+
                "+-----------------------------------------------------+\n")

    @staticmethod
    def create_vm():
        print("\n+----------------------------------------------------------------------+\n"+
                "|                        CREAR VM                                      |\n"+
                "+----------------------------------------------------------------------+")
        vm=input("[.] Ingrese el nombre de la vm: ")
        network=input("[.] Ingrese la red de la vm: ")
        description=input("[.] Ingrese una descripción: ")
        n_vm=input("[.] Ingrese cuantas VMs desea crear:")
        print("+----------------------------------------------------------------------+\n")
        
        # Se escoge que tipo de flavor

        # Se escoge que tipo de imagen

        # Se escoge las reglas de seguridad

        # Se escoge el tipo de autenticación

