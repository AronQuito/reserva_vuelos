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
