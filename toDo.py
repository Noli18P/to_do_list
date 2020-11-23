def bienvenida():
    mensaje = """
    Bienvenido a tu lista de tareas, en ella
    puedes crear, eliminar y ver las tareas 
    que tienes por hacer.

        1 - Crear tarea
        2 - Eliminar tarea
        3 - Ver tareas
        4 - Salir 
    """

    print(mensaje)

def main():
    contador = 0
    por_hacer = []
    confirmacion = ''

    if contador == 0:
        bienvenida()
        contador = 1

    while confirmacion != 's':
        seleccion = input('Ingresa la opción a realizar: \n')

        if seleccion == '1':
            tarea = input('Ingresa la tarea: ').upper()
            por_hacer.append(tarea)
        elif seleccion == '2':
            for tarea in por_hacer:
                eliminar = int(input('¿Que tarea deseas eliminar? (ingresa el nombre)')).upper()
                print(tarea)
            por_hacer.remove(eliminar)
        elif seleccion == '3':
            print('\nEstas son tus tareas por hacer: \n')
            for tarea in por_hacer:
                print(tarea)
        elif seleccion == '4':
            if len(por_hacer) != 0:
                confirmacion = input('¿Estas seguro de que deseas salir? (s/n)').lower()
                if confirmacion == 's':
                    print('Ten un buen dia!')
            else:
                print('Ten un buen dia!') 
        else: 
            print('La opcion que ingresaste no exisre')
            
if __name__ == '__main__':
    main()