import threading

class VuelosData:
    def __init__(self):
        self.vuelos = {
            "vuelo_123": {
                "asientos": {
                    "A1": None, "A2": None, "A3": None,
                    "B1": None, "B2": None, "B3": None
                }
            }
        }
        self.lectura = threading.Semaphore()
        self.escritor = threading.Semaphore()

    def leer_vuelos(self):
        self.lectura.acquire()
        vuelos_copia = self.vuelos.copy()
        self.lectura.release()
        return vuelos_copia

    def reservar(self, vuelo, asiento, nombre):
        self.lectura.acquire()
        self.escritor.acquire()
        exito = False
        if self.vuelos[vuelo]["asientos"][asiento] is None:
            self.vuelos[vuelo]["asientos"][asiento] = nombre
            exito = True
        self.escritor.release()
        self.lectura.release()
        return exito

    def cancelar(self, vuelo, asiento):
        self.lectura.acquire()
        self.escritor.acquire()
        exito = False
        if self.vuelos[vuelo]["asientos"][asiento] is not None:
            self.vuelos[vuelo]["asientos"][asiento] = None
            exito = True
        self.escritor.release()
        self.lectura.release()
        return exito

    def reiniciar_asientos(self):
        self.lectura.acquire()
        self.escritor.acquire()
        for vuelo in self.vuelos:
            for asiento in self.vuelos[vuelo]["asientos"]:
                self.vuelos[vuelo]["asientos"][asiento] = None
        self.escritor.release()
        self.lectura.release()
