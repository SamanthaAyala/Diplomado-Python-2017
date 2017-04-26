import socket

puerto = int(raw_input('Indica el puerto al que deceas apropiarte: '))

print 'Creacion del Servidor'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print 'Servidor creado'

print 'Seva a apropiar del puerto'

s.bind(("", puerto))

print 'Se apropio del puerto %d' % puerto

print 'Indicamos el numero de clientes que vamos a contestar'

s.listen(1)

print 'El servidor esta esperando a que se conecte alguien.'
sc, addr = s.accept()

print 'Imprimimos el socket que se conecto'
print sc
print 'Mostramos la direccion de quien se conecto'
print addr

recibido = sc.recv(1024)
print 'Cliente dice: %s' % recibido

while True:
        msj = socketCliente.recv(1024)
        cadena = msj.split(',')
        print '%s msj: %s' % ( str(addr) , cadena[1])

        if msj == 'adios':
            print 'Conexion Terminada'
            break

        socketCliente.send(msj)

print 'Cerramos el socket cliente'
socketCliente.close()
print 'Cerramos el socket server'
