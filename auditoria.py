from datos import lote_inspecciones
total_alertas = 0



for inspeccion in lote_inspecciones:

    if inspeccion['estado'] == "Rechazado":

        total_alertas += 1

        print(f"¡ALERTA! El puesto con reporte {inspeccion['id_reporte']} falló la inspección.")



print(f"Auditoría finalizada. Total de alertas generadas: {total_alertas}") 

