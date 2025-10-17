import csv
import pandas as pd


def main():
    ventas = []  # <-- se inicializa la lista de ventas

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
                    guardar_venta(ventas)
                elif opcion == 3: 
                    for venta in ventas:
                        print(f'Producto: {venta["producto"]}, Cantidad: {venta["cantidad"]}, Precio: {venta["precio"]}, Fecha: {venta["fecha"]}, Cliente: {venta["cliente"]}')
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
            
            continuar = input('¿Desea registrar otra venta? (s/n): ').lower()
            if continuar != 's':
                break
        except ValueError:
            print('Entrada inválida, por favor intente de nuevo.')
            continue
            

def  guardar_venta(ventas: list):
    try:
        if not ventas:
            print('No hay ventas para guardar.')
            return

        with open('ventas.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=ventas[0].keys())
            writer.writeheader()
            writer.writerows(ventas)
            print('Ventas guardadas exitosamente en ventas.csv')
    except Exception as e:
        print(f'Error al guardar la ventas: {e}')



def consultar_venta():
    try:
        df = pd.read_csv('ventas.csv')
        if df.empty:
            print('No hay ventas registradas.')
        else:
            print('\nVentas registradas:')
            df['subtotal'] = df['cantidad'] * df['precio']
            total = df['subtotal'].sum()
            print(f'Total de ventas: {total:.2f}')
            
            
            producto_mas_vendido = df.groupby('producto')['cantidad'].sum().idxmax()
            print(f'Producto más vendido: {producto_mas_vendido}')
            
            tendencia_clientes = df['cliente'].value_counts().idxmax()
            print(f'Cliente con más compras: {tendencia_clientes}')
    except FileNotFoundError:
        print('El archivo ventas.csv no existe. Por favor, registre y guarde ventas primero.')
    except Exception as e:
        print(f'Error al leer las ventas: {e}')

if __name__ == "__main__":
    print("Bienvenido al sistema de gestión de ventas.")
    main()
