import psutil
import time

def estres_memoria():
    basura_en_ram = []
    print("Iniciando estrés de memoria... Abre tu Administrador de Tareas.")
    
    try:
        while True:
            # Añadimos un string masivo (aprox 10MB por iteración)
            basura_en_ram.append("A" * 10_000_000)
            
            # Consultamos el porcentaje de RAM física ocupada
            ram_actual = psutil.virtual_memory().percent
            print(f"RAM Física en uso: {ram_actual}%")
            
            # LÍMITE DE SEGURIDAD: Evita que la máquina se congele por completo
            if ram_actual > 90.0:
                print("Límite de seguridad alcanzado (90%). El SO ya debería estar paginando.")
                print("Deteniendo para evitar el bloqueo total de la máquina.")
                break
                
            time.sleep(0.1) # Pequeña pausa para poder visualizar la gráfica
            
    except MemoryError:
        print("¡El Gestor de Memoria del SO denegó la asignación (OOM - Out of Memory)!")
    except KeyboardInterrupt:
        print("\nPrueba de estrés abortada.")

    # El Garbage Collector de Python liberará la memoria al vaciar la lista
    basura_en_ram.clear()
    print("Memoria liberada.")

if __name__ == "__main__":
    estres_memoria()