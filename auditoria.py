import json

with open('inspecciones.json', 'r') as archivo:
    lote_inspecciones = json.load(archivo)

total_alertas = 0

lista_errores = []

for inspeccion in lote_inspecciones:

    if inspeccion['estado'] == "Rechazado":
        total_alertas += 1
        print(f"¡ALERTA! El puesto con reporte {inspeccion['id_reporte']} falló la inspección.")
        lista_errores.append(inspeccion)


with open ('errores_detectados.json', 'w') as archivo:
    json.dump(lista_errores,archivo)

print(f"Auditoría finalizada. Total de alertas generadas: {total_alertas}")