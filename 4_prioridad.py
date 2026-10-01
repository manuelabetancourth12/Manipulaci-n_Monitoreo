import os
import psutil
import time
import multiprocessing

def calculo_pesado(nombre, prioridad):
    # Obtenemos el proceso actual
    proceso_actual = psutil.Process(os.getpid())
    
    # Adaptación multiplataforma para cambiar la prioridad en el SO
    try:
        if os.name == 'nt': # Windows
            if prioridad == "ALTA":
                proceso_actual.nice(psutil.HIGH_PRIORITY_CLASS)
            else:
                proceso_actual.nice(psutil.IDLE_PRIORITY_CLASS)
        else: # Linux / macOS
            if prioridad == "ALTA":
                os.nice(-10) # En Unix, valores negativos = mayor prioridad (requiere sudo)
            else:
                os.nice(10)  # Valores positivos = menor prioridad ("más amable")
    except PermissionError:
        print(f"[{nombre}] Permiso denegado para subir prioridad (necesitas sudo/admin).")
            
    print(f"Iniciando {nombre} con prioridad {prioridad} (PID: {os.getpid()})")
    
    inicio = time.time()
    
    # Bucle intensivo para monopolizar ciclos de CPU
    resultado = 0
    for i in range(30_000_000):
        resultado += i * 2
    
    fin = time.time()
    print(f"--> {nombre} ({prioridad}) finalizado en {fin - inicio:.3f} segundos.")

if __name__ == '__main__':
    print("Lanzando procesos simultáneos. Compitiendo por la CPU...")
    
    # Instanciamos dos subprocesos pesados
    p_baja = multiprocessing.Process(target=calculo_pesado, args=("Proceso_1", "BAJA"))
    p_alta = multiprocessing.Process(target=calculo_pesado, args=("Proceso_2", "ALTA"))
    
    # Iniciamos al mismo tiempo
    p_baja.start()
    p_alta.start()
    
    # Esperamos a que terminen
    p_baja.join()
    p_alta.join()