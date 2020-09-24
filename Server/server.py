# Importa la libreria "Socket"
from socket import *
# Define el puerto como 12000
serverPort = 12000
# Crear el socket usando IPV4 y UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Asigna el numero de puerto al socket
serverSocket.bind(('', serverPort))
# Indica en la consola que el servidor esta listo
print("Servidor Listo!")
# Loop infinito para siempre reciWallbir datos
while True:
    # Asgina un tamnio de buffer suficiente y guarda el nombre del archivo junto con la direccion de procedencia
    nombreRaw, clientAddress = serverSocket.recvfrom(2**20)
    # Igual que la linea anterior pero guarda la informacion que hay en el archivo
    recvFile, clientAdress=serverSocket.recvfrom(2**20)
    # Si solo llega un 0 indica que el archivo no se envio debido a su tamanio
    if recvFile==b'0':
        print("El archivo "+ nombreRaw.decode() +" era muy grande")
    # En caso de que no sea un 0 continua
    else:
        # Guarda el nombre del archivo como un String
        nombre = nombreRaw.decode()
        # Crea el archivo con el nombre dado y permite escribir bytes en el
        savFile=open(nombre,"wb")
        # Escribe la informacion en bytes dentro del archivo
        savFile.write(recvFile)
        # Cierra el archivo
        savFile.close()
        # Muestra en consola que se recibio el archivo
        print("El archivo "+ nombreRaw.decode() +" fue recibido exitosamente")
        # Manda de vuelta al cliente la confirmacion de recepcion
        serverSocket.sendto(("El archivo "+ nombreRaw.decode() +" fue recibido exitosamente").encode(), clientAddress)