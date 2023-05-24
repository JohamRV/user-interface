#!/usr/bin/env python
import time
import pprint

TIEMPO_MEDIDA=8
FAC_CONVERSION=1/100

# Leer archivo de uso de CPU
def uso_cpu():
    dicc_cpu_valor = {}
    with open('/proc/stat') as file1:
        contador=0
        lineas = file1.readlines()
        for linea in lineas:
            if linea.find('cpu') != -1:
                if contador == 0:
                    valor_cpu = 'total'
                else:
                    valor_cpu = 'cpu'+str(contador)

                lista_palabras=linea.split()
                # Se toma el tiempo IDLE
                valor_uso = lista_palabras[4]
                contador +=1
                dicc_cpu_valor[valor_cpu]=float(valor_uso)
    return dicc_cpu_valor

# Calcular uso de cpu en un intervalo de tiempo
def calculo_uso_cpu(dicc1,dicc2,tiempo,conversion):
    dicc_uso_cpu = {}
    lista_cpu = list(dicc1.keys())
    valores_uso1 = list(dicc1.values())
    valores_uso2 = list(dicc2.values())
    for i in range(len(lista_cpu)):
        resta_uso = (valores_uso2[i]-valores_uso1[i])*(conversion)
        if i==0:
            porcentaje_uso=(((tiempo*(len(lista_cpu)-1))-resta_uso)/(tiempo*(len(lista_cpu)-1)))*100
            # Caso de porcentaje negativo, cuando hay poca carga en el worker
            if porcentaje_uso<0:
                porcentaje_uso=0.0
        else:
            porcentaje_uso = ((tiempo-resta_uso)/tiempo)*100
            # Caso de porcentaje negativo, cuando hay poca carga en el worker
            if porcentaje_uso<0:
                porcentaje_uso=0.0
        dicc_uso_cpu[lista_cpu[i]]=round(porcentaje_uso,8)
    return dicc_uso_cpu

# Obtener la lista de interfaces del sistema
def get_interfaces():
    with open('/proc/net/dev') as f:
        data = f.readlines()
        interfaces = []
        for line in data[2:]:
            interface = line.split(':')[0].strip()
            interfaces.append(interface)
    return interfaces

# Leer archivo de uso de ancho de banda
def uso_bandwidth(lista_interfaces):
    dicc_bandwidth_bytes_rx={}
    dicc_bandwidth_rx={}
    dicc_bandwidth_bytes_tx={}
    dicc_bandwidth_tx={}
    dicc_error_bit={}
    with open('/proc/net/dev') as file3:
        lineas = file3.readlines()
        contador = 0
        for linea in lineas:
            if lista_interfaces[contador] in linea:
                data = linea.split(':')[1].split()
                rx_bytes,rx_packets1,tx_bytes,tx_packets1,err_rx,err_tx = int(data[0]), int(data[1]), int(data[8]), int(data[9]), int(data[2]),int(data[10])
                dicc_bandwidth_bytes_rx[lista_interfaces[contador]]=rx_bytes
                dicc_bandwidth_rx[lista_interfaces[contador]]=rx_packets1
                dicc_bandwidth_bytes_tx[lista_interfaces[contador]]=tx_bytes
                dicc_bandwidth_tx[lista_interfaces[contador]]=tx_packets1
                dicc_error_bit[lista_interfaces[contador]]=(err_rx+err_tx)
                contador += 1
                if contador>len(lista_interfaces):
                    break
    return dicc_bandwidth_bytes_rx,dicc_bandwidth_rx,dicc_bandwidth_bytes_tx,dicc_bandwidth_tx,dicc_error_bit

