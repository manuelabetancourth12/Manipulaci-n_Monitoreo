import time

class SimuladorCache:
    def __init__(self):
        # El diccionario actúa como nuestra RAM / Caché L1
        self.cache = {}

    def obtener_archivo(self, ruta_archivo):
        # 1. Comprobar si el dato ya está "cerca" del procesador
        if ruta_archivo in self.cache:
            print("[CACHÉ] Leyendo desde la memoria RAM...")
            return self.cache[ruta_archivo]
        
        # 2. Si hay un "Cache Miss", ir al disco (simulamos latencia de E/S con sleep)
        print("[DISCO] Cache Miss. Leyendo datos pesados desde el disco duro...")
        time.sleep(2) 
        
        datos = f"<Contenido binario masivo de {ruta_archivo}>"
        
        # 3. Guardar en caché para la próxima vez
        self.cache[ruta_archivo] = datos
        return datos

sim = SimuladorCache()

# Primera lectura: Penalización de disco
inicio = time.time()
sim.obtener_archivo("base_de_datos.csv")
print(f"Tiempo primera lectura (Disco): {time.time() - inicio:.4f} segundos\n")

# Segunda lectura: Ventaja de la RAM
inicio = time.time()
sim.obtener_archivo("base_de_datos.csv")
print(f"Tiempo segunda lectura (Caché): {time.time() - inicio:.4f} segundos")