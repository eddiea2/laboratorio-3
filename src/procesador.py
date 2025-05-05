import csv

class Analizador:
    def __init__(self, archivo_csv):
        """Inicializa el analizador con datos del archivo CSV, excluyendo la provincia 'ND'."""
        self.datos = []
        try:
            try:
                with open(archivo_csv, mode='r', encoding='utf-8') as file:
                    self.datos = self._filtrar_provincias(csv.DictReader(file))
            except UnicodeDecodeError:
                with open(archivo_csv, mode='r', encoding='latin-1') as file:
                    self.datos = self._filtrar_provincias(csv.DictReader(file))
        except Exception as e:
            raise ValueError(f"Error al leer el archivo CSV: {str(e)}")

    def _filtrar_provincias(self, lector):
        """Filtra registros excluyendo la provincia 'ND'."""
        return [fila for fila in lector if fila.get('PROVINCIA', '').strip().upper() != 'ND']

    def ventas_por_provincia(self):
        """Retorna un diccionario con ventas totales por provincia."""
        resultado = {}
        for registro in self.datos:
            try:
                provincia = registro['PROVINCIA']
                venta = float(registro['TOTAL_VENTAS'].replace(',', '.'))

                if provincia in resultado:
                    resultado[provincia] += venta
                else:
                    resultado[provincia] = venta
            except (KeyError, ValueError) as e:
                print(f"Error procesando registro: {registro} -> {e}")
        return resultado

    def ventas_de_provincia(self, nombre_provincia):
        """Retorna las ventas totales para una provincia específica."""
        total = 0.0
        for registro in self.datos:
            try:
                if registro['PROVINCIA'].lower() == nombre_provincia.lower():
                    total += float(registro['TOTAL_VENTAS'].replace(',', '.'))
            except (KeyError, ValueError) as e:
                print(f"Error procesando registro: {registro} -> {e}")
        return total

    def exportaciones_por_mes(self):
        """Retorna un diccionario con el total de exportaciones agrupadas por mes."""
        resultado = {}
        for registro in self.datos:
            try:
                mes = registro['MES']
                exportacion = float(registro['EXPORTACIONES'].replace(',', '.'))
                if mes in resultado:
                    resultado[mes] += exportacion
                else:
                    resultado[mes] = exportacion
            except (KeyError, ValueError) as e:
                print(f"Error procesando exportación: {registro} -> {e}")
        return resultado

    def provincia_con_mayor_importacion(self):
        """Retorna el nombre de la provincia con mayor total de importaciones."""
        importaciones = {}
        for registro in self.datos:
            try:
                provincia = registro['PROVINCIA']
                valor = float(registro['IMPORTACIONES'].replace(',', '.'))
                if provincia in importaciones:
                    importaciones[provincia] += valor
                else:
                    importaciones[provincia] = valor
            except (KeyError, ValueError) as e:
                print(f"Error procesando importación: {registro} -> {e}")
        if not importaciones:
            raise ValueError("No hay datos de importaciones disponibles.")
        return max(importaciones.items(), key=lambda x: x[1])[0]
