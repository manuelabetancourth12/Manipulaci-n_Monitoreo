import psutil
import time
from datetime import datetime

def monitor_recursos():
    print("Iniciando monitoreo de recursos. Presiona Ctrl+C para detener.")
    try:
        while True:
            # Intervalo de 1 segundo para medir correctamente el uso de CPU
            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory().percent
            
            print(f"CPU: {cpu}% | RAM: {ram}%")
            
            # Umbral de alerta
            if ram > 80.0:
                with open("log_alertas.txt", "a") as f:
                    f.write(f"[{datetime.now()}] ALERTA: Consumo de RAM crítico ({ram}%)\n")
                print("¡ALERTA! RAM supera el 80%. Registrado en log.")
                
            time.sleep(1) # Pausa para no saturar la CPU con el propio monitoreo
            
    except KeyboardInterrupt:
        print("\nMonitoreo detenido por el usuario.")

if __name__ == "__main__":
    monitor_recursos()