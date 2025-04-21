# procesador.py
import csv

class Analizador:
    def __init__(self, archivo_csv):
        """Inicializa el analizador con datos del archivo CSV"""
        self.datos = []
        try:
            # Intenta con UTF-8 primero, luego con Latin-1 como fallback
            try:
                with open(archivo_csv, mode='r', encoding='utf-8') as file:
                    self.datos = list(csv.DictReader(file))
            except UnicodeDecodeError:
                with open(archivo_csv, mode='r', encoding='latin-1') as file:
                    self.datos = list(csv.DictReader(file))
        except Exception as e:
            raise ValueError(f"Error al leer el archivo CSV: {str(e)}")

    def ventas_por_provincia(self):
        """Retorna un diccionario con ventas totales por provincia"""
        resultado = {}
        for registro in self.datos:
            provincia = registro['PROVINCIA']
            venta = float(registro['TOTAL_VENTAS'])
            
            if provincia in resultado:
                resultado[provincia] += venta
            else:
                resultado[provincia] = venta
        return resultado

    def ventas_de_provincia(self, nombre_provincia):
        """Retorna las ventas totales para una provincia específica"""
        total = 0.0
        for registro in self.datos:
            if registro['PROVINCIA'] == nombre_provincia:
                total += float(registro['TOTAL_VENTAS'])
        return total
