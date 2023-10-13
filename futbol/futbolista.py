class Futbolista(Persona, Deportista):
    _listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbolista", añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista._listaFutbolistas.append(self)
    
    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados
    def getGolesMarcados(self):
        return self._golesMarcados
    
    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil
    def getPiernaHabil(self):
        return self._piernaHabil
    
    @classmethod
    def setListaFutbolistas(cls, listaFutbolistas):
        cls._listaFutbolistas = listaFutbolistas
    
    @classmethod
    def getListaFutbolistas(cls):
        return cls._listaFutbolistas
    
    def __str__(self):
        mensaje = f"Mi nombre es {self.getNombre} soy profesional en el deporte {self.getDeporte}. Tengo {self.getEdad} años de edad y llevo {self.getAñosPracticando} años en el deporte"