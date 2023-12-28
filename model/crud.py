import mysql.connector
from mysql.connector import errorcode
from model.schemas import *

class DAO:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(
                user='root', 
                password='api12345',
                host='bdproyecto.cyxgg58rtmri.us-east-1.rds.amazonaws.com',
                database='dbm')
            print("Conecion Establecida")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de Usuario o Contraseña")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Base de Datos no Existe")
            else:
                print(err)

    def getStops(self):
        self.cnx.reconnect()
        cursor = self.cnx.cursor()
        try:
            query = ('SELECT * FROM paradero')
            cursor.execute(query)
            lista_paraderos = []
            for x in cursor:
                paradero = Paraderos(x[0], x[1], x[2], x[3], x[4], x[5])
                lista_paraderos.append(paradero)
            cursor.close()
            self.cnx.close()
            return lista_paraderos
        except Exception as e:
            print(f"Error: {e}")

    def calculateCoste(self, coste:Coste):
        ciudades = {"Curico": 1,"Molina": 2,"Lontue": 3}
        idOrigen = ciudades[coste.origen]
        idDestino = ciudades[coste.destino]
        self.cnx.reconnect()
        cursor = self.cnx.cursor()
        try:
            query = ('CALL obtenerPrecio(%s, %s, %s)')
            cursor.execute(query, (idOrigen, idDestino,coste.cantidad))
            total =  cursor.fetchone()
            coste = CosteTotal(total[0], total[1],total[2],total[3] )
            cursor.close()
            self.cnx.close()
            return coste  
        except Exception as e:
            print(f"Ocurrió un error: {e}")

            
    def insertStop(self, stop:Stop):
        self.cnx.reconnect()
        cursor = self.cnx.cursor()
        try:
            query = ('INSERT INTO paradero (idparadero, nombreparadero, direccion, idzona, latitud, longitud) values (%s, %s, %s, %s, %s, %s)')
            cursor.execute(query, (stop.idparadero, stop.nombreparadero, stop.direccion, stop.idzona, stop.latitud, stop.longitud))
            self.cnx.commit()
            cursor.close()
            self.cnx.close()
            return "Insertado con exito"
        except Exception as e:
            return(f"Ocurrió un error: {e}")



  

    
        