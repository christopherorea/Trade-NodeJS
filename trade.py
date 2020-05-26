import requests
import json
import datetime
import time
import mysql.connector

#check_hora()
contador = 2 #Este contador lleva la cuenta de las fechas ingresadas por la bd... hace falta analizar en cual se quedo y actualizar.

#Para no hacer tantos request cambiamos esta linea por una lectura XRP= requests.get('https://api.bitso.com/v3/available_books/');
#XRP.text);
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Mac30sep2012"
)
cur = mydb.cursor()
cur.execute("show databases")
print(cur.fetchall())
mydb.close()

'''
#Hacemos la apertura del json que ya descargue de ejemplo para trabajar local.
with open("trade.json") as file:
	#antes de subir cualquier info primero tomamos el tiempo actual
	tiempo = datetime.datetime.now()
	minutos = tiempo.minute
	horas = tiempo.hour
	dia_sem = tiempo.weekday()+1 #0 lunes - 6 Sabado por defecto. Se suma uno para estar en parametros que quiero.
	dia_mes = tiempo.day
	mes = tiempo.month
	ano = tiempo.year
	#cambiamos los datos del archivo un json y lo guardamos
	data = json.load(file)
	monto = data["payload"]['last']



#la funcion obtiene en que momento se encuentra el programa
def check_tiempo():
	#guardamos el tiempo actual
	time= datetime.datetime.now()
	minutes = time.minute
	#si en cuanto a los minutos no estamos dentro del rango establecido hacemos dormir el programa la cantidad de minutos 
	if(minutes != 0):
		time.sleep(minutes * 60)

def guardar_bd(monto,minutos,horas,dia_sem,dia_mes,mes,ano):
	fecha = "insert into Fecha (minuto,hora,dia_sem,dia_mes,mes,ano) values ('{0}','{1}','{2}','{3}','{4}','{5}')".format(minutos,horas,dia_sem,dia_mes,mes,ano)
	trade = "insert into Trade (ID_Moneda,ID_Fecha,monto) values(1,'{0}','{1}')".format(contador,monto)
	cursor.execute(fecha)
	cursor.execute(trade)
	db.commit()
	contador=contador + 1 
'''
