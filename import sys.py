def main():
    ventas = []  # Lista para almacenar las ventas

    while True:
        try:
            print('\nMenú Principal:')
            print('1. Registrar ventas')
            print('2. Guardar cambios CSV')
            print('3. Consultar ventas')
            print('4. Salir')
            opcion = int(input('Seleccione una opción (1-4): '))
            
            if opcion == 1:
                registrar_venta(ventas)
            elif opcion == 2:
                print('Guardando cambios CSV...')
                # Aquí podrías agregar el código para guardar en un archivo CSV
            elif opcion == 3:
                if not ventas:
                    print('No hay ventas registradas.')
                else:
                    print('\nVentas registradas:')
                    for venta in ventas:
                        print(f'Producto: {venta["producto"]}, '
                              f'Cantidad: {venta["cantidad"]}, '
                              f'Precio: {venta["precio"]}, '
                              f'Fecha: {venta["fecha"]}, '
                              f'Cliente: {venta["cliente"]}')
            elif opcion == 4:
                print('Saliendo del programa.')
                break
            else:
                print('Opción fuera de rango, intente de nuevo.')
        except ValueError:
            print('Entrada inválida, por favor ingrese un número entre 1 y 4.')
            continue


def registrar_venta(ventas: list):
    while True:
        try:
            producto = input('Ingrese el nombre del producto: ')
            cantidad = int(input('Ingrese la cantidad vendida: '))
            precio = float(input('Ingrese el precio por unidad: '))
            fecha = input('Ingrese la fecha de la venta (DD-MM-AAAA): ')
            cliente = input('Ingrese el nombre del cliente: ')
            
            if cantidad <= 0 or precio <= 0:
                print('Cantidad y precio deben ser mayores que cero. Intente de nuevo.')
                continue

            venta = {
                'producto': producto,
                'cantidad': cantidad,
                'precio': precio,
                'fecha': fecha,
                'cliente': cliente
            }
            ventas.append(venta)
            print('✅ Venta registrada correctamente.')

            continuar = input('¿Desea registrar otra venta? (s/n): ').lower()
            if continuar != 's':
                break
        except ValueError:
            print('Entrada inválida, por favor intente de nuevo.')
            continue


if __name__ == "__main__":
    print("Bienvenido al sistema de gestión de ventas.")
    main()
def main():
    ventas = []  # Lista para almacenar las ventas

    while True:
        try:
            print('\nMenú Principal:')
            print('1. Registrar ventas')
            print('2. Guardar cambios CSV')
            print('3. Consultar ventas')
            print('4. Salir')
            opcion = int(input('Seleccione una opción (1-4): '))
            
            if opcion == 1:
                registrar_venta(ventas)
            elif opcion == 2:
                print('Guardando cambios CSV...')
                # Aquí podrías agregar el código para guardar en un archivo CSV
            elif opcion == 3:
                if not ventas:
                    print('No hay ventas registradas.')
                else:
                    print('\nVentas registradas:')
                    for venta in ventas:
                        print(f'Producto: {venta["producto"]}, '
                              f'Cantidad: {venta["cantidad"]}, '
                              f'Precio: {venta["precio"]}, '
                              f'Fecha: {venta["fecha"]}, '
                              f'Cliente: {venta["cliente"]}')
            elif opcion == 4:
                print('Saliendo del programa.')
                break
            else:
                print('Opción fuera de rango, intente de nuevo.')
        except ValueError:
            print('Entrada inválida, por favor ingrese un número entre 1 y 4.')
            continue


def registrar_venta(ventas: list):
    while True:
        try:
            producto = input('Ingrese el nombre del producto: ')
            cantidad = int(input('Ingrese la cantidad vendida: '))
            precio = float(input('Ingrese el precio por unidad: '))
            fecha = input('Ingrese la fecha de la venta (DD-MM-AAAA): ')
            cliente = input('Ingrese el nombre del cliente: ')
            
            if cantidad <= 0 or precio <= 0:
                print('Cantidad y precio deben ser mayores que cero. Intente de nuevo.')
                continue

            venta = {
                'producto': producto,
                'cantidad': cantidad,
                'precio': precio,
                'fecha': fecha,
                'cliente': cliente
            }
            ventas.append(venta)
            print('✅ Venta registrada correctamente.')

            continuar = input('¿Desea registrar otra venta? (s/n): ').lower()
            if continuar != 's':
                break
        except ValueError:
            print('Entrada inválida, por favor intente de nuevo.')
            continue


if __name__ == "__main__":
    print("Bienvenido al sistema de gestión de ventas.")
    main()