# Calcular el uso de ancho de banda
def calculo_uso_bandwidth(dicc1_rx_bytes,dicc2_rx_bytes,dicc1_rx,dicc2_rx,dicc1_tx_bytes,dicc2_tx_bytes,dicc1_tx,dicc2_tx,dicc_err1,dicc_err2,tiempo):
    dicc_bandwidth={}
    lista_interfaces = list(dicc1_rx_bytes.keys())

    valores_uso1_b = list(dicc1_rx_bytes.values())
    valores_uso2_b = list(dicc2_rx_bytes.values())
    valores_uso1_rx = list(dicc1_rx.values())
    valores_uso2_rx = list(dicc2_rx.values())
    val_uso1_b_tx = list(dicc1_tx_bytes.values())
    val_uso2_b_tx = list(dicc2_tx_bytes.values())
    valores_uso1_tx = list(dicc1_tx.values())
    valores_uso2_tx = list(dicc2_tx.values())
    val_err1 = list(dicc_err1.values())
    val_err2 = list(dicc_err2.values())

    for i in range(len(lista_interfaces)):
        #Conversion de bytes a bits por segundo
        resta_uso_bits = ((valores_uso2_b[i]-valores_uso1_b[i])*8)/tiempo
        resta_uso_rx = (valores_uso2_rx[i]-valores_uso1_rx[i])/tiempo
        resta_uso_bits_tx = ((val_uso2_b_tx[i]-val_uso1_b_tx[i])*8)/tiempo
        resta_uso_tx = (valores_uso2_tx[i]-valores_uso1_tx[i])/tiempo
        resta_uso_error = (val_err2[i]-val_err1[i])/tiempo

        dicc_interface={}

        dicc_bits={}
        dicc_bits['rx']=round(resta_uso_bits,5)
        dicc_bits['tx']=round(resta_uso_bits_tx,5)

        dicc_packages={}
        dicc_packages['rx']=round(resta_uso_rx,5)
        dicc_packages['tx']=round(resta_uso_tx,5)

        dicc_interface['bits/s']=dicc_bits
        dicc_interface['pcks/s']=dicc_packages
        dicc_interface['err_bits/s']=resta_uso_error
        
        dicc_bandwidth[lista_interfaces[i]]=dicc_interface

    return dicc_bandwidth

# Leer archivo de uso de memoria
def uso_memoria():
    dicc_memoria={}
    with open('/proc/meminfo') as file2:
        lineas = file2.readlines()
        for linea in lineas:
            if linea.find('Mem') != -1:
                lista_palabras=linea.split()
                dicc_memoria[lista_palabras[0][:-1]]=lista_palabras[1]
    return dicc_memoria

# Creacion del diccionario con las entradas calculadas                
def creacion_diccionario(porcentajes_cpu,uso_memoria,bandwidth):
    unix_time= int(time.time())

    recursos = {
        'timestamp' : unix_time,
        'cpu': porcentajes_cpu,
        'memory': uso_memoria,
        'bandwidth' : bandwidth
    }

    return recursos

def main():
    print('------MONITOREO DE RECURSOS-----')
    lista_interfaces=get_interfaces()
    diccionario1=uso_cpu()
    dicc_bytes_rx1,dicc_rx1,dicc_bytes_tx1,dicc_tx1,dicc_err1=uso_bandwidth(lista_interfaces)
 
    time.sleep(TIEMPO_MEDIDA)

    diccionario2=uso_cpu()
    dicc_bytes_rx2,dicc_rx2,dicc_bytes_tx2,dicc_tx2,dicc_err2=uso_bandwidth(lista_interfaces)
    dicc_porcentajes_cpu = calculo_uso_cpu(diccionario1,diccionario2,TIEMPO_MEDIDA,FAC_CONVERSION)
    print('**Porcentaje de uso de CPU**')
    print(dicc_porcentajes_cpu.items())
    print('--------------------------------')
    dicc_bw=calculo_uso_bandwidth(dicc_bytes_rx1,dicc_bytes_rx2,dicc_rx1,dicc_rx2,dicc_bytes_tx1,dicc_bytes_tx2,dicc_tx1,dicc_tx2,dicc_err1,dicc_err2,TIEMPO_MEDIDA)
    print('**Ancho de banda**')
    print(dicc_bw)
    print('--------------------------------')
    print('**Datos de memoria**')
    dicc_memoria=uso_memoria()
    print(dicc_memoria.items())
    print('--------------------------------')

    # Construcción del diccionario
    dicc_recursos=creacion_diccionario(dicc_porcentajes_cpu,dicc_memoria,dicc_bw)
    pprint.pprint(dicc_recursos)

if __name__ == "__main__":
    main()