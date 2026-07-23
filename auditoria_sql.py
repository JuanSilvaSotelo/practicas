import sqlite3

conexion = sqlite3.connect('auditoria.db')
cursor = conexion.cursor()

cursor.execute('SELECT * FROM puestos_control WHERE estado = "Rechazado"')

resultados = cursor.fetchall()

for fila in resultados:
    print(fila)

conexion.close()