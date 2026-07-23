import json
import sqlite3

with open('inspecciones.json', 'r') as archivo:
    inspecciones = json.load(archivo)

conexion = sqlite3.connect('auditoria.db')
cursor = conexion.cursor()

for inspeccion in inspecciones:
    cursor.execute('''INSERT INTO puestos_control (id_reporte, estado) VALUES (?, ?)''',
    (inspeccion['id_reporte'], inspeccion['estado']))

conexion.commit()
conexion.close()