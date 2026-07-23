import sqlite3

conexion = sqlite3.connect('auditoria.db')
cursor = conexion.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS puestos_control (id_reporte TEXT PRIMARY KEY, estado TEXT)''')

conexion.commit()
conexion.close()