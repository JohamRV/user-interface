import os
import time
class Cluster:

    @staticmethod
    def menu():
        while True:
            os.system("cls")
            print("\n+-----------------------------------------------------+\n"+
                    "|              Cluster de servidores                  |\n"+
                    "+-----------------------------------------------------+\n"+
                    "| 1> Genérico                                         |\n"+
                    "| 2> OpenStack                                        |\n"+
                    "| 3> Regresar                                         |\n"+
                    "+-----------------------------------------------------+\n")
            option=input("[.] Seleccione un cluster: ")

            match option:
                case "1":
                    return "GENERIC"
                case "2":
                    return "OPENSTACK"
                case "3":
                    print("\n[.] Regresando al home.")
                    break
                case __:
                    print("\n[.] Opción inválida. Intente de nuevo.")
                    time.sleep(3)