def main():
    ventas = []  # Lista para almacenar las ventas

    while True:
        try:
            print('\nMenú Principal:')
            print('1. Registrar ventas')
            print('2. Guardar cambios CSV')
            print('3. Consultar ventas')
            print('4. Salir')
            opcion = int(input('Seleccione una opción (1-4): '))
            
            if opcion == 1:
                registrar_venta(ventas)
            elif opcion == 2:
                print('Guardando cambios CSV...')
                # Aquí podrías agregar el código para guardar en un archivo CSV
            elif opcion == 3:
                if not ventas:
                    print('No hay ventas registradas.')
                else:
                    print('\nVentas registradas:')
                    for venta in ventas:
                        print(f'Producto: {venta["producto"]}, '
                              f'Cantidad: {venta["cantidad"]}, '
                              f'Precio: {venta["precio"]}, '
                              f'Fecha: {venta["fecha"]}, '
                              f'Cliente: {venta["cliente"]}')
            elif opcion == 4:
                print('Saliendo del programa.')
                break
            else:
                print('Opción fuera de rango, intente de nuevo.')
        except ValueError:
            print('Entrada inválida, por favor ingrese un número entre 1 y 4.')
            continue


def registrar_venta(ventas: list):
    while True:
        try:
            producto = input('Ingrese el nombre del producto: ')
            cantidad = int(input('Ingrese la cantidad vendida: '))
            precio = float(input('Ingrese el precio por unidad: '))
            fecha = input('Ingrese la fecha de la venta (DD-MM-AAAA): ')
            cliente = input('Ingrese el nombre del cliente: ')
            
            if cantidad <= 0 or precio <= 0:
                print('Cantidad y precio deben ser mayores que cero. Intente de nuevo.')
                continue

            venta = {
                'producto': producto,
                'cantidad': cantidad,
                'precio': precio,
                'fecha': fecha,
                'cliente': cliente
            }
            ventas.append(venta)
            print('✅ Venta registrada correctamente.')

            continuar = input('¿Desea registrar otra venta? (s/n): ').lower()
            if continuar != 's':
                break
        except ValueError:
            print('Entrada inválida, por favor intente de nuevo.')
            continue


if __name__ == "__main__":
    print("Bienvenido al sistema de gestión de ventas.")
    main()
def main():
    ventas = []  # Lista para almacenar las ventas

    while True:
        try:
            print('\nMenú Principal:')
            print('1. Registrar ventas')
            print('2. Guardar cambios CSV')
            print('3. Consultar ventas')
            print('4. Salir')
            opcion = int(input('Seleccione una opción (1-4): '))
            
            if opcion == 1:
                registrar_venta(ventas)
            elif opcion == 2:
                print('Guardando cambios CSV...')
                # Aquí podrías agregar el código para guardar en un archivo CSV
            elif opcion == 3:
                if not ventas:
                    print('No hay ventas registradas.')
                else:
                    print('\nVentas registradas:')
                    for venta in ventas:
                        print(f'Producto: {venta["producto"]}, '
                              f'Cantidad: {venta["cantidad"]}, '
                              f'Precio: {venta["precio"]}, '
                              f'Fecha: {venta["fecha"]}, '
                              f'Cliente: {venta["cliente"]}')
            elif opcion == 4:
                print('Saliendo del programa.')
                break
            else:
                print('Opción fuera de rango, intente de nuevo.')
        except ValueError:
            print('Entrada inválida, por favor ingrese un número entre 1 y 4.')
            continue


def registrar_venta(ventas: list):
    while True:
        try:
            producto = input('Ingrese el nombre del producto: ')
            cantidad = int(input('Ingrese la cantidad vendida: '))
            precio = float(input('Ingrese el precio por unidad: '))
            fecha = input('Ingrese la fecha de la venta (DD-MM-AAAA): ')
            cliente = input('Ingrese el nombre del cliente: ')
            
            if cantidad <= 0 or precio <= 0:
                print('Cantidad y precio deben ser mayores que cero. Intente de nuevo.')
                continue

            venta = {
                'producto': producto,
                'cantidad': cantidad,
                'precio': precio,
                'fecha': fecha,
                'cliente': cliente
            }
            ventas.append(venta)
            print('✅ Venta registrada correctamente.')

            continuar = input('¿Desea registrar otra venta? (s/n): ').lower()
            if continuar != 's':
                break
        except ValueError:
            print('Entrada inválida, por favor intente de nuevo.')
            continue


if __name__ == "__main__":
    print("Bienvenido al sistema de gestión de ventas.")
    main()
