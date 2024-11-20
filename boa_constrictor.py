from animal_exotico import AnimalExotico

class BoaConstrictor(AnimalExotico):
    def __init__(self, nombre, peso, edad, pais_origen:str, impuestos:float):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self._ratones_comidos = 0
        
    def hacer_sonido(self):
        return "¡Tsss!"

    def comer_raton(self, raton:int):
        self._ratones_comidos += raton
        
    def ratones_comidos(self):
        return self._ratones_comidos
    
    ##nueva versión”
    

    