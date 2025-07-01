from threading import Lock, Semaphore

class VuelosData:
    def __init__(self):
        self.vuelos = {
            "vuelo_123": {
                "asientos": {
                    "1A": None,
                    "1B": None,
                    "1C": None
                }
            }
        }
        self.lectores = 0
        self.mutex = Lock()
        self.escritor = Semaphore(1)
        self.lectura = Semaphore(1)

    def leer_vuelos(self):
        with self.mutex:
            self.lectores += 1
            if self.lectores == 1:
                self.escritor.acquire()

        datos = self.vuelos.copy()

        with self.mutex:
            self.lectores -= 1
            if self.lectores == 0:
                self.escritor.release()
        return datos

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
