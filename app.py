from src.procesador import Analizador
import os

def main():
    try:
        ruta_csv = os.path.join('data', 'sri_ventas_2024.csv')
        analizador = Analizador(ruta_csv)

        print("\n Ventas totales por provincia:")
        ventas = analizador.ventas_por_provincia()
        for provincia, total in ventas.items():
            print(f"\t{provincia}: ${total:.2f}")

        print("\n Porcentaje promedio de ventas con tarifa 0% por provincia:")
        porcentajes = analizador.porcentaje_tarifa_0_por_provincia()
        for provincia, porcentaje in porcentajes.items():
            print(f"\t{provincia}: {porcentaje:.2f}%")

        print("\n Provincia con mayor volumen de importaciones:")
        mayor = analizador.provincia_con_mayor_importacion()
        print(f"\t{mayor}")

        print("\n Diferencia entre ventas totales y exportaciones por provincia:")
        diferencias = analizador.diferencia_ventas_exportaciones_por_provincia()
        for provincia, valor in diferencias.items():
            print(f"\t{provincia}: ${valor:.2f}")

    except Exception as e:
        print(f" Error al ejecutar el análisis: {str(e)}")

if __name__ == "__main__":
    main()
