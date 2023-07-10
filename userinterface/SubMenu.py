
class SubMenu():
    
    @staticmethod
    def return_admin_menu():
        from userinterface.Administrator import Administrator
        Administrator.menu()

    @staticmethod
    def go_slice_menu():
        from userinterface.Slice import Slice
        Slice.menu()

    @staticmethod
    def show_slices():
        from userinterface.Slice import Slice
        Slice.list_slices()


    @staticmethod
    def go_user_menu():
        from userinterface.User import User
        User.menu()


    @staticmethod
    def show_users():
        from userinterface.User import User
        User.list_users()


    @staticmethod
    def show_flavors():
        from userinterface.Flavor import Flavor
        Flavor.list_flavors()


    @staticmethod
    def show_images():
        from userinterface.Image import Image
        Image.list_images()


    @staticmethod
    def show_security_groups():
        from userinterface.Security import Security
        Security.list_security_groups()

    @staticmethod
    def go_topology_menu():
        from userinterface.Network import Network
        Network.create_topology()

    @staticmethod
    def go_compute_menu():
        from userinterface.Compute import Compute
        Compute.menu()

    @staticmethod
    def create_vm_by_level():
        from userinterface.Compute import Compute
        Compute.create_vm()

    @staticmethod
    def go_image_menu():
        from userinterface.Image import Image
        Image.menu()

    @staticmethod
    def go_security_menu():
        from userinterface.Security import Security
        Security.menu()

    @staticmethod
    def go_monitor_menu():
        from userinterface.Monitor import Monitor
        Monitor.menu()

    @staticmethod
    def go_to_cluster():
        from userinterface.Cluster import Cluster
        Cluster.menu()