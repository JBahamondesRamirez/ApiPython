from pydantic import BaseModel

class Paraderos:
    def __init__(self,idparadero:int, nombreparadero:str, direccion:str, idzona:int, latitud:int, longitud:int):
        self.idparadero = idparadero
        self.nombreparadero = nombreparadero
        self.direccion = direccion
        self.idzona = idzona
        self.latitud = latitud
        self.longitud = longitud

class CosteTotal:
    def __init__(self, idTarifa,zonaOrigenId:int, zonaDestinoId:int, precioViaje:int):
        self.idTarifa = idTarifa
        self.zonaOrigenId = zonaOrigenId
        self.zonaDestinoId = zonaDestinoId
        self.precioViaje = precioViaje

class Coste(BaseModel):
    origen:str
    destino:str
    cantidad:str


class Stop(BaseModel):
    idparadero:int
    nombreparadero:str
    direccion:str
    idzona:int
    latitud:float
    longitud:float