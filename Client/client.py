# Importa la libreria "Socket"
from socket import *
# Indica que el servidor esta en la misma maquina y no en otro IP
serverName = "localHost"
# Define el puerto como 12000
serverPort = 12000
# Crear el socket usando IPV4 y UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Loop infinito para siempre enviar datos
while True:
    # Guarda el nombre del archivo a enviar
    nombre=input("Ingresa el nombre del archivo:")
    # Intenta abrir el archivo como binario
    try:
        fil = open(nombre, "rb")
        # Guarda en la variable f los contenidos del archivo
        f=fil.read()
    # Si no puede abrirlo
    except:
        # Muestra que el archivo no se pudo abrir
        print("No se pudo abrir el archivo "+nombre)
        # Vuelve al inicio del ciclo
        continue
    # Envia el nombre del archivo al servidor
    clientSocket.sendto(nombre.encode(), (serverName, serverPort))
    # Intenta enviar el archivo sin importar su tamnio
    try:
        clientSocket.sendto(f,(serverName, serverPort))
    # Si su tamanio es mayor al soportado
    except:
        # Muestra en consola que el archivo es muy grande
        print("El archivo a enviar es muy grande")
        # Envia un flag de error de archivo grande al servidor
        clientSocket.sendto(b'0',(serverName, serverPort))
        # Vuelve al inicio del ciclo
        continue
    # Intenta recibir el mensaje de confirmacion
    try:
        message, serverAddress = clientSocket.recvfrom(2**20)
        # Muestra el mensaje de confirmacion en consola
        print(message.decode())
    # Si no puede recibirlo
    except:
        # Muestra en consola que no se pudo conectar con el servidor
        print("No se pudo conectar con el servidor")
        # Espera accion del usuario
        input()
        # Sale del loop y cierra el programa
        break