from tkinter import * 
from tkinter import messagebox as MessageBox
import os

global serie_r1_atras; global serie_r2_atras; global serie_r3_atras; global serie_r4_atras; global serie_r5_atras;
global serie_r6_atras;  global serie_r7_atras;  global serie_r8_atras; global serie_r9_atras;
global control_atras; global liquida_total; global series_liquidacion_atras_r1; global control_parpadeo_inicial
global lista_final

valor1 = 0; valor2 = 0; valor3 = 0; valor4 = 0; valor5 = 0; valor6 = 0; valor7 = 0; valor8 = 0; valor9 = 0;
totalCar_2 = 0; totalCar_liquidacion = 0; pico_salid_2 = 0; bandera = 0; series_liquidacion_atras_r1 = 0;
serie_r1_atras = 0; control_parpadeo_inicial = 0; historico = 1; lista_final = [""]

def validar_entrada(P):
	if P == "":
		return True
	try:
		valor = int(P)
		if valor < 1801:
			return True
		else:
			return False
	except ValueError:
		return False

def ejecutar():
	guardar_datos()
	ruta_ejecutable = r"C:\CajaMesaControl\Menu\Menu.exe"
	#os.startfile(ruta_ejecutable)
	raiz.destroy()

def datos_historico1():
	liquidacion_historico_1_rango1.config(text=liquidacion_liqui1["text"])
	pico_salida_historico_1_rango_1.config(text=pico_salida_liqui1["text"])
	series_histirico_1_rango_1.config(text=series_liquidacionr1["text"])
	carton_salida_historico_1_rango_1.config(text=carton_salida_liqui1["text"])

	liquidacion_historico_1_rango2.config(text=liquidacion_liqui2["text"])
	series_histirico_1_rango_2.config(text=series_liquidacionr2["text"])
	carton_salida_historico_1_rango_2.config(text=carton_salida_liqui2["text"])

	liquidacion_historico_1_rango3.config(text=liquidacion_liqui3["text"])
	series_histirico_1_rango_3.config(text=series_liquidacionr3["text"])
	carton_salida_historico_1_rango_3.config(text=carton_salida_liqui3["text"])

	liquidacion_historico_1_rango4.config(text=liquidacion_liqui4["text"])
	series_histirico_1_rango_4.config(text=series_liquidacionr4["text"])
	carton_salida_historico_1_rango_4.config(text=carton_salida_liqui4["text"])

	liquidacion_historico_1_rango5.config(text=liquidacion_liqui5["text"])
	series_histirico_1_rango_5.config(text=series_liquidacionr5["text"])
	carton_salida_historico_1_rango_5.config(text=carton_salida_liqui5["text"])

	liquidacion_historico_1_rango6.config(text=liquidacion_liqui6["text"])
	series_histirico_1_rango_6.config(text=series_liquidacionr6["text"])
	carton_salida_historico_1_rango_6.config(text=carton_salida_liqui6["text"])

	liquidacion_historico_1_rango7.config(text=liquidacion_liqui7["text"])
	series_histirico_1_rango_7.config(text=series_liquidacionr7["text"])
	carton_salida_historico_1_rango_7.config(text=carton_salida_liqui7["text"])

	liquidacion_historico_1_rango8.config(text=liquidacion_liqui8["text"])
	series_histirico_1_rango_8.config(text=series_liquidacionr8["text"])
	carton_salida_historico_1_rango_8.config(text=carton_salida_liqui8["text"])

	liquidacion_historico_1_rango9.config(text=liquidacion_liqui9["text"])
	series_histirico_1_rango_9.config(text=series_liquidacionr9["text"])
	carton_salida_historico_1_rango_9.config(text=carton_salida_liqui9["text"])

	liquidacion_historico_1_cierre.config(text=liquidacion_liqui_cierre["text"])
	pico_historico_1_cierre.config(text=pico_cierre_liqui["text"])
	series_historico_1_cierre.config(text=series_liquidacion_cierre["text"])
	carton_salida_historico_1_cierre.config(text=carton_salida_liqui1_cierre["text"])

	liquidacion_historico_1_total.config(text=liquidacion_liqui_total["text"])
	total_series_historico_1.config(text=total_series_liqui["text"])
	total_cartones_historico_1.config(text=total_cartones_liquidacion["text"])

def datos_historico2():
	pico_salida_historico_2_rango_1.config(text=pico_salida_historico_1_rango_1["text"])
	series_histirico_2_rango_1.config(text=series_histirico_1_rango_1["text"])
	carton_salida_historico_2_rango_1.config(text=carton_salida_historico_1_rango_1["text"])

	series_histirico_2_rango_2.config(text=series_histirico_1_rango_2["text"])
	carton_salida_historico_2_rango_2.config(text=carton_salida_historico_1_rango_2["text"])

	series_histirico_2_rango_3.config(text=series_histirico_1_rango_3["text"])
	carton_salida_historico_2_rango_3.config(text=carton_salida_historico_1_rango_3["text"])

	series_histirico_2_rango_4.config(text=series_histirico_1_rango_4["text"])
	carton_salida_historico_2_rango_4.config(text=carton_salida_historico_1_rango_4["text"])

	series_histirico_2_rango_5.config(text=series_histirico_1_rango_5["text"])
	carton_salida_historico_2_rango_5.config(text=carton_salida_historico_1_rango_5["text"])

	series_histirico_2_rango_6.config(text=series_histirico_1_rango_6["text"])
	carton_salida_historico_2_rango_6.config(text=carton_salida_historico_1_rango_6["text"])

	series_histirico_2_rango_7.config(text=series_histirico_1_rango_7["text"])
	carton_salida_historico_2_rango_7.config(text=carton_salida_historico_1_rango_7["text"])

	series_histirico_2_rango_8.config(text=series_histirico_1_rango_8["text"])
	carton_salida_historico_2_rango_8.config(text=carton_salida_historico_1_rango_8["text"])

	series_histirico_2_rango_9.config(text=series_histirico_1_rango_9["text"])
	carton_salida_historico_2_rango_9.config(text=carton_salida_historico_1_rango_9["text"])

	pico_historico_2_cierre.config(text=pico_historico_1_cierre["text"])
	series_historico_2_cierre.config(text=series_historico_1_cierre["text"])
	carton_salida_historico_2_cierre.config(text=carton_salida_historico_1_cierre["text"])

	total_series_historico_2.config(text=total_series_historico_1["text"])
	total_cartones_historico_2.config(text=total_cartones_historico_1["text"])

	datos_historico1()

def datos_historico3():
	pico_salida_historico_3_rango_1.config(text=pico_salida_historico_2_rango_1["text"])
	series_histirico_3_rango_1.config(text=series_histirico_2_rango_1["text"])
	carton_salida_historico_3_rango_1.config(text=carton_salida_historico_2_rango_1["text"])

	series_histirico_3_rango_2.config(text=series_histirico_2_rango_2["text"])
	carton_salida_historico_3_rango_2.config(text=carton_salida_historico_2_rango_2["text"])

	series_histirico_3_rango_3.config(text=series_histirico_2_rango_3["text"])
	carton_salida_historico_3_rango_3.config(text=carton_salida_historico_2_rango_3["text"])

	series_histirico_3_rango_4.config(text=series_histirico_2_rango_4["text"])
	carton_salida_historico_3_rango_4.config(text=carton_salida_historico_2_rango_4["text"])

	series_histirico_3_rango_5.config(text=series_histirico_2_rango_5["text"])
	carton_salida_historico_3_rango_5.config(text=carton_salida_historico_2_rango_5["text"])

	series_histirico_3_rango_6.config(text=series_histirico_2_rango_6["text"])
	carton_salida_historico_3_rango_6.config(text=carton_salida_historico_2_rango_6["text"])

	series_histirico_3_rango_7.config(text=series_histirico_2_rango_7["text"])
	carton_salida_historico_3_rango_7.config(text=carton_salida_historico_2_rango_7["text"])

	series_histirico_3_rango_8.config(text=series_histirico_2_rango_8["text"])
	carton_salida_historico_3_rango_8.config(text=carton_salida_historico_2_rango_8["text"])

	series_histirico_3_rango_9.config(text=series_histirico_2_rango_9["text"])
	carton_salida_historico_3_rango_9.config(text=carton_salida_historico_2_rango_9["text"])

	pico_historico_3_cierre.config(text=pico_historico_2_cierre["text"])
	series_historico_3_cierre.config(text=series_historico_2_cierre["text"])
	carton_salida_historico_3_cierre.config(text=carton_salida_historico_2_cierre["text"])

	total_series_historico_3.config(text=total_series_historico_2["text"])
	total_cartones_historico_3.config(text=total_cartones_historico_2["text"])

	datos_historico2()

def datos_historico4():
	pico_salida_historico_4_rango_1.config(text=pico_salida_historico_3_rango_1["text"])
	series_histirico_4_rango_1.config(text=series_histirico_3_rango_1["text"])
	carton_salida_historico_4_rango_1.config(text=carton_salida_historico_3_rango_1["text"])

	series_histirico_4_rango_2.config(text=series_histirico_3_rango_2["text"])
	carton_salida_historico_4_rango_2.config(text=carton_salida_historico_3_rango_2["text"])

	series_histirico_4_rango_3.config(text=series_histirico_3_rango_3["text"])
	carton_salida_historico_4_rango_3.config(text=carton_salida_historico_3_rango_3["text"])

	series_histirico_4_rango_4.config(text=series_histirico_3_rango_4["text"])
	carton_salida_historico_4_rango_4.config(text=carton_salida_historico_3_rango_4["text"])

	series_histirico_4_rango_5.config(text=series_histirico_3_rango_5["text"])
	carton_salida_historico_4_rango_5.config(text=carton_salida_historico_3_rango_5["text"])

	series_histirico_4_rango_6.config(text=series_histirico_3_rango_6["text"])
	carton_salida_historico_4_rango_6.config(text=carton_salida_historico_3_rango_6["text"])

	series_histirico_4_rango_7.config(text=series_histirico_3_rango_7["text"])
	carton_salida_historico_4_rango_7.config(text=carton_salida_historico_3_rango_7["text"])

	series_histirico_4_rango_8.config(text=series_histirico_3_rango_8["text"])
	carton_salida_historico_4_rango_8.config(text=carton_salida_historico_3_rango_8["text"])

	series_histirico_4_rango_9.config(text=series_histirico_3_rango_9["text"])
	carton_salida_historico_4_rango_9.config(text=carton_salida_historico_3_rango_9["text"])

	pico_historico_4_cierre.config(text=pico_historico_3_cierre["text"])
	series_historico_4_cierre.config(text=series_historico_3_cierre["text"])
	carton_salida_historico_4_cierre.config(text=carton_salida_historico_3_cierre["text"])

	total_series_historico_4.config(text=total_series_historico_3["text"])
	total_cartones_historico_4.config(text=total_cartones_historico_3["text"])

	datos_historico3()

def datos_historico5():
	pico_salida_historico_5_rango_1.config(text=pico_salida_historico_4_rango_1["text"])
	series_histirico_5_rango_1.config(text=series_histirico_4_rango_1["text"])
	carton_salida_historico_5_rango_1.config(text=carton_salida_historico_4_rango_1["text"])

	series_histirico_5_rango_2.config(text=series_histirico_4_rango_2["text"])
	carton_salida_historico_5_rango_2.config(text=carton_salida_historico_4_rango_2["text"])

	series_histirico_5_rango_3.config(text=series_histirico_4_rango_3["text"])
	carton_salida_historico_5_rango_3.config(text=carton_salida_historico_4_rango_3["text"])

	series_histirico_5_rango_4.config(text=series_histirico_4_rango_4["text"])
	carton_salida_historico_5_rango_4.config(text=carton_salida_historico_4_rango_4["text"])

	series_histirico_5_rango_5.config(text=series_histirico_4_rango_5["text"])
	carton_salida_historico_5_rango_5.config(text=carton_salida_historico_4_rango_5["text"])

	series_histirico_5_rango_6.config(text=series_histirico_4_rango_6["text"])
	carton_salida_historico_5_rango_6.config(text=carton_salida_historico_4_rango_6["text"])

	series_histirico_5_rango_7.config(text=series_histirico_4_rango_7["text"])
	carton_salida_historico_5_rango_7.config(text=carton_salida_historico_4_rango_7["text"])

	series_histirico_5_rango_8.config(text=series_histirico_4_rango_8["text"])
	carton_salida_historico_5_rango_8.config(text=carton_salida_historico_4_rango_8["text"])

	series_histirico_5_rango_9.config(text=series_histirico_4_rango_9["text"])
	carton_salida_historico_5_rango_9.config(text=carton_salida_historico_4_rango_9["text"])

	pico_historico_5_cierre.config(text=pico_historico_4_cierre["text"])
	series_historico_5_cierre.config(text=series_historico_4_cierre["text"])
	carton_salida_historico_5_cierre.config(text=carton_salida_historico_4_cierre["text"])

	total_series_historico_5.config(text=total_series_historico_4["text"])
	total_cartones_historico_5.config(text=total_cartones_historico_4["text"])

	datos_historico4()

def datos_historico6():
	pico_salida_historico_6_rango_1.config(text=pico_salida_historico_5_rango_1["text"])
	series_histirico_6_rango_1.config(text=series_histirico_5_rango_1["text"])
	carton_salida_historico_6_rango_1.config(text=carton_salida_historico_5_rango_1["text"])

	series_histirico_6_rango_2.config(text=series_histirico_5_rango_2["text"])
	carton_salida_historico_6_rango_2.config(text=carton_salida_historico_5_rango_2["text"])

	series_histirico_6_rango_3.config(text=series_histirico_5_rango_3["text"])
	carton_salida_historico_6_rango_3.config(text=carton_salida_historico_5_rango_3["text"])

	series_histirico_6_rango_4.config(text=series_histirico_5_rango_4["text"])
	carton_salida_historico_6_rango_4.config(text=carton_salida_historico_5_rango_4["text"])

	series_histirico_6_rango_5.config(text=series_histirico_5_rango_5["text"])
	carton_salida_historico_6_rango_5.config(text=carton_salida_historico_5_rango_5["text"])

	series_histirico_6_rango_6.config(text=series_histirico_5_rango_6["text"])
	carton_salida_historico_6_rango_6.config(text=carton_salida_historico_5_rango_6["text"])

	series_histirico_6_rango_7.config(text=series_histirico_5_rango_7["text"])
	carton_salida_historico_6_rango_7.config(text=carton_salida_historico_5_rango_7["text"])

	series_histirico_6_rango_8.config(text=series_histirico_5_rango_8["text"])
	carton_salida_historico_6_rango_8.config(text=carton_salida_historico_5_rango_8["text"])

	series_histirico_6_rango_9.config(text=series_histirico_5_rango_9["text"])
	carton_salida_historico_6_rango_9.config(text=carton_salida_historico_5_rango_9["text"])

	pico_historico_6_cierre.config(text=pico_historico_5_cierre["text"])
	series_historico_6_cierre.config(text=series_historico_5_cierre["text"])
	carton_salida_historico_6_cierre.config(text=carton_salida_historico_5_cierre["text"])

	total_series_historico_6.config(text=total_series_historico_5["text"])
	total_cartones_historico_6.config(text=total_cartones_historico_5["text"])

	datos_historico5()

def poner_al_frente_raiz():
	raiz.focus_force()
	CierreTotal.focus()

def poner_al_frente_root():
	root.focus_force()

def prueba(event): #funciona al pulsar intro en el cierre
	total_cartones_1()
	total_cartones_2()
	total_cartones_3()
	total_cartones_6()
	pico_cie_ini = pico_cierre()
	pico_final.config(text = pico_cie_ini)

def focus_next_window(event):
	CartonSalida_1()
	CartonSalida_1_proxima()
	CierreTotal.focus()

def focus_next_window_2(event):
	CartonSalida_2()
	CartonSalida_2_proxima()
	CierreTotal.focus()

def focus_next_window_3(event):
	CartonSalida_3()
	CartonSalida_3_proxima()
	CierreTotal.focus()

def focus_next_window_6(event):
	CartonSalida_6()
	CartonSalida_6_proxima()
	CierreTotal.focus()

def reset():
	global control_parpadeo_inicial; global valor1; global valor2; global valor3; global valor4; global valor5; global valor6
	global valor7; global valor8; global valor9; global historico
	valor1=0; valor2=0; valor3=0; valor4=0; valor5=0; valor6=0; valor7=0; valor8=0; valor9=0 

	historico = 1
	salida.set(0)
	salida_2.set(0)
	salida_3.set(0)
	salida_6.set(0)
	
	control_parpadeo_inicial = 0
	etiqueta_vacia.pack()
	boton_prepara_rectifica.config(text="COMENZAR")
	etiquita_instrucciones_inicial.pack()
	parpadeo_inicial(etiquita_instrucciones_inicial)

	numero_series_rango1.config(text=0)
	numero_series_rango2.config(text=0)
	numero_series_rango3.config(text=0)
	numero_series_rango4.config(text=0)
	numero_series_rango5.config(text=0)
	numero_series_rango6.config(text=0)
	numero_series_rango7.config(text=0)
	numero_series_rango8.config(text=0)
	numero_series_rango9.config(text=0)

	CartonSalida_1()
	CartonSalida_2()
	CartonSalida_3()
	CartonSalida_6()

	pico_r1.config(text=0)
	pico_r1_2.config(text=0)
	pico_r1_3.config(text=0)
	pico_r1_6.config(text=0)
	cartones_cierre.config(text=0)
	cartones_cierre_2.config(text=0)
	cartones_cierre_3.config(text=0)
	cartones_cierre_6.config(text=0)
	total_car_1.config(text=0)
	total_car_2.config(text=0)
	total_car_3.config(text=0)
	total_car_6.config(text=0)
	numero_series1.config(text=valor1)
	numero_series2.config(text=valor2)
	numero_series3.config(text=valor3)
	numero_series4.config(text=valor4)
	numero_series5.config(text=valor5)
	numero_series6.config(text=valor6)
	numero_series7.config(text=valor7)
	numero_series8.config(text=valor8)
	numero_series9.config(text=valor9)

	salida.set("")
	salida_2.set("")
	salida_3.set("")
	salida_6.set("")
	cierre.set("")
	SalidaEntry_1.focus()

def parpadeo_inicial(etiquita_instrucciones_inicial):
	if control_parpadeo_inicial == 0:
		if etiquita_instrucciones_inicial.cget("foreground") == "red":
			etiquita_instrucciones_inicial.config (foreground="black")
		else:
			etiquita_instrucciones_inicial.config(foreground="red")
		etiquita_instrucciones_inicial.after(1100, parpadeo_inicial, etiquita_instrucciones_inicial)
	else:
		pass

def atras():
	global bandera
	global control_atras; global serie_r1_atras; global serie_r2_atras; global serie_r3_atras; global serie_r4_atras;
	global serie_r5_atras; global serie_r6_atras; global serie_r7_atras; global serie_r8_atras; global serie_r9_atras;
	global series_liquidacion_atras_r1; global control_parpadeo; global historico

	control_parpadeo = 1
	historico = 0
	bandera = 1

	serie_r1_atras = numero_series_rango1["text"]
	serie_r2_atras = numero_series_rango2["text"]
	serie_r3_atras = numero_series_rango3["text"]
	serie_r4_atras = numero_series_rango4["text"]
	serie_r5_atras = numero_series_rango5["text"]
	serie_r6_atras = numero_series_rango6["text"]
	serie_r7_atras = numero_series_rango7["text"]
	serie_r8_atras = numero_series_rango8["text"]
	serie_r9_atras = numero_series_rango9["text"]

	boton_atras['state'] = DISABLED

	if control_atras == 1:
		try:
			salida_1 = int(SalidaEntry_1.get()) - int(total_cartones_liquidacion["text"])
			cierre_atras = int(SalidaEntry_1.get()) - 1
			if cierre_atras == 0:
				cierre.set(1800)
			else:
				cierre.set(cierre_atras)

			if salida_1 < 0:
				salida.set(salida_1 + 1800)
			else:
				salida.set(salida_1)
		except:
			pass
	elif control_atras == 2:
		try:
			salida2 = int(SalidaEntry_2.get()) - int(total_cartones_liquidacion["text"])
			cierre_atras = int(SalidaEntry_2.get()) - 1
			if cierre_atras == 0:
				cierre.set(1800)
			else:
				cierre.set(cierre_atras)

			if salida2 < 0:
				salida_2.set(salida2 + 1800)
			else:
				salida_2.set(salida2)
		except:
			pass
	elif control_atras == 3:
		try:
			salida3 = int(SalidaEntry_3.get()) - int(total_cartones_liquidacion["text"])
			cierre_atras = int(SalidaEntry_3.get()) - 1
			if cierre_atras == 0:
				cierre.set(1800)
			else:
				cierre.set(cierre_atras)

			if salida3 < 0:
				salida_3.set(salida3 + 1800)
			else:
				salida_3.set(salida3)
		except:
			pass
	else:
		try:
			salida6 = int(SalidaEntry_6.get()) - int(total_cartones_liquidacion["text"])
			cierre_atras = int(SalidaEntry_6.get()) - 1
			if cierre_atras == 0:
				cierre.set(1800)
			else:
				cierre.set(cierre_atras)

			if salida6 < 0:
				salida_6.set(salida6 + 1800)
			else:
				salida_6.set(salida6)
		except:
			pass

	CierreTotal.icursor(END)
	liquidacion_atras()
	CartonSalida_1()
	CartonSalida_2()
	CartonSalida_3()
	CartonSalida_6()
	total_cartones_1()
	total_cartones_2()
	total_cartones_3()
	total_cartones_6()
	CartonSalida_1_proxima()
	CartonSalida_2_proxima()
	CartonSalida_3_proxima()
	CartonSalida_6_proxima()

def totalCaja():
	global liquida_total
	try:	
		total_linea = float(liquida_total[0] * 0.085)
		total_linea_redondeado = round(total_linea, 2),"€"
		linea.set(total_linea_redondeado)

		total_bingo = float(liquida_total[0] * 0.54)
		total_bingo_redondeado = round(total_bingo, 2),"€"
		bingo.set(total_bingo_redondeado)		
		
		total_caja =float(liquida_total[0] * 0.37)
		total_caja_redondeado = round(total_caja, 2),"€"
		caja_partida.set(total_caja_redondeado)
	except:
		pass

def PreparaRectifica():
	global bandera
	global serie_r1_atras; global serie_r2_atras; global serie_r3_atras; global serie_r4_atras;
	global serie_r5_atras; global serie_r6_atras; global serie_r7_atras; global serie_r8_atras; global serie_r9_atras;
	global control_parpadeo_inicial

	boton_sube_ahora1['state'] = NORMAL
	boton_sube_ahora1.config(text="SUBIR", bg="#8B0000")
	boton_sube_ahora2['state'] = NORMAL
	boton_sube_ahora2.config(text="SUBIR", bg="#8B0000")
	boton_sube_ahora3['state'] = NORMAL
	boton_sube_ahora3.config(text="SUBIR", bg="#8B0000")
	boton_sube_ahora4['state'] = NORMAL
	boton_sube_ahora4.config(text="SUBIR", bg="#8B0000")
	boton_sube_ahora5['state'] = NORMAL
	boton_sube_ahora5.config(text="SUBIR", bg="#8B0000")
	boton_sube_ahora6['state'] = NORMAL
	boton_sube_ahora6.config(text="SUBIR", bg="#8B0000")
	boton_sube_ahora7['state'] = NORMAL
	boton_sube_ahora7.config(text="SUBIR", bg="#8B0000")
	boton_sube_ahora8['state'] = NORMAL
	boton_sube_ahora8.config(text="SUBIR", bg="#8B0000")
	boton_sube_ahora9['state'] = NORMAL
	boton_sube_ahora9.config(text="SUBIR", bg="#8B0000")

	valor_atras = 1
	boton_prepara_rectifica.config(text="     SUBIR TODOS     ")
	etiquita_instrucciones_inicial.pack_forget()
	control_parpadeo_inicial = 1

	if bandera == 1:
		numero_series_rango1.config(text=serie_r1_atras)
		numero_series_rango2.config(text=serie_r2_atras)
		numero_series_rango3.config(text=serie_r3_atras)
		numero_series_rango4.config(text=serie_r4_atras)
		numero_series_rango5.config(text=serie_r5_atras)
		numero_series_rango6.config(text=serie_r6_atras)
		numero_series_rango7.config(text=serie_r7_atras)
		numero_series_rango8.config(text=serie_r8_atras)
		numero_series_rango9.config(text=serie_r9_atras)
	else:
		numero_series_rango1.config(text=numero_series1["text"], fg = "blue")
		numero_series_rango2.config(text=numero_series2["text"], fg = "blue")
		numero_series_rango3.config(text=numero_series3["text"], fg = "blue")
		numero_series_rango4.config(text=numero_series4["text"], fg = "blue")
		numero_series_rango5.config(text=numero_series5["text"], fg = "blue")
		numero_series_rango6.config(text=numero_series6["text"], fg = "blue")
		numero_series_rango7.config(text=numero_series7["text"], fg = "blue")
		numero_series_rango8.config(text=numero_series8["text"], fg = "blue")
		numero_series_rango9.config(text=numero_series9["text"], fg = "blue")

	CartonSalida_1()
	CartonSalida_2()
	CartonSalida_3()
	CartonSalida_6()
	cambiaColor()
	bandera = 0

def liquidacion_atras():
	numero_series_rango1.config(text=series_liquidacionr1["text"])
	numero_series_rango2.config(text=series_liquidacionr2["text"])
	numero_series_rango3.config(text=series_liquidacionr3["text"])
	numero_series_rango4.config(text=series_liquidacionr4["text"])
	numero_series_rango5.config(text=series_liquidacionr5["text"])
	numero_series_rango6.config(text=series_liquidacionr6["text"])
	numero_series_rango7.config(text=series_liquidacionr7["text"])
	numero_series_rango8.config(text=series_liquidacionr8["text"])
	numero_series_rango9.config(text=series_liquidacionr9["text"])

	series_liquidacionr1.config(text=series_liquidacion_atras_r1)
	series_liquidacionr2.config(text=series_liquidacion_atras_r2)
	series_liquidacionr3.config(text=series_liquidacion_atras_r3)
	series_liquidacionr4.config(text=series_liquidacion_atras_r4)
	series_liquidacionr5.config(text=series_liquidacion_atras_r5)
	series_liquidacionr6.config(text=series_liquidacion_atras_r6)
	series_liquidacionr7.config(text=series_liquidacion_atras_r7)
	series_liquidacionr8.config(text=series_liquidacion_atras_r8)
	series_liquidacionr9.config(text=series_liquidacion_atras_r9)
	series_liquidacion_cierre.config(text=series_liquidacion_atras_cierre)

	total_series_liqui.config(text=series_liquidacion_atras_total)
	pico_salida_liqui1.config(text=pico_salida_liqui1_atras)
	pico_cierre_liqui.config(text=pico_cierre_liqui_atras)

	carton_salida_liqui1.config(text=carton_salida_liqui1_atras)
	carton_salida_liqui2.config(text=carton_salida_liqui2_atras)
	carton_salida_liqui3.config(text=carton_salida_liqui3_atras)
	carton_salida_liqui4.config(text=carton_salida_liqui4_atras)
	carton_salida_liqui5.config(text=carton_salida_liqui5_atras)
	carton_salida_liqui6.config(text=carton_salida_liqui6_atras)
	carton_salida_liqui7.config(text=carton_salida_liqui7_atras)
	carton_salida_liqui8.config(text=carton_salida_liqui8_atras)
	carton_salida_liqui9.config(text=carton_salida_liqui9_atras)
	carton_salida_liqui1_cierre.config(text=carton_salida_liqui1_cierre_atras)
	total_cartones_liquidacion.config(text=total_cartones_liquidacion_atras)

	labels = [series_liquidacionr1, series_liquidacionr2,series_liquidacionr3,series_liquidacionr4,series_liquidacionr5,series_liquidacionr6,
		series_liquidacionr7,series_liquidacionr8,series_liquidacionr9,series_liquidacion_cierre,total_series_liqui,pico_salida_liqui1,
		pico_cierre_liqui,carton_salida_liqui1,carton_salida_liqui2,carton_salida_liqui3,carton_salida_liqui4,carton_salida_liqui5,
		carton_salida_liqui6,carton_salida_liqui7,carton_salida_liqui8,carton_salida_liqui9,carton_salida_liqui1_cierre,total_cartones_liquidacion]#,label_liquidacion
	
	for label in labels:
		label.config(fg="black")

	liquidacion_liqui1.config(text=liquidacion_liqui1_atras)
	liquidacion_liqui2.config(text=liquidacion_liqui2_atras)
	liquidacion_liqui3.config(text=liquidacion_liqui3_atras)
	liquidacion_liqui4.config(text=liquidacion_liqui4_atras)
	liquidacion_liqui5.config(text=liquidacion_liqui5_atras)
	liquidacion_liqui6.config(text=liquidacion_liqui6_atras)
	liquidacion_liqui7.config(text=liquidacion_liqui7_atras)
	liquidacion_liqui8.config(text=liquidacion_liqui8_atras)
	liquidacion_liqui9.config(text=liquidacion_liqui9_atras)
	liquidacion_liqui_cierre.config(text=liquidacion_liqui_cierre_atras)
	liquidacion_liqui_total.config(text=liquidacion_liqui_total_atras)

def cerrar():
	valor=MessageBox.askquestion("Salir", "¿Deseas salir de la aplicación?")
	if valor=="yes":
		ejecutar()

def total_cartones_1():
	if SalidaEntry_1.get() == 0 or SalidaEntry_1.get() == "":
		totalCar = 0
	else:
		try:
			if int(SalidaEntry_1.get()) > int(CierreTotal.get()):
				totalCar = 1800 - int(SalidaEntry_1.get()) + int(CierreTotal.get()) + 1
				total_car_1.config(text = totalCar)
				return totalCar
			else:
				totalCar = int(CierreTotal.get()) - int(SalidaEntry_1.get()) + 1
				total_car_1.config(text = totalCar)
				return totalCar
		except:
			pass
	return totalCar

def total_cartones_2():
	totalCar_2 = 0
	if SalidaEntry_2.get() == 0 or SalidaEntry_2.get() == "":
		totalCar_2 = 0
	else:
		try:
			if int(SalidaEntry_2.get()) > int(CierreTotal.get()):
				totalCar_2 = 1800 - int(SalidaEntry_2.get()) + int(CierreTotal.get()) + 1
			else:
				totalCar_2 = int(CierreTotal.get()) - int(SalidaEntry_2.get()) + 1
		except:
			pass
	total_car_2.config(text = totalCar_2)
	return totalCar_2

def total_cartones_3():
	totalCar_3 = 0
	if SalidaEntry_3.get() == 0 or SalidaEntry_3.get() == "":
		totalCar_3 = 0
	else:
		try:
			if int(SalidaEntry_3.get()) > int(CierreTotal.get()):
				totalCar_3 = 1800 - int(SalidaEntry_3.get()) + int(CierreTotal.get()) + 1
			else:
				totalCar_3 = int(CierreTotal.get()) - int(SalidaEntry_3.get()) + 1
		except:
			pass
	total_car_3.config(text = totalCar_3)
	return totalCar_3

def total_cartones_6():
	totalCar_6 = 0
	if SalidaEntry_6.get() == 0 or SalidaEntry_6.get() == "":
		totalCar_6 = 0
	else:
		try:
			if int(SalidaEntry_6.get()) > int(CierreTotal.get()):
				totalCar_6 = 1800 - int(SalidaEntry_6.get()) + int(CierreTotal.get()) + 1
				total_car_6.config(text = totalCar_6)
			else:
				totalCar_6 = int(CierreTotal.get()) - int(SalidaEntry_6.get()) + 1
				total_car_6.config(text = totalCar_6)
		except:
			pass
	total_car_6.config(text = totalCar_6)		
	return totalCar_6

def subir(num):
	if num == 1:
		numero_series_rango1.config(text=numero_series1["text"])
	elif num == 2:
 		numero_series_rango2.config(text=numero_series2["text"])
	elif num == 3:
 		numero_series_rango3.config(text=numero_series3["text"])
	elif num == 4:
 		numero_series_rango4.config(text=numero_series4["text"])
	elif num == 5:
 		numero_series_rango5.config(text=numero_series5["text"])
	elif num == 6:
 		numero_series_rango6.config(text=numero_series6["text"])
	elif num == 7:
 		numero_series_rango7.config(text=numero_series7["text"])
	elif num == 8:
 		numero_series_rango8.config(text=numero_series8["text"])
	elif num == 9:
 		numero_series_rango9.config(text=numero_series9["text"])

	CartonSalida_1()
	CartonSalida_2()
	CartonSalida_3()
	CartonSalida_6()
	cambiaColor()

def incrementar(num):
	global valor1; global valor2; global valor3; global valor4; global valor5
	global valor6; global valor7; global valor8; global valor9

	if num == 1:
		valor1 = valor1 + 1
		numero_series1.config(text=valor1)

	if num == 2:
		valor2 = valor2 + 1
		numero_series2.config(text=valor2) 

	if num == 3:
		valor3 = valor3 + 1
		numero_series3.config(text=valor3)

	if num == 4:
		valor4 = valor4 + 1
		numero_series4.config(text=valor4)

	if num == 5:
		valor5 = valor5 + 1
		numero_series5.config(text=valor5)

	if num == 6:
		valor6 = valor6 + 1
		numero_series6.config(text=valor6)

	if num == 7:
		valor7 = valor7 + 1
		numero_series7.config(text=valor7)

	if num == 8:
		valor8 = valor8 + 1
		numero_series8.config(text=valor8)

	if num == 9:
		valor9 = valor9 + 1
		numero_series9.config(text=valor9)

	CartonSalida_1_proxima()
	CartonSalida_2_proxima()
	CartonSalida_3_proxima()
	CartonSalida_6_proxima()

def decrementar(num):
	global valor1; global valor2; global valor3; global valor4; global valor5
	global valor6; global valor7; global valor8; global valor9
	
	if num == 1 :
		if valor1 == 0 :
	 		numero_series1.config(text=valor1)
		else:
			valor1 = valor1 - 1
			numero_series1.config(text=valor1)

	if num == 2 :
		if valor2 == 0 :
	 		numero_series2.config(text=valor2)
		else:
			valor2 = valor2 - 1
			numero_series2.config(text=valor2)

	if num == 3:
		if valor3 == 0 :
	 		numero_series3.config(text=valor3)
		else:
			valor3 = valor3 - 1
			numero_series3.config(text=valor3)

	if num == 4:
		if valor4 == 0 :
	 		numero_series4.config(text=valor4)
		else:
			valor4 = valor4 - 1
			numero_series4.config(text=valor4)

	if num == 5:
		if valor5 == 0 :
	 		numero_series5.config(text=valor5)
		else:
			valor5 = valor5 - 1
			numero_series5.config(text=valor5)

	if num == 6:
		if valor6 == 0 :
	 		numero_series6.config(text=valor6)
		else:
			valor6 = valor6 - 1
			numero_series6.config(text=valor6)

	if num == 7:
		if valor7 == 0 :
	 		numero_series7.config(text=valor7)
		else:
			valor7 = valor7 - 1
			numero_series7.config(text=valor7)

	if num == 8:
		if valor8 == 0 :
	 		numero_series8.config(text=valor8)
		else:
			valor8 = valor8 - 1
			numero_series8.config(text=valor8)

	if num == 9:
		if valor9 == 0 :
	 		numero_series9.config(text=valor9)
		else:
			valor9 = valor9 - 1
			numero_series9.config(text=valor9)

	CartonSalida_1_proxima()
	CartonSalida_2_proxima()
	CartonSalida_3_proxima()
	CartonSalida_6_proxima()

def pico_salida_1():
	try:
		if SalidaEntry_1.get() == 0 or SalidaEntry_1.get() == "":
			pass
		else:
			pico_sal_1 = 7 - (int(SalidaEntry_1.get()) % 6)

			if pico_sal_1 == 7:
				return 1
			elif pico_sal_1 == 6:
				return 0
			else:
				return pico_sal_1
	except:
		pass

def pico_salid_2():
	try:
		if SalidaEntry_2.get() == 0 or SalidaEntry_2.get() == "":
			pass
		else:
			pico_sal_2 = 7 - (int(SalidaEntry_2.get()) % 6)

			if pico_sal_2 == 7:
				return 1
			elif pico_sal_2 == 6:
				return 0
			else:
				return pico_sal_2
	except:
		pass

def pico_salid_3():
	try:
		if SalidaEntry_3.get() == 0 or SalidaEntry_3.get() == "":
			pass
		else:
			pico_sal_3 = 7 - (int(SalidaEntry_3.get()) % 6)

			if pico_sal_3 == 7:
				return 1
			elif pico_sal_3 == 6:
				return 0
			else:
				return pico_sal_3
	except:
		pass

def pico_salid_6():
	try:
		if SalidaEntry_6.get() == 0 or SalidaEntry_6.get() == "":
			pass
		else:
			pico_sal_6 = 7 - (int(SalidaEntry_6.get()) % 6)

			if pico_sal_6 == 7:
				return 1
			elif pico_sal_6 == 6:
				return 0
			else:
				return pico_sal_6
	except:
		pass

def pico_cierre():
	try:
		if CierreTotal.get() == 0 or CierreTotal.get() == "":
			pass
		else:
			pico_cie = (int(cierre.get()) % 6)
			pico_final.config(text = pico_cie)
			return pico_cie
	except:
		pass

def CartonSalida_1():
	pico_salida = pico_salida_1()

	cambiaColor()	

	try:
		if SalidaEntry_1.get() == "":
			pass
		else:
			CarSalR = SalidaEntry_1.get()
			CarSalR1 = int(CarSalR)
			pico_r1.config(text=pico_salida)

			#----Rango 2-----

			if int(numero_series_rango2["text"]) == 0 :
				cartones_r2.config(text=0)
			else:
				CarSalR2 = CarSalR1 + pico_salida + (int(numero_series_rango1["text"]) * 6)
				if CarSalR2 > 1800:
					cartones_r2.config(text=CarSalR2 - 1800)
				else:
					cartones_r2.config(text=CarSalR2)
				
			#----Rango 3-----

			if int(numero_series_rango3["text"]) == 0 :
				cartones_r3.config(text=0)
			else:
				CarSalR3 = CarSalR1 + pico_salida + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6)
				if CarSalR3 > 1800:
					cartones_r3.config(text=CarSalR3 - 1800)
				else:
					cartones_r3.config(text=CarSalR3)

			#----Rango 4-----

			if int(numero_series_rango4["text"]) == 0 :
				cartones_r4.config(text=0)
			else:
				CarSalR4 = CarSalR1 + pico_salida + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6)
				if CarSalR4 > 1800:
					cartones_r4.config(text=CarSalR4 - 1800)
				else:
					cartones_r4.config(text=CarSalR4)

			#----Rango 5-----

			if int(numero_series_rango5["text"]) == 0 :
				cartones_r5.config(text=0)
			else:
				CarSalR5 = CarSalR1 + pico_salida + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6)
				if CarSalR5 > 1800:
					cartones_r5.config(text=CarSalR5 - 1800)
				else:
					cartones_r5.config(text=CarSalR5)

			#----Rango 6-----

			if int(numero_series_rango6["text"]) == 0 :
				cartones_r6.config(text=0)
			else:
				CarSalR6 = CarSalR1 + pico_salida + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6)
				if CarSalR6 > 1800:
					cartones_r6.config(text=CarSalR6 - 1800)
				else:
					cartones_r6.config(text=CarSalR6)

			#----Rango 7-----

			if int(numero_series_rango7["text"]) == 0 :
				cartones_r7.config(text=0)
			else:
				CarSalR7 = CarSalR1 + pico_salida + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6) + (int(numero_series_rango6["text"]) * 6)
				if CarSalR7 > 1800:
					cartones_r7.config(text=CarSalR7 - 1800)
				else:
					cartones_r7.config(text=CarSalR7)

			#----Rango 8-----

			if int(numero_series_rango8["text"]) == 0 :
				cartones_r8.config(text=0)
			else:
				CarSalR8 = CarSalR1 + pico_salida + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6) + (int(numero_series_rango6["text"]) * 6) + (int(numero_series_rango7["text"]) * 6)
				if CarSalR8 > 1800:
					cartones_r8.config(text=CarSalR8 - 1800)
				else:
					cartones_r8.config(text=CarSalR8)

			#----Rango 9-----

			if int(numero_series_rango9["text"]) == 0 :
				cartones_r9.config(text=0)
			else:
				CarSalR9 = CarSalR1 + pico_salida + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6) + (int(numero_series_rango6["text"]) * 6) + (int(numero_series_rango7["text"]) * 6) + (int(numero_series_rango8["text"]) * 6)
				if CarSalR9 > 1800:
					cartones_r9.config(text=CarSalR9 - 1800)
				else:
					cartones_r9.config(text=CarSalR9)

			#----Rango cierre-----

			CarSalCie = int(CarSalR1) + pico_salida + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6) + (int(numero_series_rango6["text"]) * 6) + (int(numero_series_rango7["text"]) * 6) + (int(numero_series_rango8["text"]) * 6) + (int(numero_series_rango9["text"]) * 6)
			if CarSalCie > 1800:
				cartones_cierre.config(text=CarSalCie - 1800)
			else:
				cartones_cierre.config(text=CarSalCie)
	except:
		pass

def CartonSalida_1_proxima():
	pico_salida = pico_salida_1()

	#cambiaColor()	
	try:
		if SalidaEntry_1.get() == "":
			cartones_r2_proxima.config(text=0)
			cartones_r3_proxima.config(text=0)
			cartones_r4_proxima.config(text=0)
			cartones_r5_proxima.config(text=0)
			cartones_r6_proxima.config(text=0)
			cartones_r7_proxima.config(text=0)
			cartones_r8_proxima.config(text=0)
			cartones_r9_proxima.config(text=0)
			cartones_cierre_proxima.config(text=0)
		else:
			CarSalR = SalidaEntry_1.get()
			CarSalR1 = int(CarSalR)
			pico_r1.config(text=pico_salida)

			#----Rango 2-----

			if int(numero_series2["text"]) == 0 :
				cartones_r2_proxima.config(text=0)
			else:
				CarSalR2 = CarSalR1 + pico_salida + (int(numero_series1["text"]) * 6)
				if CarSalR2 > 1800:
					cartones_r2_proxima.config(text=CarSalR2 - 1800)
				else:
					cartones_r2_proxima.config(text=CarSalR2)
				
			#----Rango 3-----

			if int(numero_series3["text"]) == 0 :
				cartones_r3_proxima.config(text=0)
			else:
				CarSalR3 = CarSalR1 + pico_salida + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6)
				if CarSalR3 > 1800:
					cartones_r3_proxima.config(text=CarSalR3 - 1800)
				else:
					cartones_r3_proxima.config(text=CarSalR3)

			#----Rango 4-----

			if int(numero_series4["text"]) == 0 :
				cartones_r4_proxima.config(text=0)
			else:
				CarSalR4 = CarSalR1 + pico_salida + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6)
				if CarSalR4 > 1800:
					cartones_r4_proxima.config(text=CarSalR4 - 1800)
				else:
					cartones_r4_proxima.config(text=CarSalR4)

			#----Rango 5-----

			if int(numero_series5["text"]) == 0 :
				cartones_r5_proxima.config(text=0)
			else:
				CarSalR5 = CarSalR1 + pico_salida + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6)
				if CarSalR5 > 1800:
					cartones_r5_proxima.config(text=CarSalR5 - 1800)
				else:
					cartones_r5_proxima.config(text=CarSalR5)

			#----Rango 6-----

			if int(numero_series6["text"]) == 0 :
				cartones_r6_proxima.config(text=0)
			else:
				CarSalR6 = CarSalR1 + pico_salida + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6) + (int(numero_series5["text"]) * 6)
				if CarSalR6 > 1800:
					cartones_r6_proxima.config(text=CarSalR6 - 1800)
				else:
					cartones_r6_proxima.config(text=CarSalR6)

			#----Rango 7-----

			if int(numero_series7["text"]) == 0 :
				cartones_r7_proxima.config(text=0)
			else:
				CarSalR7 = CarSalR1 + pico_salida + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6) + (int(numero_series5["text"]) * 6) + (int(numero_series6["text"]) * 6)
				if CarSalR7 > 1800:
					cartones_r7_proxima.config(text=CarSalR7 - 1800)
				else:
					cartones_r7_proxima.config(text=CarSalR7)

			#----Rango 8-----

			if int(numero_series8["text"]) == 0 :
				cartones_r8_proxima.config(text=0)
			else:
				CarSalR8 = CarSalR1 + pico_salida + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6) + (int(numero_series5["text"]) * 6) + (int(numero_series6["text"]) * 6) + (int(numero_series7["text"]) * 6)
				if CarSalR8 > 1800:
					cartones_r8_proxima.config(text=CarSalR8 - 1800)
				else:
					cartones_r8_proxima.config(text=CarSalR8)

			#----Rango 9-----

			if int(numero_series9["text"]) == 0 :
				cartones_r9_proxima.config(text=0)
			else:
				CarSalR9 = CarSalR1 + pico_salida + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6) + (int(numero_series5["text"]) * 6) + (int(numero_series6["text"]) * 6) + (int(numero_series7["text"]) * 6) + (int(numero_series8["text"]) * 6)
				if CarSalR9 > 1800:
					cartones_r9_proxima.config(text=CarSalR9 - 1800)
				else:
					cartones_r9_proxima.config(text=CarSalR9)

			#----Rango cierre-----

			CarSalCie = int(CarSalR1) + pico_salida + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6) + (int(numero_series5["text"]) * 6) + (int(numero_series6["text"]) * 6) + (int(numero_series7["text"]) * 6) + (int(numero_series8["text"]) * 6) + (int(numero_series9["text"]) * 6)
			if CarSalCie > 1800:
				cartones_cierre_proxima.config(text=CarSalCie - 1800)
			else:
				cartones_cierre_proxima.config(text=CarSalCie)
	except:
		pass

def CartonSalida_2():
	pico_salida_2 = pico_salid_2()
	try:
		if SalidaEntry_2.get() == "":
			pass
		else:
			CarSalR1 = SalidaEntry_2.get()
			CarSalR1_2 = int(CarSalR1)
			pico_r1_2.config(text=pico_salida_2)

			#----Rango 2-----

			if int(numero_series_rango2["text"]) == 0 :
				cartones_r2_2.config(text=0)
			else:
				CarSalR2_2 = CarSalR1_2 + pico_salida_2 + (int(numero_series_rango1["text"]) * 6) #
				if CarSalR2_2 > 1800:
					cartones_r2_2.config(text=CarSalR2_2 - 1800)
				else:
					cartones_r2_2.config(text=CarSalR2_2)
				
			#----Rango 3-----

			if int(numero_series_rango3["text"]) == 0 :
				cartones_r3_2.config(text=0)
			else:
				CarSalR3_2 = CarSalR1_2 + pico_salida_2 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6)
				if CarSalR3_2 > 1800:
					cartones_r3_2.config(text=CarSalR3_2 - 1800)
				else:
					cartones_r3_2.config(text=CarSalR3_2)

			#----Rango 4-----

			if int(numero_series_rango4["text"]) == 0 :
				cartones_r4_2.config(text=0)
			else:
				CarSalR4_2 = CarSalR1_2 + pico_salida_2 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6)
				if CarSalR4_2 > 1800:
					cartones_r4_2.config(text=CarSalR4_2 - 1800)
				else:
					cartones_r4_2.config(text=CarSalR4_2)

			#----Rango 5-----

			if int(numero_series_rango5["text"]) == 0 :
				cartones_r5_2.config(text=0)
			else:
				CarSalR5_2 = CarSalR1_2 + pico_salida_2 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6)
				if CarSalR5_2 > 1800:
					cartones_r5_2.config(text=CarSalR5_2 - 1800)
				else:
					cartones_r5_2.config(text=CarSalR5_2)

			#----Rango 6-----

			if int(numero_series_rango6["text"]) == 0 :
				cartones_r6_2.config(text=0)
			else:
				CarSalR6_2 = CarSalR1_2 + pico_salida_2 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6)
				if CarSalR6_2 > 1800:
					cartones_r6_2.config(text=CarSalR6_2 - 1800)
				else:
					cartones_r6_2.config(text=CarSalR6_2)

			#----Rango 7-----

			if int(numero_series_rango7["text"]) == 0 :
				cartones_r7_2.config(text=0)
			else:
				CarSalR7_2 = CarSalR1_2 + pico_salida_2 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6) + (int(numero_series_rango6["text"]) * 6)
				if CarSalR7_2 > 1800:
					cartones_r7_2.config(text=CarSalR7_2 - 1800)
				else:
					cartones_r7_2.config(text=CarSalR7_2)

			#----Rango 8-----

			if int(numero_series_rango8["text"]) == 0 :
				cartones_r8_2.config(text=0)
			else:
				CarSalR8_2 = CarSalR1_2 + pico_salida_2 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6) + (int(numero_series_rango6["text"]) * 6) + (int(numero_series_rango7["text"]) * 6)
				if CarSalR8_2 > 1800:
					cartones_r8_2.config(text=CarSalR8_2 - 1800)
				else:
					cartones_r8_2.config(text=CarSalR8_2)

			#----Rango 9-----

			if int(numero_series_rango9["text"]) == 0 :
				cartones_r9_2.config(text=0)
			else:
				CarSalR9_2 = CarSalR1_2 + pico_salida_2 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6) + (int(numero_series_rango6["text"]) * 6) + (int(numero_series_rango7["text"]) * 6) + (int(numero_series_rango8["text"]) * 6)
				if CarSalR9_2 > 1800:
					cartones_r9_2.config(text=CarSalR9_2 - 1800)

				else:
					cartones_r9_2.config(text=CarSalR9_2)

			#----Rango cierre-----

			CarSalCie_2 = CarSalR1_2 + pico_salida_2 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6) + (int(numero_series_rango6["text"]) * 6) + (int(numero_series_rango7["text"]) * 6) + (int(numero_series_rango8["text"]) * 6) + (int(numero_series_rango9["text"]) * 6)
			if CarSalCie_2 > 1800:
				cartones_cierre_2.config(text=CarSalCie_2 - 1800)

			else:
				cartones_cierre_2.config(text=CarSalCie_2)
	except:
		pass

def CartonSalida_2_proxima():
	pico_salida_2 = pico_salid_2()

	#cambiaColor()	

	try:
		if SalidaEntry_2.get() == "":
			cartones_r2_2_proxima.config(text=0)
			cartones_r3_2_proxima.config(text=0)
			cartones_r4_2_proxima.config(text=0)
			cartones_r5_2_proxima.config(text=0)
			cartones_r6_2_proxima.config(text=0)
			cartones_r7_2_proxima.config(text=0)
			cartones_r8_2_proxima.config(text=0)
			cartones_r9_2_proxima.config(text=0)
			cartones_cierre_2_proxima.config(text=0)
		else:
			CarSalR1 = SalidaEntry_2.get()
			CarSalR1_2 = int(CarSalR1)
			pico_r1_2.config(text=pico_salida_2)

			#----Rango 2-----

			if int(numero_series2["text"]) == 0 :
				cartones_r2_2_proxima.config(text=0)
			else:
				CarSalR2 = CarSalR1_2 + pico_salida_2 + (int(numero_series1["text"]) * 6)
				if CarSalR2 > 1800:
					cartones_r2_2_proxima.config(text=CarSalR2 - 1800)
				else:
					cartones_r2_2_proxima.config(text=CarSalR2)
				
			#----Rango 3-----

			if int(numero_series3["text"]) == 0 :
				cartones_r3_2_proxima.config(text=0)
			else:
				CarSalR3 = CarSalR1_2 + pico_salida_2 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6)
				if CarSalR3 > 1800:
					cartones_r3_2_proxima.config(text=CarSalR3 - 1800)
				else:
					cartones_r3_2_proxima.config(text=CarSalR3)

			#----Rango 4-----

			if int(numero_series4["text"]) == 0 :
				cartones_r4_2_proxima.config(text=0)
			else:
				CarSalR4 = CarSalR1_2 + pico_salida_2 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6)
				if CarSalR4 > 1800:
					cartones_r4_2_proxima.config(text=CarSalR4 - 1800)
				else:
					cartones_r4_2_proxima.config(text=CarSalR4)

			#----Rango 5-----

			if int(numero_series5["text"]) == 0 :
				cartones_r5_2_proxima.config(text=0)
			else:
				CarSalR5 = CarSalR1_2 + pico_salida_2 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6)
				if CarSalR5 > 1800:
					cartones_r5_2_proxima.config(text=CarSalR5 - 1800)
				else:
					cartones_r5_2_proxima.config(text=CarSalR5)

			#----Rango 6-----

			if int(numero_series6["text"]) == 0 :
				cartones_r6_2_proxima.config(text=0)
			else:
				CarSalR6 = CarSalR1_2 + pico_salida_2 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6) + (int(numero_series5["text"]) * 6)
				if CarSalR6 > 1800:
					cartones_r6_2_proxima.config(text=CarSalR6 - 1800)
				else:
					cartones_r6_2_proxima.config(text=CarSalR6)

			#----Rango 7-----

			if int(numero_series7["text"]) == 0 :
				cartones_r7_2_proxima.config(text=0)
			else:
				CarSalR7 = CarSalR1_2 + pico_salida_2 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6) + (int(numero_series5["text"]) * 6) + (int(numero_series6["text"]) * 6)
				if CarSalR7 > 1800:
					cartones_r7_2_proxima.config(text=CarSalR7 - 1800)
				else:
					cartones_r7_2_proxima.config(text=CarSalR7)

			#----Rango 8-----

			if int(numero_series8["text"]) == 0 :
				cartones_r8_2_proxima.config(text=0)
			else:
				CarSalR8 = CarSalR1_2 + pico_salida_2 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6) + (int(numero_series5["text"]) * 6) + (int(numero_series6["text"]) * 6) + (int(numero_series7["text"]) * 6)
				if CarSalR8 > 1800:
					cartones_r8_2_proxima.config(text=CarSalR8 - 1800)
				else:
					cartones_r8_2_proxima.config(text=CarSalR8)

			#----Rango 9-----

			if int(numero_series9["text"]) == 0 :
				cartones_r9_2_proxima.config(text=0)
			else:
				CarSalR9 = CarSalR1_2 + pico_salida_2 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6) + (int(numero_series5["text"]) * 6) + (int(numero_series6["text"]) * 6) + (int(numero_series7["text"]) * 6) + (int(numero_series8["text"]) * 6)
				if CarSalR9 > 1800:
					cartones_r9_2_proxima.config(text=CarSalR9 - 1800)
				else:
					cartones_r9_2_proxima.config(text=CarSalR9)

			#----Rango cierre-----

			CarSalCie = int(CarSalR1_2) + pico_salida_2 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6) + (int(numero_series5["text"]) * 6) + (int(numero_series6["text"]) * 6) + (int(numero_series7["text"]) * 6) + (int(numero_series8["text"]) * 6) + (int(numero_series9["text"]) * 6)
			if CarSalCie > 1800:
				cartones_cierre_2_proxima.config(text=CarSalCie - 1800)
			else:
				cartones_cierre_2_proxima.config(text=CarSalCie)
	except:
		pass

def CartonSalida_3():
	pico_salida_3 = pico_salid_3()
	try:
		if SalidaEntry_3.get() == "":
			pass
		else:
			CarSalR1 = SalidaEntry_3.get()
			CarSalR1_3 = int(CarSalR1)
			pico_r1_3.config(text=pico_salida_3)

			#----Rango 2-----

			if int(numero_series_rango2["text"]) == 0 :
				cartones_r2_3.config(text=0)
			else:
				CarSalR2_3 = CarSalR1_3 + pico_salida_3 + (int(numero_series_rango1["text"]) * 6) #
				if CarSalR2_3 > 1800:
					cartones_r2_3.config(text=CarSalR2_3 - 1800)
				else:
					cartones_r2_3.config(text=CarSalR2_3)
				
			#----Rango 3-----

			if int(numero_series_rango3["text"]) == 0 :
				cartones_r3_3.config(text=0)
			else:
				CarSalR3_3 = CarSalR1_3 + pico_salida_3 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6)
				if CarSalR3_3 > 1800:
					cartones_r3_3.config(text=CarSalR3_3 - 1800)
				else:
					cartones_r3_3.config(text=CarSalR3_3)

			#----Rango 4-----

			if int(numero_series_rango4["text"]) == 0 :
				cartones_r4_3.config(text=0)
			else:
				CarSalR4_3 = CarSalR1_3 + pico_salida_3 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6)
				if CarSalR4_3 > 1800:
					cartones_r4_3.config(text=CarSalR4_3 - 1800)
				else:
					cartones_r4_3.config(text=CarSalR4_3)

			#----Rango 5-----

			if int(numero_series_rango5["text"]) == 0 :
				cartones_r5_3.config(text=0)
			else:
				CarSalR5_3 = CarSalR1_3 + pico_salida_3 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6)
				if CarSalR5_3 > 1800:
					cartones_r5_3.config(text=CarSalR5_3 - 1800)
				else:
					cartones_r5_3.config(text=CarSalR5_3)

			#----Rango 6-----

			if int(numero_series_rango6["text"]) == 0 :
				cartones_r6_3.config(text=0)
			else:
				CarSalR6_3 = CarSalR1_3 + pico_salida_3 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6)
				if CarSalR6_3 > 1800:
					cartones_r6_3.config(text=CarSalR6_3 - 1800)
				else:
					cartones_r6_3.config(text=CarSalR6_3)

			#----Rango 7-----

			if int(numero_series_rango7["text"]) == 0 :
				cartones_r7_3.config(text=0)
			else:
				CarSalR7_3 = CarSalR1_3 + pico_salida_3 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6) + (int(numero_series_rango6["text"]) * 6)
				if CarSalR7_3 > 1800:
					cartones_r7_3.config(text=CarSalR7_3 - 1800)
				else:
					cartones_r7_3.config(text=CarSalR7_3)

			#----Rango 8-----

			if int(numero_series_rango8["text"]) == 0 :
				cartones_r8_3.config(text=0)
			else:
				CarSalR8_3 = CarSalR1_3 + pico_salida_3 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6) + (int(numero_series_rango6["text"]) * 6) + (int(numero_series_rango7["text"]) * 6)
				if CarSalR8_3 > 1800:
					cartones_r8_3.config(text=CarSalR8_3 - 1800)
				else:
					cartones_r8_3.config(text=CarSalR8_3)

			#----Rango 9-----

			if int(numero_series_rango9["text"]) == 0 :
				cartones_r9_3.config(text=0)
			else:
				CarSalR9_3 = CarSalR1_3 + pico_salida_3 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6) + (int(numero_series_rango6["text"]) * 6) + (int(numero_series_rango7["text"]) * 6) + (int(numero_series_rango8["text"]) * 6)
				if CarSalR9_3 > 1800:
					cartones_r9_3.config(text=CarSalR9_3 - 1800)
				else:
					cartones_r9_3.config(text=CarSalR9_3)

			#----Rango cierre-----

			CarSalCie_3 = CarSalR1_3 + pico_salida_3 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6) + (int(numero_series_rango6["text"]) * 6) + (int(numero_series_rango7["text"]) * 6) + (int(numero_series_rango8["text"]) * 6) + (int(numero_series_rango9["text"]) * 6)
				
			if CarSalCie_3 > 1800:
				cartones_cierre_3.config(text=CarSalCie_3 - 1800)
			else:
				cartones_cierre_3.config(text=CarSalCie_3)
	except:
		pass

def CartonSalida_3_proxima():
	pico_salida_3 = pico_salid_3()
	try:
		if SalidaEntry_3.get() == "":
			cartones_r2_3_proxima.config(text=0)
			cartones_r3_3_proxima.config(text=0)
			cartones_r4_3_proxima.config(text=0)
			cartones_r5_3_proxima.config(text=0)
			cartones_r6_3_proxima.config(text=0)
			cartones_r7_3_proxima.config(text=0)
			cartones_r8_3_proxima.config(text=0)
			cartones_r9_3_proxima.config(text=0)
			cartones_cierre_3_proxima.config(text=0)
		else:
			CarSalR1 = SalidaEntry_3.get()
			CarSalR1_3 = int(CarSalR1)
			pico_r1_3.config(text=pico_salida_3)

			#----Rango 2-----

			if int(numero_series2["text"]) == 0 :
				cartones_r2_3_proxima.config(text=0)
			else:
				CarSalR2 = CarSalR1_3 + pico_salida_3 + (int(numero_series1["text"]) * 6)
				if CarSalR2 > 1800:
					cartones_r2_3_proxima.config(text=CarSalR2 - 1800)
				else:
					cartones_r2_3_proxima.config(text=CarSalR2)
				
			#----Rango 3-----

			if int(numero_series3["text"]) == 0 :
				cartones_r3_3_proxima.config(text=0)
			else:
				CarSalR3 = CarSalR1_3 + pico_salida_3 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6)
				if CarSalR3 > 1800:
					cartones_r3_3_proxima.config(text=CarSalR3 - 1800)
				else:
					cartones_r3_3_proxima.config(text=CarSalR3)

			#----Rango 4-----

			if int(numero_series4["text"]) == 0 :
				cartones_r4_3_proxima.config(text=0)
			else:
				CarSalR4 = CarSalR1_3 + pico_salida_3 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6)
				if CarSalR4 > 1800:
					cartones_r4_3_proxima.config(text=CarSalR4 - 1800)
				else:
					cartones_r4_3_proxima.config(text=CarSalR4)

			#----Rango 5-----

			if int(numero_series5["text"]) == 0 :
				cartones_r5_3_proxima.config(text=0)
			else:
				CarSalR5 = CarSalR1_3 + pico_salida_3 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6)
				if CarSalR5 > 1800:
					cartones_r5_3_proxima.config(text=CarSalR5 - 1800)
				else:
					cartones_r5_3_proxima.config(text=CarSalR5)

			#----Rango 6-----

			if int(numero_series6["text"]) == 0 :
				cartones_r6_3_proxima.config(text=0)
			else:
				CarSalR6 = CarSalR1_3 + pico_salida_3 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6) + (int(numero_series5["text"]) * 6)
				if CarSalR6 > 1800:
					cartones_r6_3_proxima.config(text=CarSalR6 - 1800)
				else:
					cartones_r6_3_proxima.config(text=CarSalR6)

			#----Rango 7-----

			if int(numero_series7["text"]) == 0 :
				cartones_r7_3_proxima.config(text=0)
			else:
				CarSalR7 = CarSalR1_3 + pico_salida_3 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6) + (int(numero_series5["text"]) * 6) + (int(numero_series6["text"]) * 6)
				if CarSalR7 > 1800:
					cartones_r7_3_proxima.config(text=CarSalR7 - 1800)
				else:
					cartones_r7_3_proxima.config(text=CarSalR7)

			#----Rango 8-----

			if int(numero_series8["text"]) == 0 :
				cartones_r8_3_proxima.config(text=0)
			else:
				CarSalR8 = CarSalR1_3 + pico_salida_3 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6) + (int(numero_series5["text"]) * 6) + (int(numero_series6["text"]) * 6) + (int(numero_series7["text"]) * 6)
				if CarSalR8 > 1800:
					cartones_r8_3_proxima.config(text=CarSalR8 - 1800)
				else:
					cartones_r8_3_proxima.config(text=CarSalR8)

			#----Rango 9-----

			if int(numero_series9["text"]) == 0 :
				cartones_r9_3_proxima.config(text=0)
			else:
				CarSalR9 = CarSalR1_3 + pico_salida_3 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6) + (int(numero_series5["text"]) * 6) + (int(numero_series6["text"]) * 6) + (int(numero_series7["text"]) * 6) + (int(numero_series8["text"]) * 6)
				if CarSalR9 > 1800:
					cartones_r9_3_proxima.config(text=CarSalR9 - 1800)
				else:
					cartones_r9_3_proxima.config(text=CarSalR9)

			#----Rango cierre-----

			CarSalCie = int(CarSalR1_3) + pico_salida_3 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6) + (int(numero_series5["text"]) * 6) + (int(numero_series6["text"]) * 6) + (int(numero_series7["text"]) * 6) + (int(numero_series8["text"]) * 6) + (int(numero_series9["text"]) * 6)
			if CarSalCie > 1800:
				cartones_cierre_3_proxima.config(text=CarSalCie - 1800)
			else:
				cartones_cierre_3_proxima.config(text=CarSalCie)
	except:
		pass

def CartonSalida_6():
	pico_salida_6 = pico_salid_6()

	try:
		if SalidaEntry_6.get() == "":
			pass

		else:
			CarSalR1 = SalidaEntry_6.get()
			CarSalR1_6 = int(CarSalR1)
			pico_r1_6.config(text=pico_salida_6)

			#----Rango 2-----

			if int(numero_series_rango2["text"]) == 0 :
				cartones_r2_6.config(text=0)
			else:
				CarSalR2_6 = CarSalR1_6 + pico_salida_6 + (int(numero_series_rango1["text"]) * 6) #
				if CarSalR2_6 > 1800:
					cartones_r2_6.config(text=CarSalR2_6 - 1800)
				else:
					cartones_r2_6.config(text=CarSalR2_6)
				
			#----Rango 3-----

			if int(numero_series_rango3["text"]) == 0 :
				cartones_r3_6.config(text=0)
			else:
				CarSalR3_6 = CarSalR1_6 + pico_salida_6 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6)
				if CarSalR3_6 > 1800:
					cartones_r3_6.config(text=CarSalR3_6 - 1800)
				else:
					cartones_r3_6.config(text=CarSalR3_6)

			#----Rango 4-----

			if int(numero_series_rango4["text"]) == 0 :
				cartones_r4_6.config(text=0)
			else:
				CarSalR4_6 = CarSalR1_6 + pico_salida_6 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6)
				if CarSalR4_6 > 1800:
					cartones_r4_6.config(text=CarSalR4_6 - 1800)
				else:
					cartones_r4_6.config(text=CarSalR4_6)

			#----Rango 5-----

			if int(numero_series_rango5["text"]) == 0 :
				cartones_r5_6.config(text=0)
			else:
				CarSalR5_6 = CarSalR1_6 + pico_salida_6 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6)
				if CarSalR5_6 > 1800:
					cartones_r5_6.config(text=CarSalR5_6 - 1800)
				else:
					cartones_r5_6.config(text=CarSalR5_6)

			#----Rango 6-----

			if int(numero_series_rango6["text"]) == 0 :
				cartones_r6_6.config(text=0)
			else:
				CarSalR6_6 = CarSalR1_6 + pico_salida_6 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6)
				if CarSalR6_6 > 1800:
					cartones_r6_6.config(text=CarSalR6_6 - 1800)
				else:
					cartones_r6_6.config(text=CarSalR6_6)

			#----Rango 7-----

			if int(numero_series_rango7["text"]) == 0 :
				cartones_r7_6.config(text=0)
			else:
				CarSalR7_6 = CarSalR1_6 + pico_salida_6 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6) + (int(numero_series_rango6["text"]) * 6)
				if CarSalR7_6 > 1800:
					cartones_r7_6.config(text=CarSalR7_6 - 1800)
				else:
					cartones_r7_6.config(text=CarSalR7_6)

			#----Rango 8-----

			if int(numero_series_rango8["text"]) == 0 :
				cartones_r8_6.config(text=0)
			else:
				CarSalR8_6 = CarSalR1_6 + pico_salida_6 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6) + (int(numero_series_rango6["text"]) * 6) + (int(numero_series_rango7["text"]) * 6)
				if CarSalR8_6 > 1800:
					cartones_r8_6.config(text=CarSalR8_6 - 1800)
				else:
					cartones_r8_6.config(text=CarSalR8_6)

			#----Rango 9-----

			if int(numero_series_rango9["text"]) == 0 :
				cartones_r9_6.config(text=0)
			else:
				CarSalR9_6 = CarSalR1_6 + pico_salida_6 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6) + (int(numero_series_rango6["text"]) * 6) + (int(numero_series_rango7["text"]) * 6) + (int(numero_series_rango8["text"]) * 6)
				if CarSalR9_6 > 1800:
					cartones_r9_6.config(text=CarSalR9_6 - 1800)
				else:
					cartones_r9_6.config(text=CarSalR9_6)

			#----Rango cierre-----

			CarSalCie_6 = CarSalR1_6 + pico_salida_6 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6) + (int(numero_series_rango6["text"]) * 6) + (int(numero_series_rango7["text"]) * 6) + (int(numero_series_rango8["text"]) * 6) + (int(numero_series_rango9["text"]) * 6)
				
			if CarSalCie_6 > 1800:
				cartones_cierre_6.config(text=CarSalCie_6 - 1800)
			else:
				cartones_cierre_6.config(text=CarSalCie_6)
	except:
		pass

def CartonSalida_6_proxima():
	pico_salida_6 = pico_salid_6()
	try:
		if SalidaEntry_6.get() == "":
			cartones_r2_6_proxima.config(text=0)
			cartones_r3_6_proxima.config(text=0)
			cartones_r4_6_proxima.config(text=0)
			cartones_r5_6_proxima.config(text=0)
			cartones_r6_6_proxima.config(text=0)
			cartones_r7_6_proxima.config(text=0)
			cartones_r8_6_proxima.config(text=0)
			cartones_r9_6_proxima.config(text=0)
			cartones_cierre_6_proxima.config(text=0)
		else:
			CarSalR1 = int(SalidaEntry_6.get())
			CarSalR1_6 = int(CarSalR1)
			pico_r1_6.config(text=pico_salida_6)

			#----Rango 2-----

			if int(numero_series2["text"]) == 0 :
				cartones_r2_6_proxima.config(text=0)
			else:
				CarSalR2 = CarSalR1_6 + pico_salida_6 + (int(numero_series1["text"]) * 6)
				if CarSalR2 > 1800:
					cartones_r2_6_proxima.config(text=CarSalR2 - 1800)
				else:
					cartones_r2_6_proxima.config(text=CarSalR2)
				
			#----Rango 3-----

			if int(numero_series3["text"]) == 0 :
				cartones_r3_6_proxima.config(text=0)
			else:
				CarSalR3 = CarSalR1_6 + pico_salida_6 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6)
				if CarSalR3 > 1800:
					cartones_r3_6_proxima.config(text=CarSalR3 - 1800)
				else:
					cartones_r3_6_proxima.config(text=CarSalR3)

			#----Rango 4-----

			if int(numero_series4["text"]) == 0 :
				cartones_r4_6_proxima.config(text=0)
			else:
				CarSalR4 = CarSalR1_6 + pico_salida_6 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6)
				if CarSalR4 > 1800:
					cartones_r4_6_proxima.config(text=CarSalR4 - 1800)
				else:
					cartones_r4_6_proxima.config(text=CarSalR4)

			#----Rango 5-----

			if int(numero_series5["text"]) == 0 :
				cartones_r5_6_proxima.config(text=0)
			else:
				CarSalR5 = CarSalR1_6 + pico_salida_6 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6)
				if CarSalR5 > 1800:
					cartones_r5_6_proxima.config(text=CarSalR5 - 1800)
				else:
					cartones_r5_6_proxima.config(text=CarSalR5)

			#----Rango 6-----

			if int(numero_series6["text"]) == 0 :
				cartones_r6_6_proxima.config(text=0)
			else:
				CarSalR6 = CarSalR1_6 + pico_salida_6 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6) + (int(numero_series5["text"]) * 6)
				if CarSalR6 > 1800:
					cartones_r6_6_proxima.config(text=CarSalR6 - 1800)
				else:
					cartones_r6_6_proxima.config(text=CarSalR6)

			#----Rango 7-----

			if int(numero_series7["text"]) == 0 :
				cartones_r7_6_proxima.config(text=0)
			else:
				CarSalR7 = CarSalR1_6 + pico_salida_6 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6) + (int(numero_series5["text"]) * 6) + (int(numero_series6["text"]) * 6)
				if CarSalR7 > 1800:
					cartones_r7_6_proxima.config(text=CarSalR7 - 1800)
				else:
					cartones_r7_6_proxima.config(text=CarSalR7)

			#----Rango 8-----

			if int(numero_series8["text"]) == 0 :
				cartones_r8_6_proxima.config(text=0)
			else:
				CarSalR8 = CarSalR1_6 + pico_salida_6 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6) + (int(numero_series5["text"]) * 6) + (int(numero_series6["text"]) * 6) + (int(numero_series7["text"]) * 6)
				if CarSalR8 > 1800:
					cartones_r8_6_proxima.config(text=CarSalR8 - 1800)
				else:
					cartones_r8_6_proxima.config(text=CarSalR8)

			#----Rango 9-----

			if int(numero_series9["text"]) == 0 :
				cartones_r9_6_proxima.config(text=0)
			else:
				CarSalR9 = CarSalR1_6 + pico_salida_6 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6) + (int(numero_series5["text"]) * 6) + (int(numero_series6["text"]) * 6) + (int(numero_series7["text"]) * 6) + (int(numero_series8["text"]) * 6)
				if CarSalR9 > 1800:
					cartones_r9_6_proxima.config(text=CarSalR9 - 1800)
				else:
					cartones_r9_6_proxima.config(text=CarSalR9)

			#----Rango cierre-----

			CarSalCie = int(CarSalR1_6) + pico_salida_6 + (int(numero_series1["text"]) * 6) + (int(numero_series2["text"]) * 6) + (int(numero_series3["text"]) * 6) + (int(numero_series4["text"]) * 6) + (int(numero_series5["text"]) * 6) + (int(numero_series6["text"]) * 6) + (int(numero_series7["text"]) * 6) + (int(numero_series8["text"]) * 6) + (int(numero_series9["text"]) * 6)
			if CarSalCie > 1800:
				cartones_cierre_6_proxima.config(text=CarSalCie - 1800)
			else:
				cartones_cierre_6_proxima.config(text=CarSalCie)
	except:
		pass

def comprobacion_1():
	fallo = 0
	totalCar = total_cartones_1()
	try:
		series_asignadas = int(numero_series_rango1["text"]) + int(numero_series_rango2["text"]) + int(numero_series_rango3["text"]) + int(numero_series_rango4["text"]) + int(numero_series_rango5["text"]) + int(numero_series_rango6["text"]) + int(numero_series_rango7["text"]) + int(numero_series_rango8["text"]) + int(numero_series_rango9["text"])
		if totalCar < series_asignadas * 6:
			MessageBox.showinfo(message="Series ASIGNADAS superior a cartones a la venta\n corrija el cierre o número de series", title="ATENCION")
			series_cie = 0
			fallo = 1
		return fallo
	except:
		pass

def series_cierre():
	totalCar = total_cartones_1()
	pico_salida = pico_salida_1()
	pico_cierre_fin = pico_cierre()
	series_cie = 0
	prueba = 0
	try:
		series_asignadas = int(series_liquidacionr1["text"]) + int(series_liquidacionr2["text"]) + int(series_liquidacionr3["text"]) + int(series_liquidacionr4["text"]) + int(series_liquidacionr5["text"]) + int(series_liquidacionr6["text"]) + int(series_liquidacionr7["text"]) + int(series_liquidacionr8["text"]) + int(series_liquidacionr9["text"]) 
		if SalidaEntry_1.get() == "" or SalidaEntry_1.get() == "0" or CierreTotal.get() == "" or CierreTotal.get() == "0":
			pass
		else:
			if totalCar - pico_salida >= 6 and totalCar - pico_salida  < 12 :
				series_cie = 0
			else:
				series_cie = round((totalCar - pico_salida - pico_cierre_fin) / 6) - series_asignadas

		if series_cie < 0:#and pico_cierre_fin < 0
			MessageBox.showinfo(message="Número de series asignadas superior a cartones a la venta\n vuelva a introducir el cierre o baje número de series", title="ATENCION")
			#borrar()
			series_cie = 0
			prueba = 1

		if prueba == 1:
			return prueba
		else:
			return series_cie
	except:
		pass

def comprobacion_2():
	fallo = 0
	totalCar_2 = total_cartones_2()
	try:
		series_asignadas_2 = int(numero_series_rango1["text"]) + int(numero_series_rango2["text"]) + int(numero_series_rango3["text"]) + int(numero_series_rango4["text"]) + int(numero_series_rango5["text"]) + int(numero_series_rango6["text"]) + int(numero_series_rango7["text"]) + int(numero_series_rango8["text"]) + int(numero_series_rango9["text"])
		if totalCar_2 < series_asignadas_2 * 6:
			MessageBox.showinfo(message="Series ASIGNADAS superior a cartones a la venta\n corrija el cierre o número de series", title="ATENCION")
			series_cie_2 = 0
			fallo = 1
		return fallo
	except:
		pass

def series_cierre_2():
	totalCar_2 = total_cartones_2()
	pico_salida_2 = pico_salid_2()
	pico_cierre_fin_2 = pico_cierre()
	series_cie_2 = 0
	prueba = 0
	try:
		series_asignadas_2 = int(series_liquidacionr1["text"]) + int(series_liquidacionr2["text"]) + int(series_liquidacionr3["text"]) + int(series_liquidacionr4["text"]) + int(series_liquidacionr5["text"]) + int(series_liquidacionr6["text"]) + int(series_liquidacionr7["text"]) + int(series_liquidacionr8["text"]) + int(series_liquidacionr9["text"]) 
		if SalidaEntry_2.get() == "" or SalidaEntry_2.get() == "0" or CierreTotal.get() == "" or CierreTotal.get() == "0":
			pass
		else:
			if totalCar_2 - pico_salida_2 >= 6 and totalCar_2 - pico_salida_2  < 12 :
				series_cie_2 = 0
			else:
				series_cie_2 = round((totalCar_2 - pico_salida_2 - pico_cierre_fin_2) / 6) - series_asignadas_2

		if series_cie_2 < 0:
			MessageBox.showinfo(message="Número de xxxxx series asignadas superior a cartones a la venta\n vuelva a introducir el cierre o baje número de series", title="ATENCION")
			#borrar()
			series_cie_2 = 0
			prueba = 1

		if prueba == 1:
			return prueba
		else:
			return series_cie_2
	except:
		pass

def comprobacion_3():
	fallo = 0
	totalCar_3 = total_cartones_3()
	try:
		series_asignadas_3 = int(numero_series_rango1["text"]) + int(numero_series_rango2["text"]) + int(numero_series_rango3["text"]) + int(numero_series_rango4["text"]) + int(numero_series_rango5["text"]) + int(numero_series_rango6["text"]) + int(numero_series_rango7["text"]) + int(numero_series_rango8["text"]) + int(numero_series_rango9["text"])
		if totalCar_3 < series_asignadas_3 * 6:
			MessageBox.showinfo(message="Series ASIGNADAS superior a cartones a la venta\n corrija el cierre o número de series", title="ATENCION")
			series_cie_3 = 0
			fallo = 1
		return fallo
	except:
		pass

def series_cierre_3():
	totalCar_3 = total_cartones_3()
	pico_salida_3 = pico_salid_3()
	pico_cierre_fin_3 = pico_cierre()
	series_cie_3 = 0
	prueba = 0
	try:
		series_asignadas_3 = int(series_liquidacionr1["text"]) + int(series_liquidacionr2["text"]) + int(series_liquidacionr3["text"]) + int(series_liquidacionr4["text"]) + int(series_liquidacionr5["text"]) + int(series_liquidacionr6["text"]) + int(series_liquidacionr7["text"]) + int(series_liquidacionr8["text"]) + int(series_liquidacionr9["text"]) 
		if SalidaEntry_3.get() == "" or SalidaEntry_3.get() == "0" or CierreTotal.get() == "" or CierreTotal.get() == "0":
			pass
		else:
			if totalCar_3 - pico_salida_3 >= 6 and totalCar_3 - pico_salida_3  < 12 :
				series_cie_3 = 0
			else:
				series_cie_3 = round((totalCar_3 - pico_salida_3 - pico_cierre_fin_3) / 6) - series_asignadas_3

		if series_cie_3 < 0:
			MessageBox.showinfo(message="Número de series asignadas superior a cartones a la venta\n vuelva a introducir el cierre o baje número de series", title="ATENCION")
			#borrar()
			series_cie_3 = 0
			prueba = 1

		if prueba == 1:
			return prueba
		else:
			return series_cie_3
	except:
		pass

def comprobacion_6():
	fallo = 0
	totalCar_6 = total_cartones_6()
	try:
		series_asignadas_6 = int(numero_series_rango1["text"]) + int(numero_series_rango2["text"]) + int(numero_series_rango3["text"]) + int(numero_series_rango4["text"]) + int(numero_series_rango5["text"]) + int(numero_series_rango6["text"]) + int(numero_series_rango7["text"]) + int(numero_series_rango8["text"]) + int(numero_series_rango9["text"])
		if totalCar_6 < series_asignadas_6 * 6:
			MessageBox.showinfo(message="Series ASIGNADAS superior a cartones a la venta\n corrija el cierre o número de series", title="ATENCION")
			series_cie_6 = 0
			fallo = 1
		return fallo
	except:
		pass

def series_cierre_6():
	totalCar_6 = total_cartones_6()
	pico_salida_6 = pico_salid_6()
	pico_cierre_fin_6 = pico_cierre()
	series_cie_6 = 0
	prueba = 0
	try:
		series_asignadas_6 = int(series_liquidacionr1["text"]) + int(series_liquidacionr2["text"]) + int(series_liquidacionr3["text"]) + int(series_liquidacionr4["text"]) + int(series_liquidacionr5["text"]) + int(series_liquidacionr6["text"]) + int(series_liquidacionr7["text"]) + int(series_liquidacionr8["text"]) + int(series_liquidacionr9["text"])
		if SalidaEntry_6.get() == "" or SalidaEntry_6.get() == "0" or CierreTotal.get() == "" or CierreTotal.get() == "0":
			pass
		else:
			if totalCar_6 - pico_salida_6 >= 6 and totalCar_6 - pico_salida_6  < 12 :
				series_cie_6 = 0
			else:
				series_cie_6 = round((totalCar_6 - pico_salida_6 - pico_cierre_fin_6) / 6) - series_asignadas_6

		if series_cie_6 < 0:
			MessageBox.showinfo(message="Número de series asignadas superior a cartones a la venta\n vuelva a introducir el cierre o baje numero de series", title="ATENCION")
			#borrar()
			series_cie_6 = 0
			prueba = 1

		if prueba == 1:
			return prueba
		else:
			return series_cie_6
	except:
		pass

def series_total():
	series_cier = series_cierre()
	try:
		series_totales = series_cier + int(series_liquidacionr1["text"]) + int(series_liquidacionr2["text"]) + int(series_liquidacionr3["text"]) + int(series_liquidacionr4["text"]) + int(series_liquidacionr5["text"]) + int(series_liquidacionr6["text"]) + int(series_liquidacionr7["text"]) + int(series_liquidacionr8["text"]) + int(series_liquidacionr9["text"]) 
		return series_totales
	except:
		pass
	
def series_total_2():
	series_cier = series_cierre_2()
	try:
		series_totales = series_cier + int(series_liquidacionr1["text"]) + int(series_liquidacionr2["text"]) + int(series_liquidacionr3["text"]) + int(series_liquidacionr4["text"]) + int(series_liquidacionr5["text"]) + int(series_liquidacionr6["text"]) + int(series_liquidacionr7["text"]) + int(series_liquidacionr8["text"]) + int(series_liquidacionr9["text"]) 
		return series_totales
	except:
		pass

def series_total_3():
	series_cier = series_cierre_3()
	try:
		series_totales = series_cier + int(series_liquidacionr1["text"]) + int(series_liquidacionr2["text"]) + int(series_liquidacionr3["text"]) + int(series_liquidacionr4["text"]) + int(series_liquidacionr5["text"]) + int(series_liquidacionr6["text"]) + int(series_liquidacionr7["text"]) + int(series_liquidacionr8["text"]) + int(series_liquidacionr9["text"]) 
		return series_totales
	except:
		pass

def series_total_6():
	series_cier = series_cierre_6()
	try:
		series_totales = series_cier + int(series_liquidacionr1["text"]) + int(series_liquidacionr2["text"]) + int(series_liquidacionr3["text"]) + int(series_liquidacionr4["text"]) + int(series_liquidacionr5["text"]) + int(series_liquidacionr6["text"]) + int(series_liquidacionr7["text"]) + int(series_liquidacionr8["text"]) + int(series_liquidacionr9["text"]) 
		return series_totales
	except:
		pass

# ------------------------cambio color----------------------------------------

def cambiaColor():
	if int(numero_series_rango2["text"]) != 0:
		label_R2.config(text="RANGO 2",fg="green", font=("Times New Roman",20,"bold"))
	else:
		label_R2.config(text="RANGO 2", fg="black", font=("Times New Roman",20,"bold"))

	if int(numero_series_rango3["text"]) != 0:
		label_R3.config(text="RANGO 3",fg="green", font=("Times New Roman",20,"bold"))
	else:
		label_R3.config(text="RANGO 3",fg="black", font=("Times New Roman",20,"bold"))

	if int(numero_series_rango4["text"]) != 0:
		label_R4.config(text="RANGO 4",fg="green", font=("Times New Roman",20,"bold"))
	else:
		label_R4.config(text="RANGO 4",fg="black", font=("Times New Roman",20,"bold"))

	if int(numero_series_rango5["text"]) != 0:
		label_R5.config(text="RANGO 5",fg="green", font=("Times New Roman",20,"bold"))
	else:
		label_R5.config(text="RANGO 5",fg="black", font=("Times New Roman",20,"bold"))

	if int(numero_series_rango6["text"]) != 0:
		label_R6.config(text="RANGO 6",fg="green", font=("Times New Roman",20,"bold"))
	else:
		label_R6.config(text="RANGO 6",fg="black", font=("Times New Roman",20,"bold"))

	if int(numero_series_rango7["text"]) != 0:
		label_R7.config(text="RANGO 7",fg="green", font=("Times New Roman",20,"bold"))
	else:
		label_R7.config(text="RANGO 7",fg="black", font=("Times New Roman",20,"bold"))

	if int(numero_series_rango8["text"]) != 0:
		label_R8.config(text="RANGO 8",fg="green", font=("Times New Roman",20,"bold"))
	else:
		label_R8.config(text="RANGO 8",fg="black", font=("Times New Roman",20,"bold"))

	if int(numero_series_rango9["text"]) != 0:
		label_R9.config(text="RANGO 9",fg="green", font=("Times New Roman",20,"bold"))
	else:
		label_R9.config(text="RANGO 9",fg="black", font=("Times New Roman",20,"bold"))			

	#--------------cambio color zona liquidacion---------------------------

	if carton_salida_liqui2["text"] == 0 or carton_salida_liqui2["text"] == "0":
		label_R2_liquidacion.config(text="RANGO 2",fg="black", font=("Times New Roman",20,"bold"))
	else:
		label_R2_liquidacion.config(text="RANGO 2",fg="green", font=("Times New Roman",20,"bold"))

	if carton_salida_liqui3["text"] == 0 or carton_salida_liqui3["text"] == "0":
		label_R3_liquidacion.config(text="RANGO 3",fg="black", font=("Times New Roman",20,"bold"))
	else:
		label_R3_liquidacion.config(text="RANGO 3",fg="green", font=("Times New Roman",20,"bold"))

	if carton_salida_liqui4["text"] == 0 or carton_salida_liqui4["text"] == "0":
		label_R4_liquidacion.config(text="RANGO 4",fg="black", font=("Times New Roman",20,"bold"))
	else:
		label_R4_liquidacion.config(text="RANGO 4",fg="green", font=("Times New Roman",20,"bold"))

	if carton_salida_liqui5["text"] == 0 or carton_salida_liqui5["text"] == "0":
		label_R5_liquidacion.config(text="RANGO 5",fg="black", font=("Times New Roman",20,"bold"))
	else:
		label_R5_liquidacion.config(text="RANGO 5",fg="green", font=("Times New Roman",20,"bold"))

	if carton_salida_liqui6["text"] == 0 or carton_salida_liqui6["text"] == "0":
		label_R6_liquidacion.config(text="RANGO 6",fg="black", font=("Times New Roman",20,"bold"))
	else:
		label_R6_liquidacion.config(text="RANGO 6",fg="green", font=("Times New Roman",20,"bold"))

	if carton_salida_liqui7["text"] == 0 or carton_salida_liqui7["text"] == "0":
		label_R7_liquidacion.config(text="RANGO 7",fg="black", font=("Times New Roman",20,"bold"))
	else:
		label_R7_liquidacion.config(text=" RANGO 7",fg="green", font=("Times New Roman",20,"bold"))

	if carton_salida_liqui8["text"] == 0 or carton_salida_liqui8["text"] == "0":
		label_R8_liquidacion.config(text="RANGO 8",fg="black", font=("Times New Roman",20,"bold"))
	else:
		label_R8_liquidacion.config(text="RANGO 8",fg="green", font=("Times New Roman",20,"bold"))

	if carton_salida_liqui9["text"] == 0 or carton_salida_liqui9["text"] == "0":
		label_R9_liquidacion.config(text="RANGO 9",fg="black", font=("Times New Roman",20,"bold"))
	else:
		label_R9_liquidacion.config(text="RANGO 9",fg="green", font=("Times New Roman",20,"bold"))

def atras_liquidacion():
	global series_liquidacion_atras_r1; global series_liquidacion_atras_r2; global series_liquidacion_atras_r3; global series_liquidacion_atras_r4;
	global series_liquidacion_atras_r5; global series_liquidacion_atras_r6; global series_liquidacion_atras_r7; global series_liquidacion_atras_r8;
	global series_liquidacion_atras_r9; global series_liquidacion_atras_cierre; global series_liquidacion_atras_total; global pico_salida_liqui1_atras;
	global pico_cierre_liqui_atras; global carton_salida_liqui1_atras; global carton_salida_liqui2_atras; global carton_salida_liqui3_atras;
	global carton_salida_liqui4_atras; global carton_salida_liqui5_atras; global carton_salida_liqui6_atras; global carton_salida_liqui7_atras;
	global carton_salida_liqui8_atras; global carton_salida_liqui9_atras; global carton_salida_liqui1_cierre_atras; global total_cartones_liquidacion_atras;
	global liquidacion_liqui1_atras; global liquidacion_liqui2_atras; global liquidacion_liqui3_atras; global liquidacion_liqui4_atras;
	global liquidacion_liqui5_atras; global liquidacion_liqui6_atras; global liquidacion_liqui7_atras; global liquidacion_liqui8_atras;
	global liquidacion_liqui9_atras; global liquidacion_liqui_cierre_atras; global liquidacion_liqui_total_atras; global label_liquidacion_atras
	global color_atras_final

	series_liquidacion_atras_r1 = series_liquidacionr1["text"]
	series_liquidacion_atras_r2 = series_liquidacionr2["text"]
	series_liquidacion_atras_r3 = series_liquidacionr3["text"]
	series_liquidacion_atras_r4 = series_liquidacionr4["text"]
	series_liquidacion_atras_r5 = series_liquidacionr5["text"]
	series_liquidacion_atras_r6 = series_liquidacionr6["text"]
	series_liquidacion_atras_r7 = series_liquidacionr7["text"]
	series_liquidacion_atras_r8 = series_liquidacionr8["text"]
	series_liquidacion_atras_r9 = series_liquidacionr9["text"]
	series_liquidacion_atras_cierre = series_liquidacion_cierre["text"]
	series_liquidacion_atras_total = total_series_liqui["text"]
	pico_salida_liqui1_atras = pico_salida_liqui1["text"]
	pico_cierre_liqui_atras = pico_cierre_liqui["text"]
	carton_salida_liqui1_atras = carton_salida_liqui1["text"]
	carton_salida_liqui2_atras = carton_salida_liqui2["text"]
	carton_salida_liqui3_atras = carton_salida_liqui3["text"]
	carton_salida_liqui4_atras = carton_salida_liqui4["text"]
	carton_salida_liqui5_atras = carton_salida_liqui5["text"]
	carton_salida_liqui6_atras = carton_salida_liqui6["text"]
	carton_salida_liqui7_atras = carton_salida_liqui7["text"]
	carton_salida_liqui8_atras = carton_salida_liqui8["text"]
	carton_salida_liqui9_atras = carton_salida_liqui9["text"]
	carton_salida_liqui1_cierre_atras = carton_salida_liqui1_cierre["text"]
	total_cartones_liquidacion_atras = total_cartones_liquidacion["text"]

	liquidacion_liqui1_atras = liquidacion_liqui1["text"]
	liquidacion_liqui2_atras = liquidacion_liqui2["text"]
	liquidacion_liqui3_atras = liquidacion_liqui3["text"]
	liquidacion_liqui4_atras = liquidacion_liqui4["text"]
	liquidacion_liqui5_atras = liquidacion_liqui5["text"]
	liquidacion_liqui6_atras = liquidacion_liqui6["text"]
	liquidacion_liqui7_atras = liquidacion_liqui7["text"]
	liquidacion_liqui8_atras = liquidacion_liqui8["text"]
	liquidacion_liqui9_atras = liquidacion_liqui9["text"]
	liquidacion_liqui_cierre_atras = liquidacion_liqui_cierre["text"]
	liquidacion_liqui_total_atras = liquidacion_liqui_total["text"]

	if color_atras == 1:
		color_atras_final = "blue"
	elif color_atras ==  2:
		color_atras_final = "#8B0000"
	elif color_atras == 3:
		color_atras_final = "#FF1493"
	else:
		color_atras_final = "#2F4F4F"
	
def sube_a_liquidacion():
	global liquida_total; global color_atras; global liquida_cierre

	color_atras = 1
	atras_liquidacion()
	try:
		pico_salida = pico_salida_1()
		pico_cierre_fin = pico_cierre()
		total_cartones = total_cartones_1()
		CarSalR1 = salida.get()

		series_liquidacionr1.config(text=numero_series_rango1["text"],fg ="blue")
		pico_salida_liqui1.config(text=pico_salida,fg ="blue")
		try:
			r1 = numero_series_rango1["text"] * 6 + int(SalidaEntry_1.get()) + pico_salida - 1
			if r1 >= 1801:
				r1 = r1 - 1800
				resultado = int(SalidaEntry_1.get()),"-",r1
				carton_salida_liqui1.config(text=resultado,fg ="blue")
			else:
				resultado = int(SalidaEntry_1.get()),"-",r1
				carton_salida_liqui1.config(text=resultado,fg ="blue")
		except:
			pass

		#-------------------------Liquidacion rango 2------------------------------

		series_liquidacionr2.config(text=numero_series_rango2["text"],fg ="blue")
		try:
			r1 = numero_series_rango2["text"] * 6 + cartones_r2["text"] - 1
			if numero_series_rango2["text"] == 0:
				carton_salida_liqui2.config(text="0",fg ="blue")
			elif r1 >= 1801:
				r1 = numero_series_rango2["text"] * 6 + cartones_r2["text"] - 1801
				resultado = cartones_r2["text"],"-",r1
				carton_salida_liqui2.config(text=resultado,fg ="blue")
			elif r1 <= 1800 and r1 != 0:
				resultado = cartones_r2["text"],"-",r1
				carton_salida_liqui2.config(text=resultado,fg ="blue")
		except:
			pass
			
		#------------------Liquidacion rango 3--------------------------
		
		series_liquidacionr3.config(text=numero_series_rango3["text"],fg ="blue")
		try:
			r1 = numero_series_rango3["text"] * 6 + cartones_r3["text"] - 1
			if numero_series_rango3["text"] == 0:
				carton_salida_liqui3.config(text="0",fg ="blue")
			elif r1 >= 1801:
				r1 = numero_series_rango3["text"] * 6 + cartones_r3["text"] - 1801
				resultado = cartones_r3["text"],"-",r1
				carton_salida_liqui3.config(text=resultado,fg ="blue")
			elif r1 <= 1800 and r1 != 0:
				resultado = cartones_r3["text"],"-",r1
				carton_salida_liqui3.config(text=resultado,fg ="blue")
		except:
			pass
		
		#------------------Liquidacion rango 4--------------------------
		
		series_liquidacionr4.config(text=numero_series_rango4["text"],fg ="blue")
		try:
			r1 = numero_series_rango4["text"] * 6 + cartones_r4["text"] - 1
			if numero_series_rango4["text"] == 0:
				carton_salida_liqui4.config(text="0",fg ="blue")
			elif r1 >= 1801:
				r1 = numero_series_rango4["text"] * 6 + cartones_r4["text"] - 1801
				resultado = cartones_r4["text"],"-",r1
				carton_salida_liqui4.config(text=resultado,fg ="blue")
			elif r1 <= 1800 and r1 != 0:
				resultado = cartones_r4["text"],"-",r1
				carton_salida_liqui4.config(text=resultado,fg ="blue")
		except:
			pass

		#------------------Liquidacion rango 5--------------------------
		
		series_liquidacionr5.config(text=numero_series_rango5["text"],fg ="blue")
		try:
			r1 = numero_series_rango5["text"] * 6 + cartones_r5["text"] - 1
			if numero_series_rango5["text"] == 0:
				carton_salida_liqui5.config(text="0",fg ="blue")
			elif r1 >= 1801:
				r1 = numero_series_rango5["text"] * 6 + cartones_r5["text"] - 1801
				resultado = cartones_r5["text"],"-",r1
				carton_salida_liqui5.config(text=resultado,fg ="blue")
			elif r1 <= 1800 and r1 != 0:
				resultado = cartones_r5["text"],"-",r1
				carton_salida_liqui5.config(text=resultado,fg ="blue")
		except:
			pass    		

		#------------------Liquidacion rango 6--------------------------
		
		series_liquidacionr6.config(text=numero_series_rango6["text"],fg ="blue")
		try:
			r1 = numero_series_rango6["text"] * 6 + cartones_r6["text"] - 1
			if numero_series_rango6["text"] == 0:
				carton_salida_liqui6.config(text="0",fg ="blue")
			elif r1 >= 1801:
				r1 = numero_series_rango6["text"] * 6 + cartones_r6["text"] - 1801
				resultado = cartones_r6["text"],"-",r1
				carton_salida_liqui6.config(text=resultado,fg ="blue")
			elif r1 <= 1800 and r1 != 0:
				resultado = cartones_r6["text"],"-",r1
				carton_salida_liqui6.config(text=resultado,fg ="blue")
		except:
			pass    

		#------------------Liquidacion rango 7--------------------------
		
		series_liquidacionr7.config(text=numero_series_rango7["text"],fg ="blue")
		try:
			r1 = numero_series_rango7["text"] * 6 + cartones_r7["text"] - 1
			if numero_series_rango7["text"] == 0:
				carton_salida_liqui7.config(text="0",fg ="blue")
			elif r1 >= 1801:
				r1 = numero_series_rango7["text"] * 6 + cartones_r7["text"] - 1801
				resultado = cartones_r7["text"],"-",r1
				carton_salida_liqui7.config(text=resultado,fg ="blue")
			elif r1 <= 1800 and r1 != 0:
				resultado = cartones_r7["text"],"-",r1
				carton_salida_liqui7.config(text=resultado,fg ="blue")
		except:
			pass

		#------------------Liquidacion rango 8--------------------------
		
		series_liquidacionr8.config(text=numero_series_rango8["text"],fg ="blue")
		try:
			r1 = numero_series_rango8["text"] * 6 + cartones_r8["text"] - 1
			if numero_series_rango8["text"] == 0:
				carton_salida_liqui8.config(text="0",fg ="blue")
			elif r1 >= 1801:
				r1 = numero_series_rango8["text"] * 6 + cartones_r8["text"] - 1801
				resultado = cartones_r8["text"],"-",r1
				carton_salida_liqui8.config(text=resultado,fg ="blue")
			elif r1 <= 1800 and r1 != 0:
				resultado = cartones_r8["text"],"-",r1
				carton_salida_liqui8.config(text=resultado,fg ="blue")
		except:
			pass

		#------------------Liquidacion rango 9--------------------------
		
		series_liquidacionr9.config(text=numero_series_rango9["text"],fg ="blue")
		try:
			r1 = numero_series_rango9["text"] * 6 + cartones_r9["text"] - 1
			if numero_series_rango9["text"] == 0:
				carton_salida_liqui9.config(text="0",fg ="blue")
			elif r1 >= 1801:
				r1 = numero_series_rango9["text"] * 6 + cartones_r9["text"] - 1801
				resultado = cartones_r9["text"],"-",r1
				carton_salida_liqui9.config(text=resultado,fg ="blue")
			elif r1 <= 1800 and r1 != 0:
				resultado = cartones_r9["text"],"-",r1
				carton_salida_liqui9.config(text=resultado,fg ="blue")
		except:
			pass

		#------------------Liquidacion cierre--------------------------

		total_series_cierre = series_cierre()
		series_liquidacion_cierre.config(text=total_series_cierre,fg ="blue")
		try:
			CarSalCie = CarSalR1 + pico_salida + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6) + (int(numero_series_rango6["text"]) * 6) + (int(numero_series_rango7["text"]) * 6) + (int(numero_series_rango8["text"]) * 6) + (int(numero_series_rango9["text"]) * 6)
			diferencia = CarSalCie - int(cierre.get()) 
			if diferencia == 1:
				carton_salida_liqui1_cierre.config(text= 0, fg ="blue")
				pico_cierre_liqui.config(fg ="blue")
			else:
				if CarSalCie >= 1800:
					resultado= CarSalCie - 1800, "-", cierre.get()
				else: 
					resultado = CarSalCie, "-", cierre.get()
				carton_salida_liqui1_cierre.config(text=resultado, fg ="blue")
				pico_cierre_liqui.config(fg ="blue")
		except:
			pass

		#----------------------Liquidacion Total-----------------------------
		series_totales = series_total()
		try:
			liquida_total = total_cartones * 1.5,"€"
			liquidacion_liqui_total.config(text=liquida_total, fg="#800080")
			total_series_liqui.config(text=series_totales, fg ="blue")
			total_cartones_liquidacion.config(text=total_cartones, fg ="blue")
		except:
			pass

		if int(CierreTotal.get()) == 1800:
			salida.set(1)
			PreparaRectifica()
			CartonSalida_1()
			total_car_1.config(text = 0)
			cierre.set("")
			CierreTotal.focus()
			
		else:
			salida.set(int (cierre.get()) + 1)
			PreparaRectifica()
			CartonSalida_1()
			total_car_1.config(text = 0)
			cierre.set("")
			CierreTotal.focus()

		pico_cierre_liqui.config(text = pico_cierre_fin)
		pico_final.config(text = 0)
		total_car_1.config(text=0)
		total_car_2.config(text=0)
		total_car_3.config(text=0)
		total_car_6.config(text=0)
	except:
		pass

# --------------------- Sube a liquidacion 2----------------------------------

def sube_a_liquidacion_2():
	global liquida_total; global color_atras

	color_atras = 2
	atras_liquidacion()
	try:
		pico_salida_2 = pico_salid_2()
		pico_cierre_fin = pico_cierre()
		total_cartone_2 = total_cartones_2()
		CarSalR1_2 = salida_2.get()
		
		series_liquidacionr1.config(text=numero_series_rango1["text"],fg ="#8B0000")
		pico_salida_liqui1.config(text=pico_salida_2,fg ="#8B0000")
		try:
			r1 = numero_series_rango1["text"] * 6 + int(SalidaEntry_2.get()) + pico_salida_2 - 1
			if r1 >= 1801:
				r1 = r1 - 1800
				resultado = int(SalidaEntry_2.get()),"-",r1
				carton_salida_liqui1.config(text=resultado,fg ="#8B0000")
			else:
				resultado = int(SalidaEntry_2.get()),"-",r1
				carton_salida_liqui1.config(text=resultado,fg ="#8B0000")
		except:
			pass

		#-------------------------Liquidacion rango 2------------------------------

		series_liquidacionr2.config(text=numero_series_rango2["text"],fg ="#8B0000")
		try:
			r1 = numero_series_rango2["text"] * 6 + cartones_r2_2["text"] - 1
			if numero_series_rango2["text"] == 0:
				carton_salida_liqui2.config(text="0",fg ="#8B0000")
			elif r1 >= 1801:
				r1 = numero_series_rango2["text"] * 6 + cartones_r2_2["text"] - 1801
				resultado = cartones_r2_2["text"],"-",r1
				carton_salida_liqui2.config(text=resultado,fg ="#8B0000")
			elif r1 <= 1800 and r1 != 0:
				resultado = cartones_r2_2["text"],"-",r1
				carton_salida_liqui2.config(text=resultado,fg ="#8B0000")
		except:
			pass
			
		#------------------Liquidacion rango 3--------------------------
		
		series_liquidacionr3.config(text=numero_series_rango3["text"],fg ="#8B0000")
		try:
			r1 = numero_series_rango3["text"] * 6 + cartones_r3_2["text"] - 1
			if numero_series_rango3["text"] == 0:
				carton_salida_liqui3.config(text="0",fg ="#8B0000")
			elif r1 >= 1801:
				r1 = numero_series_rango3["text"] * 6 + cartones_r3_2["text"] - 1801
				resultado = cartones_r3_2["text"],"-",r1
				carton_salida_liqui3.config(text=resultado,fg ="#8B0000")
			elif r1 <= 1800 and r1 != 0:
				resultado = cartones_r3_2["text"],"-",r1
				carton_salida_liqui3.config(text=resultado,fg ="#8B0000")
		except:
			pass
		
		#------------------Liquidacion rango 4--------------------------
		
		series_liquidacionr4.config(text=numero_series_rango4["text"],fg ="#8B0000")
		try:
			r1 = numero_series_rango4["text"] * 6 + cartones_r4_2["text"] - 1
			if numero_series_rango4["text"] == 0:
				carton_salida_liqui4.config(text="0",fg ="#8B0000")
			elif r1 >= 1801:
				r1 = numero_series_rango4["text"] * 6 + cartones_r4_2["text"] - 1801
				resultado = cartones_r4_2["text"],"-",r1
				carton_salida_liqui4.config(text=resultado,fg ="#8B0000")
			elif r1 <= 1800 and r1 != 0:
				resultado = cartones_r4_2["text"],"-",r1
				carton_salida_liqui4.config(text=resultado,fg ="#8B0000")
		except:
			pass   		

		#------------------Liquidacion rango 5--------------------------
		
		series_liquidacionr5.config(text=numero_series_rango5["text"],fg ="#8B0000")
		try:
			r1 = numero_series_rango5["text"] * 6 + cartones_r5_2["text"] - 1
			if numero_series_rango5["text"] == 0:
				carton_salida_liqui5.config(text="0",fg ="#8B0000")
			elif r1 >= 1801:
				r1 = numero_series_rango5["text"] * 6 + cartones_r5_2["text"] - 1801
				resultado = cartones_r5_2["text"],"-",r1
				carton_salida_liqui5.config(text=resultado,fg ="#8B0000")
			elif r1 <= 1800 and r1 != 0:
				resultado = cartones_r5_2["text"],"-",r1
				carton_salida_liqui5.config(text=resultado,fg ="#8B0000")
		except:
			pass    		

		#------------------Liquidacion rango 6--------------------------
		
		series_liquidacionr6.config(text=numero_series_rango6["text"],fg ="#8B0000")
		try:
			r1 = numero_series_rango6["text"] * 6 + cartones_r6_2["text"] - 1
			if numero_series_rango6["text"] == 0:
				carton_salida_liqui6.config(text="0",fg ="#8B0000")
			elif r1 >= 1801:
				r1 = numero_series_rango6["text"] * 6 + cartones_r6_2["text"] - 1801
				resultado = cartones_r6_2["text"],"-",r1
				carton_salida_liqui6.config(text=resultado,fg ="#8B0000")
			elif r1 <= 1800 and r1 != 0:
				resultado = cartones_r6_2["text"],"-",r1
				carton_salida_liqui6.config(text=resultado,fg ="#8B0000")
		except:
			pass    

		#------------------Liquidacion rango 7--------------------------
		
		series_liquidacionr7.config(text=numero_series_rango7["text"],fg ="#8B0000")
		try:
			r1 = numero_series_rango7["text"] * 6 + cartones_r7_2["text"] - 1
			if numero_series_rango7["text"] == 0:
				carton_salida_liqui7.config(text="0",fg ="#8B0000")
			elif r1 >= 1801:
				r1 = numero_series_rango7["text"] * 6 + cartones_r7_2["#8B0000"] - 1801
				resultado = cartones_r7_2["text"],"-",r1
				carton_salida_liqui7.config(text=resultado,fg ="#8B0000")
			elif r1 <= 1800 and r1 != 0:
				resultado = cartones_r7_2["text"],"-",r1
				carton_salida_liqui7.config(text=resultado,fg ="#8B0000")
		except:
			pass

		#------------------Liquidacion rango 8--------------------------
		
		series_liquidacionr8.config(text=numero_series_rango8["text"],fg ="#8B0000")
		try:
			r1 = numero_series_rango8["text"] * 6 + cartones_r8_2["text"] - 1
			if numero_series_rango8["text"] == 0:
				carton_salida_liqui8.config(text="0",fg ="#8B0000")
			elif r1 >= 1801:
				r1 = numero_series_rango8["text"] * 6 + cartones_r8_2["text"] - 1801
				resultado = cartones_r8_2["text"],"-",r1
				carton_salida_liqui8.config(text=resultado,fg ="#8B0000")
			elif r1 <= 1800 and r1 != 0:
				resultado = cartones_r8_2["text"],"-",r1
				carton_salida_liqui8.config(text=resultado,fg ="#8B0000")
		except:
			pass

		#------------------Liquidacion rango 9--------------------------
		
		series_liquidacionr9.config(text=numero_series_rango9["text"],fg ="#8B0000")
		try:
			r1 = numero_series_rango9["text"] * 6 + cartones_r9_2["text"] - 1
			if numero_series_rango9["text"] == 0:
				carton_salida_liqui9.config(text="0",fg ="#8B0000")
			elif r1 >= 1801:
				r1 = numero_series_rango9["text"] * 6 + cartones_r9_2["text"] - 1801
				resultado = cartones_r9_2["text"],"-",r1
				carton_salida_liqui9.config(text=resultado,fg ="#8B0000")
			elif r1 <= 1800 and r1 != 0:
				resultado = cartones_r9_2["text"],"-",r1
				carton_salida_liqui9.config(text=resultado,fg ="#8B0000")
		except:
			pass

		#------------------Liquidacion cierre--------------------------

		series_cierr_2 = series_cierre_2()
		series_liquidacion_cierre.config(text=series_cierr_2, fg ="#8B0000")
		try:
			CarSalCie_2 = CarSalR1_2 + pico_salida_2 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6) + (int(numero_series_rango6["text"]) * 6) + (int(numero_series_rango7["text"]) * 6) + (int(numero_series_rango8["text"]) * 6) + (int(numero_series_rango9["text"]) * 6)
			diferencia = CarSalCie_2 - int(cierre.get()) 
			if diferencia == 1:
				carton_salida_liqui1_cierre.config(text= 0, fg ="#8B0000")
				pico_cierre_liqui.config(fg ="#8B0000")
			else:
				if CarSalCie_2 >= 1800:
					resultado = CarSalCie_2 - 1800, "-", cierre.get()
				else:
					resultado = CarSalCie_2, "-", cierre.get()
				carton_salida_liqui1_cierre.config(text=resultado, fg ="#8B0000")
				pico_cierre_liqui.config(fg ="#8B0000")
		except:
			pass

		#----------------------Liquidación Total-----------------------------
		series_totales_2 = series_total_2()
		try:
			liquida_total = total_cartone_2 * 2,"€"
			liquidacion_liqui_total.config(text=liquida_total)
			total_series_liqui.config(text=series_totales_2, fg ="#8B0000")
			total_cartones_liquidacion.config(text=total_cartone_2, fg ="#8B0000")
		except:
			pass

		if int(CierreTotal.get()) == 1800:
			salida_2.set(1)
			PreparaRectifica()
			CartonSalida_2()
			total_car_2.config(text = 0)
			cierre.set("")
			CierreTotal.focus()
		else:
			salida_2.set(int (cierre.get()) + 1)
			PreparaRectifica()
			CartonSalida_2()
			total_car_2.config(text = 0)
			cierre.set("")
			CierreTotal.focus()

		pico_cierre_liqui.config(text = pico_cierre_fin)
		pico_final.config(text = 0)
		total_car_1.config(text=0)
		total_car_2.config(text=0)
		total_car_3.config(text=0)
		total_car_6.config(text=0)
	except:
		pass

# --------------------------Sube a liquidación 3------------------------------

def sube_a_liquidacion_3():
	global liquida_total; global color_atras

	color_atras = 3
	atras_liquidacion()
	try:
		pico_salida_3 = pico_salid_3()
		pico_cierre_fin = pico_cierre()
		total_cartone_3 = total_cartones_3()
		CarSalR1_3 = salida_3.get()

		series_liquidacionr1.config(text=numero_series_rango1["text"],fg ="#FF1493")
		pico_salida_liqui1.config(text=pico_salida_3,fg ="#FF1493")
		r1 = numero_series_rango1["text"] * 6 + int(SalidaEntry_3.get()) + pico_salida_3 - 1
		if r1 >= 1801:
			r1 = r1 - 1800
			resultado = int(SalidaEntry_3.get()),"-",r1
			carton_salida_liqui1.config(text=resultado,fg ="#FF1493")
		else:
			resultado = int(SalidaEntry_3.get()),"-",r1
			carton_salida_liqui1.config(text=resultado,fg ="#FF1493")

		#-------------------------Liquidacion rango 2------------------------------

		series_liquidacionr2.config(text=numero_series_rango2["text"],fg ="#FF1493")
		r1 = numero_series_rango2["text"] * 6 + cartones_r2_3["text"] - 1
		if numero_series_rango2["text"] == 0:
			carton_salida_liqui2.config(text="0",fg ="#FF1493")
		elif r1 >= 1801:
			r1 = numero_series_rango2["text"] * 6 + cartones_r2_3["text"] - 1801
			resultado = cartones_r2_3["text"],"-",r1
			carton_salida_liqui2.config(text=resultado,fg ="#FF1493")
		elif r1 <= 1800 and r1 != 0:
			resultado = cartones_r2_3["text"],"-",r1
			carton_salida_liqui2.config(text=resultado,fg ="#FF1493")
			
		#------------------Liquidacion rango 3--------------------------
		
		series_liquidacionr3.config(text=numero_series_rango3["text"],fg ="#FF1493")
		r1 = numero_series_rango3["text"] * 6 + cartones_r3_3["text"] - 1
		if numero_series_rango3["text"] == 0:
			carton_salida_liqui3.config(text="0",fg ="#FF1493")
		elif r1 >= 1801:
			r1 = numero_series_rango3["text"] * 6 + cartones_r3_3["text"] - 1801
			resultado = cartones_r3_3["text"],"-",r1
			carton_salida_liqui3.config(text=resultado,fg ="#FF1493")
		elif r1 <= 1800 and r1 != 0:
			resultado = cartones_r3_3["text"],"-",r1
			carton_salida_liqui3.config(text=resultado,fg ="#FF1493")
		
		#------------------Liquidacion rango 4--------------------------
		
		series_liquidacionr4.config(text=numero_series_rango4["text"],fg ="#FF1493")
		r1 = numero_series_rango4["text"] * 6 + cartones_r4_3["text"] - 1
		if numero_series_rango4["text"] == 0:
			carton_salida_liqui4.config(text="0",fg ="#FF1493")
		elif r1 >= 1801:
			r1 = numero_series_rango4["text"] * 6 + cartones_r4_3["text"] - 1801
			resultado = cartones_r4_3["text"],"-",r1
			carton_salida_liqui4.config(text=resultado,fg ="#FF1493")
		elif r1 <= 1800 and r1 != 0:
			resultado = cartones_r4_3["text"],"-",r1
			carton_salida_liqui4.config(text=resultado,fg ="#FF1493")   		

		#------------------Liquidacion rango 5--------------------------
		
		series_liquidacionr5.config(text=numero_series_rango5["text"],fg ="#FF1493")
		r1 = numero_series_rango5["text"] * 6 + cartones_r5_3["text"] - 1
		if numero_series_rango5["text"] == 0:
			carton_salida_liqui5.config(text="0",fg ="#FF1493")
		elif r1 >= 1801:
			r1 = numero_series_rango5["text"] * 6 + cartones_r5_3["text"] - 1801
			resultado = cartones_r5_3["text"],"-",r1
			carton_salida_liqui5.config(text=resultado,fg ="#FF1493")
		elif r1 <= 1800 and r1 != 0:
			resultado = cartones_r5_3["text"],"-",r1
			carton_salida_liqui5.config(text=resultado,fg ="#FF1493")    		

		#------------------Liquidacion rango 6--------------------------
		
		series_liquidacionr6.config(text=numero_series_rango6["text"],fg ="#FF1493")
		r1 = numero_series_rango6["text"] * 6 + cartones_r6_3["text"] - 1
		if numero_series_rango6["text"] == 0:
			carton_salida_liqui6.config(text="0",fg ="#FF1493")
		elif r1 >= 1801:
			r1 = numero_series_rango6["text"] * 6 + cartones_r6_3["text"] - 1801
			resultado = cartones_r6_3["text"],"-",r1
			carton_salida_liqui6.config(text=resultado,fg ="#FF1493")
		elif r1 <= 1800 and r1 != 0:
			resultado = cartones_r6_3["text"],"-",r1
			carton_salida_liqui6.config(text=resultado,fg ="#FF1493")    

		#------------------Liquidacion rango 7--------------------------
		
		series_liquidacionr7.config(text=numero_series_rango7["text"],fg ="#FF1493")
		r1 = numero_series_rango7["text"] * 6 + cartones_r7_3["text"] - 1
		if numero_series_rango7["text"] == 0:
			carton_salida_liqui7.config(text="0",fg ="#FF1493")
		elif r1 >= 1801:
			r1 = numero_series_rango7["text"] * 6 + cartones_r7_3["#FF1493"] - 1801
			resultado = cartones_r7_3["text"],"-",r1
			carton_salida_liqui7.config(text=resultado,fg ="#FF1493")
		elif r1 <= 1800 and r1 != 0:
			resultado = cartones_r7_3["text"],"-",r1
			carton_salida_liqui7.config(text=resultado,fg ="#FF1493")

		#------------------Liquidacion rango 8--------------------------
		
		series_liquidacionr8.config(text=numero_series_rango8["text"],fg ="#FF1493")
		r1 = numero_series_rango8["text"] * 6 + cartones_r8_3["text"] - 1
		if numero_series_rango8["text"] == 0:
			carton_salida_liqui8.config(text="0",fg ="#FF1493")
		elif r1 >= 1801:
			r1 = numero_series_rango8["text"] * 6 + cartones_r8_3["text"] - 1801
			resultado = cartones_r8_3["text"],"-",r1
			carton_salida_liqui8.config(text=resultado,fg ="#FF1493")
		elif r1 <= 1800 and r1 != 0:
			resultado = cartones_r8_3["text"],"-",r1
			carton_salida_liqui8.config(text=resultado,fg ="#FF1493")

		#------------------Liquidacion rango 9--------------------------
		
		series_liquidacionr9.config(text=numero_series_rango9["text"],fg ="#FF1493")
		r1 = numero_series_rango9["text"] * 6 + cartones_r9_3["text"] - 1
		if numero_series_rango9["text"] == 0:
			carton_salida_liqui9.config(text="0",fg ="#FF1493")
		elif r1 >= 1801:
			r1 = numero_series_rango9["text"] * 6 + cartones_r9_3["text"] - 1801
			resultado = cartones_r9_3["text"],"-",r1
			carton_salida_liqui9.config(text=resultado,fg ="#FF1493")
		elif r1 <= 1800 and r1 != 0:
			resultado = cartones_r9_3["text"],"-",r1
			carton_salida_liqui9.config(text=resultado,fg ="#FF1493")

		#------------------Liquidacion cierre--------------------------

		series_cierr_3 = series_cierre_3()
		series_liquidacion_cierre.config(text=series_cierr_3, fg ="#FF1493")
		try:
			CarSalCie_3 = CarSalR1_3 + pico_salida_3 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6) + (int(numero_series_rango6["text"]) * 6) + (int(numero_series_rango7["text"]) * 6) + (int(numero_series_rango8["text"]) * 6) + (int(numero_series_rango9["text"]) * 6)
			diferencia = CarSalCie_3 - int(cierre.get()) 
			if diferencia == 1:
				carton_salida_liqui1_cierre.config(text= 0, fg ="#FF1493")
				pico_cierre_liqui.config(fg ="#FF1493")
			else:
				if CarSalCie_3 >= 1800:
					resultado = CarSalCie_3 - 1800, "-", cierre.get()
				else: 
					resultado = CarSalCie_3, "-", cierre.get()
				carton_salida_liqui1_cierre.config(text=resultado, fg ="#FF1493")
				pico_cierre_liqui.config(fg ="#FF1493")
		except:
			pass

		#----------------------Liquidación Total-----------------------------
		series_totales_3 = series_total_3()
		liquida_total = total_cartone_3 * 3,"€"
		liquidacion_liqui_total.config(text=liquida_total)
		total_series_liqui.config(text=series_totales_3, fg ="#FF1493")
		total_cartones_liquidacion.config(text=total_cartone_3, fg ="#FF1493")

		if int(CierreTotal.get()) == 1800:
			salida_3.set(1)
			PreparaRectifica()
			CartonSalida_3()
			total_car_3.config(text = 0)
			cierre.set("")
			CierreTotal.focus()
		else:
			salida_3.set(int (cierre.get()) + 1)
			PreparaRectifica()
			CartonSalida_3()
			total_car_3.config(text = 0)
			cierre.set("")
			CierreTotal.focus()

		pico_cierre_liqui.config(text = pico_cierre_fin)
		pico_final.config(text = 0)
		total_car_1.config(text=0)
		total_car_2.config(text=0)
		total_car_3.config(text=0)
		total_car_6.config(text=0)
	except:
		pass

# ----------------------------Sube a liquidación 6----------------------

def sube_a_liquidacion_6():
	global serie_r1_atras; global serie_r2_atras; global serie_r3_atras; global serie_r4_atras;
	global serie_r5_atras; global serie_r6_atras; global serie_r7_atras; global serie_r8_atras; global serie_r9_atras;
	global liquida_total; global color_atras

	color_atras = 4
	atras_liquidacion()
	try:
		pico_salida_6 = pico_salid_6()
		pico_cierre_fin = pico_cierre()
		total_cartone_6 = total_cartones_6()
		CarSalR1_6 = salida_6.get()
		
		series_liquidacionr1.config(text=numero_series_rango1["text"],fg ="#2F4F4F")
		pico_salida_liqui1.config(text=pico_salida_6,fg ="#2F4F4F")
		r1 = numero_series_rango1["text"] * 6 + int(SalidaEntry_6.get()) + pico_salida_6 - 1
		if r1 >= 1801:
			r1 = r1 - 1800
			resultado = int(SalidaEntry_6.get()),"-",r1
			carton_salida_liqui1.config(text=resultado,fg ="#2F4F4F")
		else:
			resultado = int(SalidaEntry_6.get()),"-",r1
			carton_salida_liqui1.config(text=resultado,fg ="#2F4F4F")

		#-------------------------Liquidacion rango 2------------------------------

		series_liquidacionr2.config(text=numero_series_rango2["text"],fg ="#2F4F4F")
		r1 = numero_series_rango2["text"] * 6 + cartones_r2_6["text"] - 1
		if numero_series_rango2["text"] == 0:
			carton_salida_liqui2.config(text="0",fg ="#2F4F4F")
		elif r1 >= 1801:
			r1 = numero_series_rango2["text"] * 6 + cartones_r2_6["text"] - 1801
			resultado = cartones_r2_6["text"],"-",r1
			carton_salida_liqui2.config(text=resultado,fg ="#2F4F4F")
		elif r1 <= 1800 and r1 != 0:
			resultado = cartones_r2_6["text"],"-",r1
			carton_salida_liqui2.config(text=resultado,fg ="#2F4F4F")
			
		#------------------Liquidacion rango 3--------------------------
		
		series_liquidacionr3.config(text=numero_series_rango3["text"],fg ="#2F4F4F")
		r1 = numero_series_rango3["text"] * 6 + cartones_r3_6["text"] - 1
		if numero_series_rango3["text"] == 0:
			carton_salida_liqui3.config(text="0",fg ="#2F4F4F")
		elif r1 >= 1801:
			r1 = numero_series_rango3["text"] * 6 + cartones_r3_6["text"] - 1801
			resultado = cartones_r3_6["text"],"-",r1
			carton_salida_liqui3.config(text=resultado,fg ="#2F4F4F")
		elif r1 <= 1800 and r1 != 0:
			resultado = cartones_r3_6["text"],"-",r1
			carton_salida_liqui3.config(text=resultado,fg ="#2F4F4F")
		
		#------------------Liquidacion rango 4--------------------------
		
		series_liquidacionr4.config(text=numero_series_rango4["text"],fg ="#2F4F4F")
		r1 = numero_series_rango4["text"] * 6 + cartones_r4_6["text"] - 1
		if numero_series_rango4["text"] == 0:
			carton_salida_liqui4.config(text="0",fg ="#2F4F4F")
		elif r1 >= 1801:
			r1 = numero_series_rango4["text"] * 6 + cartones_r4_6["text"] - 1801
			resultado = cartones_r4_6["text"],"-",r1
			carton_salida_liqui4.config(text=resultado,fg ="#2F4F4F")
		elif r1 <= 1800 and r1 != 0:
			resultado = cartones_r4_6["text"],"-",r1
			carton_salida_liqui4.config(text=resultado,fg ="#2F4F4F")   		

		#------------------Liquidacion rango 5--------------------------
		
		series_liquidacionr5.config(text=numero_series_rango5["text"],fg ="#2F4F4F")
		r1 = numero_series_rango5["text"] * 6 + cartones_r5_6["text"] - 1
		if numero_series_rango5["text"] == 0:
			carton_salida_liqui5.config(text="0",fg ="#2F4F4F")
		elif r1 >= 1801:
			r1 = numero_series_rango5["text"] * 6 + cartones_r5_6["text"] - 1801
			resultado = cartones_r5_6["text"],"-",r1
			carton_salida_liqui5.config(text=resultado,fg ="#2F4F4F")
		elif r1 <= 1800 and r1 != 0:
			resultado = cartones_r5_6["text"],"-",r1
			carton_salida_liqui5.config(text=resultado,fg ="#2F4F4F")    		

		#------------------Liquidacion rango 6--------------------------
		
		series_liquidacionr6.config(text=numero_series_rango6["text"],fg ="#2F4F4F")
		r1 = numero_series_rango6["text"] * 6 + cartones_r6_6["text"] - 1
		if numero_series_rango6["text"] == 0:
			carton_salida_liqui6.config(text="0",fg ="#2F4F4F")
		elif r1 >= 1801:
			r1 = numero_series_rango6["text"] * 6 + cartones_r6_6["text"] - 1801
			resultado = cartones_r6_6["text"],"-",r1
			carton_salida_liqui6.config(text=resultado,fg ="#2F4F4F")
		elif r1 <= 1800 and r1 != 0:
			resultado = cartones_r6_6["text"],"-",r1
			carton_salida_liqui6.config(text=resultado,fg ="#2F4F4F")    

		#------------------Liquidacion rango 7--------------------------
		
		series_liquidacionr7.config(text=numero_series_rango7["text"],fg ="#2F4F4F")
		r1 = numero_series_rango7["text"] * 6 + cartones_r7_6["text"] - 1
		if numero_series_rango7["text"] == 0:
			carton_salida_liqui7.config(text="0",fg ="#2F4F4F")
		elif r1 >= 1801:
			r1 = numero_series_rango7["text"] * 6 + cartones_r7_6["#2F4F4F"] - 1801
			resultado = cartones_r7_6["text"],"-",r1
			carton_salida_liqui7.config(text=resultado,fg ="#2F4F4F")
		elif r1 <= 1800 and r1 != 0:
			resultado = cartones_r7_6["text"],"-",r1
			carton_salida_liqui7.config(text=resultado,fg ="#2F4F4F")

		#------------------Liquidacion rango 8--------------------------
		
		series_liquidacionr8.config(text=numero_series_rango8["text"],fg ="#2F4F4F")
		r1 = numero_series_rango8["text"] * 6 + cartones_r8_6["text"] - 1
		if numero_series_rango8["text"] == 0:
			carton_salida_liqui8.config(text="0",fg ="#2F4F4F")
		elif r1 >= 1801:
			r1 = numero_series_rango8["text"] * 6 + cartones_r8_6["text"] - 1801
			resultado = cartones_r8_6["text"],"-",r1
			carton_salida_liqui8.config(text=resultado,fg ="#2F4F4F")
		elif r1 <= 1800 and r1 != 0:
			resultado = cartones_r8_6["text"],"-",r1
			carton_salida_liqui8.config(text=resultado,fg ="#2F4F4F")

		#------------------Liquidacion rango 9--------------------------
		
		series_liquidacionr9.config(text=numero_series_rango9["text"],fg ="#2F4F4F")
		r1 = numero_series_rango9["text"] * 6 + cartones_r9_6["text"] - 1
		if numero_series_rango9["text"] == 0:
			carton_salida_liqui9.config(text="0",fg ="#2F4F4F")
		elif r1 >= 1801:
			r1 = numero_series_rango9["text"] * 6 + cartones_r9_6["text"] - 1801
			resultado = cartones_r9_6["text"],"-",r1
			carton_salida_liqui9.config(text=resultado,fg ="#2F4F4F")
		elif r1 <= 1800 and r1 != 0:
			resultado = cartones_r9_6["text"],"-",r1
			carton_salida_liqui9.config(text=resultado,fg ="#2F4F4F")

		#------------------Liquidacion cierre--------------------------

		series_cierr_6 = series_cierre_6()
		series_liquidacion_cierre.config(text=series_cierr_6, fg ="#2F4F4F")
		try:
			CarSalCie_6 = CarSalR1_6 + pico_salida_6 + (int(numero_series_rango1["text"]) * 6) + (int(numero_series_rango2["text"]) * 6) + (int(numero_series_rango3["text"]) * 6) + (int(numero_series_rango4["text"]) * 6) + (int(numero_series_rango5["text"]) * 6) + (int(numero_series_rango6["text"]) * 6) + (int(numero_series_rango7["text"]) * 6) + (int(numero_series_rango8["text"]) * 6) + (int(numero_series_rango9["text"]) * 6)
			diferencia = CarSalCie_6 - int(cierre.get()) 
			if diferencia == 1:
				carton_salida_liqui1_cierre.config(text= 0, fg ="#FF1493")
				pico_cierre_liqui.config(fg ="#FF1493")
			else:
				if CarSalCie_6 >= 1800:
					resultado = CarSalCie_6 - 1800, "-", cierre.get()
				else: 
					resultado = CarSalCie_6, "-", cierre.get()
				carton_salida_liqui1_cierre.config(text=resultado, fg ="#2F4F4F")
				pico_cierre_liqui.config(fg ="#2F4F4F")
		except:
			pass

		#----------------------Liquidación Total-----------------------------
		series_totales_6 = series_total_6()
		liquida_total = total_cartone_6 * 6,"€"
		liquidacion_liqui_total.config(text=liquida_total)
		total_series_liqui.config(text=series_totales_6, fg ="#2F4F4F")
		total_cartones_liquidacion.config(text=total_cartone_6, fg ="#2F4F4F")

		if int(CierreTotal.get()) == 1800:
			salida_6.set(1)
			PreparaRectifica()
			CartonSalida_6()
			total_car_6.config(text = 0)
			cierre.set("")
			CierreTotal.focus()
		else:
			salida_6.set(int (cierre.get()) + 1)
			PreparaRectifica()
			CartonSalida_6()
			total_car_6.config(text = 0)
			cierre.set("")
			CierreTotal.focus()

		pico_cierre_liqui.config(text = pico_cierre_fin)
		pico_final.config(text = 0)
		total_car_1.config(text=0)
		total_car_2.config(text=0)
		total_car_3.config(text=0)
		total_car_6.config(text=0)
	except:
		pass

# ---------------------------liquidacion------------------------------------------------

def liquida(num):
	global control_atras; global control_parpadeo; global historico

	control_parpadeo = 0
	if CierreTotal.get() == "" or CierreTotal.get() == "0":
		pass
	else:
		if num == 1.5:
			verifica = comprobacion_1()
			if verifica == 1:				
				pass
			else:
				comprobacion = series_cierre()
				if comprobacion == 1:
					pass
				else:
					control_atras = 1
					boton_atras['state'] = NORMAL
					sube_a_liquidacion()
					calcula_liquidacion(1.5)
					if historico == 1:
						datos_historico6()
					else:
						datos_historico1()
						historico = 1
		elif num == 2:
			verifica_2 = comprobacion_2()
			if verifica_2 == 1:
				pass
			else:
				comprobacion = series_cierre_2()
				if comprobacion == 1:
					pass
				else:
					control_atras = 2
					boton_atras['state'] = NORMAL
					sube_a_liquidacion_2()
					calcula_liquidacion(2)
					if historico == 1:
						datos_historico6()
					else:
						datos_historico1()
						historico = 1
		elif num == 3:
			verifica_3 = comprobacion_3()
			if verifica_3 == 1:
				pass
			else:
				comprobacion = series_cierre_3()
				if comprobacion == 1:
					pass
				else:
					control_atras = 3
					boton_atras['state'] = NORMAL
					sube_a_liquidacion_3()
					calcula_liquidacion(3)
					if historico == 1:
						datos_historico6()
					else:
						datos_historico1()
						historico = 1
		else:
			verifica_6 = comprobacion_6()
			if verifica_6 == 1:
				pass
			else:
				comprobacion = series_cierre_6()
				if comprobacion == 1:
					pass
				else:
					control_atras = 6
					boton_atras['state'] = NORMAL
					sube_a_liquidacion_6()
					calcula_liquidacion(6)
					if historico == 1:
						datos_historico6()
					else:
						datos_historico1()
						historico = 1

		CartonSalida_1_proxima()
		CartonSalida_2_proxima()
		CartonSalida_3_proxima()
		CartonSalida_6_proxima()

def calcula_liquidacion(num):
	global liquida_total; global liquida_cierre
	liquida_total = 0
	try:
		liquida1 = (int(series_liquidacionr1["text"]) * 6 + int(pico_salida_liqui1["text"])) * num ,"€"
		liquidacion_liqui1.config(text=liquida1)

		liquida2 = int(series_liquidacionr2["text"]) * 6 * num,"€"
		liquidacion_liqui2.config(text=liquida2)

		liquida3 = int(series_liquidacionr3["text"]) * 6 * num,"€"
		liquidacion_liqui3.config(text=liquida3)

		liquida4 = int(series_liquidacionr4["text"]) * 6 * num,"€"
		liquidacion_liqui4.config(text=liquida4)

		liquida5 = int(series_liquidacionr5["text"]) * 6 * num,"€"
		liquidacion_liqui5.config(text=liquida5)

		liquida6 = int(series_liquidacionr6["text"]) * 6 * num,"€"
		liquidacion_liqui6.config(text=liquida6)

		liquida7 = int(series_liquidacionr7["text"]) * 6 * num,"€"
		liquidacion_liqui7.config(text=liquida7)

		liquida8 = int(series_liquidacionr8["text"]) * 6 * num,"€"
		liquidacion_liqui8.config(text=liquida8)

		liquida9 = int(series_liquidacionr9["text"]) * 6 * num,"€"
		liquidacion_liqui9.config(text=liquida9)

		liquida_cierre = (int(series_liquidacion_cierre["text"]) * 6 + int(pico_cierre_liqui["text"]))* num,"€"
		liquidacion_liqui_cierre.config(text=liquida_cierre)

		liquida_total = int(total_cartones_liquidacion["text"]) * num,"€"
		liquidacion_liqui_total.config(text=liquida_total)

		totalCaja()
	except:
		pass

# ------------------------------memoria--------------------------------------
def guardar_datos():
    with open("memoria.txt", "w") as archivo:
        archivo.write(str(numero_series_rango1.cget("text")) + '\n')
        archivo.write(str(numero_series_rango2.cget("text")) + '\n')
        archivo.write(str(numero_series_rango3.cget("text")) + '\n')
        archivo.write(str(numero_series_rango4.cget("text")) + '\n')
        archivo.write(str(numero_series_rango5.cget("text")) + '\n')
        archivo.write(str(numero_series_rango6.cget("text")) + '\n')
        archivo.write(str(numero_series_rango7.cget("text")) + '\n')
        archivo.write(str(numero_series_rango8.cget("text")) + '\n')
        archivo.write(str(numero_series_rango9.cget("text")) + '\n')
        archivo.write(str(numero_series1.cget("text")) + '\n')
        archivo.write(str(numero_series2.cget("text")) + '\n')
        archivo.write(str(numero_series3.cget("text")) + '\n')
        archivo.write(str(numero_series4.cget("text")) + '\n')
        archivo.write(str(numero_series5.cget("text")) + '\n')
        archivo.write(str(numero_series6.cget("text")) + '\n')
        archivo.write(str(numero_series7.cget("text")) + '\n')
        archivo.write(str(numero_series8.cget("text")) + '\n')
        archivo.write(str(numero_series9.cget("text")))

# ---------------------------- Entorno Grafico---------------------------------------

raiz = Tk()
raiz.title("CAJA MESA CARBI-93")
raiz.attributes('-fullscreen', True)
raiz.config(bg="#000099")

caja_partida=IntVar()
linea=IntVar()
bingo=IntVar()

marco2=Frame(raiz,bg="#000099")
marco2.pack(expand=True, fill= BOTH)
marco1=Frame(raiz,bg="#3149E4")
marco1.pack(expand=True, fill= BOTH)

Venta_frame = Frame(raiz,bg="#000099")
Venta_frame.pack(expand=True, fill= BOTH)

label_linea = Label(Venta_frame, text ="      PREMIO DE LINEA",bg="#000099", fg ="#F0F8FF", font=("Times New Roman",12,"bold"))
label_linea.grid(row = 0, column = 0,pady=10)

entry_linea = Entry(Venta_frame,justify= RIGHT,textvariable=linea, font=("Arial",12,"bold"), width=10, state="readonly")
entry_linea.grid(row = 0, column = 1)

label_bingo = Label(Venta_frame, text ="        PREMIO DE BINGO",bg="#000099", fg ="#F0F8FF", font=("Times New Roman",12,"bold"))
label_bingo.grid(row = 0, column = 2)

entry_bingo = Entry(Venta_frame,justify= RIGHT,textvariable=bingo, font=("Arial",12,"bold"), width=10, state="readonly")
entry_bingo.grid(row = 0, column = 3)

label_venta = Label(Venta_frame, text ="         VENTA",bg="#000099", fg ="white", font=("Times New Roman",30,"bold"))
label_venta.grid(row = 0, column = 4, padx = 150)

label_caja_partida = Label(Venta_frame, text ="                                 CAJA PARTIDA",bg="#000099", fg ="#F0F8FF", font=("Times New Roman",12,"bold"))
label_caja_partida.grid(row = 0, column = 5)

entry_caja_partida = Entry(Venta_frame,justify= RIGHT,textvariable=caja_partida, font=("Arial",12,"bold"), width=10, state="readonly")
entry_caja_partida.grid(row = 0, column = 6)

marco=Frame(raiz)
marco.pack(expand=True, fill= BOTH)
marco.config(bg="lightblue")

marco0=Frame(raiz)
marco0.pack(expand=True, fill= BOTH)
marco0.config(bg="lightblue")

marcoA=Frame(raiz)
marcoA.pack(expand=True, fill= BOTH)
marcoA.config(bg="lightblue")

marcoB=Frame(raiz)
marcoB.pack(expand=True, fill= BOTH)
marcoB.config(bg="lightblue")

marcoFinal=Frame(raiz)
marcoFinal.pack(expand=True, fill= BOTH)
marcoFinal.config(bg="lightblue")

marcoIntermedioFinal=Frame(raiz)
marcoIntermedioFinal.pack(expand=True, fill= BOTH)
marcoIntermedioFinal.config(bg="lightblue")
Label(marcoIntermedioFinal, text = "",bg="lightblue", font=("Arial",3)).pack()

photoSube=PhotoImage(file=r"c:\CajaMesaControl\flechaSube.png")
photoBaja=PhotoImage(file=r"c:\CajaMesaControl\flechaBaja.png")

#variables
salida = IntVar()
salida_2 = IntVar()
salida_3 = IntVar()
salida_6 = IntVar()
totalCar = IntVar()
cierre = IntVar()
totalCar_2 = IntVar()

salida.set("")
salida_2.set("")
salida_3.set("")
salida_6.set("")

# ------------------------Frames precios------------------------------------------

precios_frame = Frame(marco)
precios_frame.pack(expand=True, fill= BOTH, side=LEFT)
precios_frame.config(bg="gray90")

Label(precios_frame, text = "PRECIOS",bg="gray90",fg="black", font=("Times New Roman",15)).pack(pady=6)

Label(precios_frame, text = "      ",bg="gray90", font=("Arial",10,"bold")).pack(pady=32)

Label(precios_frame, text="1,5€", bg="white", fg="blue", font=("Times New Roman",22,"bold"),width=3).pack()

Label(precios_frame, text= "2€", bg="white", fg="#8B0000", font=("Times New Roman",22,"bold"),width=3).pack(pady=30)

Label(precios_frame, text= "3€", bg="white", fg="#FF1493", font=("Times New Roman",22,"bold"),width=3).pack()

Label(precios_frame, text= "6€", bg="white", fg="#2F4F4F", font=("Times New Roman",22,"bold"),width=3).pack(pady=27)

# ------------------------Frames rango 1----------------------------------------

rango1_frame = Frame(marco)
rango1_frame.pack(expand=True, fill= BOTH, side=LEFT)
rango1_frame.config(bg="#31BFE4")

Label(rango1_frame, text = " RANGO 1",bg="#31BFE4",fg="green", font=("Times New Roman",20,"bold")).pack()

Label(rango1_frame, text = "SERIES",bg="#31BFE4", font=("Times New Roman",13,"bold")).pack()

numero_series_rango1=Label(rango1_frame, text=0,font=("Times New Roman",22,"bold"))
numero_series_rango1.pack()
numero_series_rango1.configure(foreground="blue", bg = "white",width=3)

Label(rango1_frame, text = "SALIDAS",bg="#31BFE4", font=("Times New Roman",13,"bold")).pack()


validacion = raiz.register(validar_entrada)

SalidaEntry_1 = Entry(rango1_frame,validate="key",validatecommand=(validacion, "%P"),justify= RIGHT,textvariable=salida, fg = "blue",  font=("Times New Roman",22,"bold"), width=5)
SalidaEntry_1.pack()
SalidaEntry_1.bind("<Return>", focus_next_window)

A = Label(rango1_frame, text= "", bg="#31BFE4", font=("Times New Roman",1),width=5)
A.config()
A.pack(pady = 1)

SalidaEntry_2 = Entry(rango1_frame,validate="key",validatecommand=(validacion, "%P"),justify= RIGHT, textvariable=salida_2, fg="#8B0000", font=("Times New Roman",22,"bold"), width=5)
SalidaEntry_2.pack(pady=23)
SalidaEntry_2.bind("<Return>", focus_next_window_2)

B = Label(rango1_frame, text= "", bg="#31BFE4", font=("Times New Roman",1),width=5)
B.config()
B.pack(pady = 1)

SalidaEntry_3 = Entry(rango1_frame,validate="key",validatecommand=(validacion, "%P"),justify= RIGHT, textvariable=salida_3, fg="#FF1493", font=("Times New Roman",22,"bold"), width=5)
SalidaEntry_3.pack()
SalidaEntry_3.bind("<Return>", focus_next_window_3)

C = Label(rango1_frame, text= "", bg="#31BFE4", font=("Times New Roman",1),width=5)
C.config()
C.pack(pady = 1)

SalidaEntry_6 = Entry(rango1_frame,validate="key",validatecommand=(validacion, "%P"),justify= RIGHT, textvariable=salida_6, fg="#2F4F4F", font=("Times New Roman",22,"bold"), width=5)
SalidaEntry_6.pack(pady=18)
SalidaEntry_6.bind("<Return>", focus_next_window_6)

#--------------------------Frame Picos-------------------------------------

rango_pico_salida_frame = Frame(marco)
rango_pico_salida_frame.pack(expand=True, fill= BOTH, side=LEFT)
rango_pico_salida_frame.config(bg="#31BFE4")

AA = Label(rango_pico_salida_frame, text= "", bg="#31BFE4", font=("Times New Roman",1))
AA.pack(pady = 60)

pico_r1 = Label(rango_pico_salida_frame, text = "0", bg="white",fg = "blue", font=("Times New Roman",12,"bold"))
pico_r1.pack()

pico_r1_2 = Label(rango_pico_salida_frame, text = "0", bg="white",fg = "#8B0000", font=("Times New Roman",12,"bold"))
pico_r1_2.pack(pady=45)

pico_r1_3 = Label(rango_pico_salida_frame, text = "0", bg="white",fg = "#FF1493", font=("Times New Roman",12,"bold"))
pico_r1_3.pack()

pico_r1_6 = Label(rango_pico_salida_frame, text = "0", bg="white",fg = "#2F4F4F", font=("Times New Roman",12,"bold"))
pico_r1_6.pack(pady=39)

# ------------------------Frames rango 2----------------------------------------

rango2_frame = Frame(marco)
rango2_frame.pack(expand=True, fill= BOTH, side=LEFT)
rango2_frame.config(bg="#C0C0C0")

label_R2 = Label(rango2_frame, text = "RANGO 2",bg="#C0C0C0", font=("Times New Roman",20,"bold"))
label_R2.pack()
label_R2.config(fg="black")

label_R2_series = Label(rango2_frame, text = "SERIES", font=("Times New Roman",13,"bold"))
label_R2_series.pack()
label_R2_series.configure(bg="#C0C0C0")

numero_series_rango2=Label(rango2_frame, text=0,font=("Times New Roman",22,"bold"))
numero_series_rango2.pack()
numero_series_rango2.configure(foreground="blue", bg = "white",width=3)

Label_R2_salida = Label(rango2_frame, text = "SALIDAS",bg="#C0C0C0", font=("Times New Roman",13,"bold"))
Label_R2_salida.pack()
Label_R2_salida.configure(bg="#C0C0C0")

cartones_r2 = Label(rango2_frame, text = "0" ,bg="white",fg="blue", font=("Times New Roman",18,"bold"),width=5)
cartones_r2.pack()
cartones_r2_proxima = Label(rango2_frame, text = "0" ,bg="white",fg="blue", font=("Times New Roman",12,"bold"),width=5)
cartones_r2_proxima.pack(pady=1)

Label(rango2_frame, text= "", bg="#C0C0C0", font=("Times New Roman",1),width=5).pack()

cartones_r2_2 = Label(rango2_frame, text= "0", bg="white", fg="#8B0000", font=("Times New Roman",18,"bold"),width=5)
cartones_r2_2.pack()
cartones_r2_2_proxima = Label(rango2_frame, text= "0", bg="white", fg="#8B0000", font=("Times New Roman",12,"bold"),width=5)
cartones_r2_2_proxima.pack(pady=1)

Label(rango2_frame, text= "", bg="#C0C0C0", font=("Times New Roman",1),width=5).pack()

cartones_r2_3= Label(rango2_frame, text="0", bg="white", fg="#FF1493", font=("Times New Roman",18,"bold"),width=5)
cartones_r2_3.pack()
cartones_r2_3_proxima= Label(rango2_frame, text="0", bg="white", fg="#FF1493", font=("Times New Roman",12,"bold"),width=5)
cartones_r2_3_proxima.pack(pady=1)

Label(rango2_frame, text= "", bg="#C0C0C0", font=("Times New Roman",1),width=5).pack()

cartones_r2_6= Label(rango2_frame, text="0", bg="white", fg="#2F4F4F", font=("Times New Roman",22,"bold"),width=5)
cartones_r2_6.pack()
cartones_r2_6_proxima= Label(rango2_frame, text="0", bg="white", fg="#2F4F4F", font=("Times New Roman",12,"bold"),width=5)
cartones_r2_6_proxima.pack(pady=1)

Label(rango2_frame, text= "", bg="#C0C0C0", font=("Times New Roman",1),width=5).pack()
# ------------------------Frames rango 3----------------------------------------

rango3_frame = Frame(marco)
rango3_frame.pack(expand=True, fill= BOTH, side=LEFT)
rango3_frame.config(bg="gray59")

label_R3 = Label(rango3_frame, text = "RANGO 3",bg="gray59", font=("Times New Roman",20,"bold"))
label_R3.pack()
label_R3.config(fg="black")

Label(rango3_frame, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

numero_series_rango3=Label(rango3_frame, text=0,font=("Times New Roman",22,"bold"))
numero_series_rango3.pack()
numero_series_rango3.configure(foreground="blue", bg = "white",width=3)

Label(rango3_frame, text = "SALIDAS",bg="gray59", font=("Times New Roman",13,"bold")).pack()

cartones_r3 = Label(rango3_frame, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"),width=5)
cartones_r3.pack()
cartones_r3_proxima = Label(rango3_frame, text = "0" ,bg="white",fg="blue", font=("Times New Roman",12,"bold"),width=5)
cartones_r3_proxima.pack(pady=1)

Label(rango3_frame, text= "", bg="gray59", font=("Times New Roman",1),width=5).pack()

cartones_r3_2= Label(rango3_frame, text="0", bg="white", fg="#8B0000", font=("Times New Roman",18,"bold"),width=5)
cartones_r3_2.pack()
cartones_r3_2_proxima = Label(rango3_frame, text = "0" ,bg="white",fg="#8B0000", font=("Times New Roman",12,"bold"),width=5)
cartones_r3_2_proxima.pack(pady=1)

Label(rango3_frame, text= "", bg="gray59", font=("Times New Roman",1),width=5).pack()

cartones_r3_3= Label(rango3_frame, text="0", bg="white", fg="#FF1493", font=("Times New Roman",18,"bold"),width=5)
cartones_r3_3.pack()
cartones_r3_3_proxima = Label(rango3_frame, text = "0" ,bg="white",fg="#FF1493", font=("Times New Roman",12,"bold"),width=5)
cartones_r3_3_proxima.pack(pady=1)

Label(rango3_frame, text= "", bg="gray59", font=("Times New Roman",1),width=5).pack()

cartones_r3_6= Label(rango3_frame, text="0", bg="white", fg="#2F4F4F", font=("Times New Roman",18,"bold"),width=5)
cartones_r3_6.pack()
cartones_r3_6_proxima = Label(rango3_frame, text = "0" ,bg="white",fg="#2F4F4F", font=("Times New Roman",12,"bold"),width=5)
cartones_r3_6_proxima.pack(pady=1)

# ------------------------Frames rango 4----------------------------------------

rango4_frame = Frame(marco)
rango4_frame.pack(expand=True, fill= BOTH, side=LEFT)
rango4_frame.config(bg="#C0C0C0")

label_R4 = Label(rango4_frame, text = "RANGO 4",bg="#C0C0C0", font=("Times New Roman",20,"bold"))
label_R4.pack()
label_R4.config(fg="black")

Label(rango4_frame, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

numero_series_rango4=Label(rango4_frame, text=0,font=("Times New Roman",22,"bold"))
numero_series_rango4.pack()
numero_series_rango4.configure(foreground="blue", bg = "white",width=3)

Label(rango4_frame, text = "SALIDAS",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

cartones_r4 = Label(rango4_frame, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"),width=5)
cartones_r4.pack()
cartones_r4_proxima = Label(rango4_frame, text = "0" ,bg="white",fg="blue", font=("Times New Roman",12,"bold"),width=5)
cartones_r4_proxima.pack(pady=1)

Label(rango4_frame, text= "", bg="#C0C0C0", font=("Times New Roman",1),width=5).pack()

cartones_r4_2= Label(rango4_frame, text="0", bg="white", fg="#8B0000", font=("Times New Roman",18,"bold"),width=5)
cartones_r4_2.pack()
cartones_r4_2_proxima = Label(rango4_frame, text = "0" ,bg="white",fg="#8B0000", font=("Times New Roman",12,"bold"),width=5)
cartones_r4_2_proxima.pack(pady=1)

Label(rango4_frame, text= "", bg="#C0C0C0", font=("Times New Roman",1),width=5).pack()

cartones_r4_3= Label(rango4_frame, text="0", bg="white", fg="#FF1493", font=("Times New Roman",18,"bold"),width=5)
cartones_r4_3.pack()
cartones_r4_3_proxima = Label(rango4_frame, text = "0" ,bg="white",fg="#FF1493", font=("Times New Roman",12,"bold"),width=5)
cartones_r4_3_proxima.pack(pady=1)

Label(rango4_frame, text= "", bg="#C0C0C0", font=("Times New Roman",1),width=5).pack()

cartones_r4_6= Label(rango4_frame, text="0", bg="white", fg="#2F4F4F", font=("Times New Roman",18,"bold"),width=5)
cartones_r4_6.pack()
cartones_r4_6_proxima = Label(rango4_frame, text = "0" ,bg="white",fg="#2F4F4F", font=("Times New Roman",12,"bold"),width=5)
cartones_r4_6_proxima.pack(pady=1)

# ------------------------Frames rango 5----------------------------------------

rango5_frame = Frame(marco)
rango5_frame.pack(expand=True, fill= BOTH, side=LEFT)
rango5_frame.config(bg="gray59")

label_R5 = Label(rango5_frame, text = "RANGO 5",bg="gray59", font=("Times New Roman",20,"bold"))
label_R5.pack()
label_R5.config(fg="black")

Label(rango5_frame, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

numero_series_rango5=Label(rango5_frame, text=0,font=("Times New Roman",22,"bold"))
numero_series_rango5.pack()
numero_series_rango5.configure(foreground="blue", bg = "white",width=3)

Label(rango5_frame, text = "SALIDAS",bg="gray59", font=("Times New Roman",13,"bold")).pack()

cartones_r5 = Label(rango5_frame, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"),width=5)
cartones_r5.pack()
cartones_r5_proxima = Label(rango5_frame, text = "0" ,bg="white",fg="blue", font=("Times New Roman",12,"bold"),width=5)
cartones_r5_proxima.pack(pady=1)

Label(rango5_frame, text= "", bg="gray59", font=("Times New Roman",1),width=5).pack()

cartones_r5_2= Label(rango5_frame, text="0", bg="white", fg="#8B0000", font=("Times New Roman",18,"bold"),width=5)
cartones_r5_2.pack()
cartones_r5_2_proxima = Label(rango5_frame, text = "0" ,bg="white",fg="#8B0000", font=("Times New Roman",12,"bold"),width=5)
cartones_r5_2_proxima.pack(pady=1)

Label(rango5_frame, text= "", bg="gray59", font=("Times New Roman",1),width=5).pack()

cartones_r5_3= Label(rango5_frame, text="0", bg="white", fg="#FF1493", font=("Times New Roman",18,"bold"),width=5)
cartones_r5_3.pack()
cartones_r5_3_proxima = Label(rango5_frame, text = "0" ,bg="white",fg="#FF1493", font=("Times New Roman",12,"bold"),width=5)
cartones_r5_3_proxima.pack(pady=1)

Label(rango5_frame, text= "", bg="gray59", font=("Times New Roman",1),width=5).pack()

cartones_r5_6= Label(rango5_frame, text="0", bg="white", fg="#2F4F4F", font=("Times New Roman",18,"bold"),width=5)
cartones_r5_6.pack()
cartones_r5_6_proxima = Label(rango5_frame, text = "0" ,bg="white",fg="#2F4F4F", font=("Times New Roman",12,"bold"),width=5)
cartones_r5_6_proxima.pack(pady=1)

# ------------------------Frames rango 6----------------------------------------

rango6_frame = Frame(marco)
rango6_frame.pack(expand=True, fill= BOTH, side=LEFT)
rango6_frame.config(bg="#C0C0C0")

label_R6 = Label(rango6_frame, text = "RANGO 6",bg="#C0C0C0", font=("Times New Roman",20,"bold"))
label_R6.pack()
label_R6.config(fg="black")

Label(rango6_frame, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

numero_series_rango6=Label(rango6_frame, text=0,font=("Times New Roman",22,"bold"))
numero_series_rango6.pack()
numero_series_rango6.configure(foreground="blue", bg = "white",width=3)

Label(rango6_frame, text = "SALIDAS",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

cartones_r6 = Label(rango6_frame, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"),width=5)
cartones_r6.pack()
cartones_r6_proxima = Label(rango6_frame, text = "0" ,bg="white",fg="blue", font=("Times New Roman",12,"bold"),width=5)
cartones_r6_proxima.pack(pady=1)

Label(rango6_frame, text= "", bg="#C0C0C0", font=("Times New Roman",1),width=5).pack()

cartones_r6_2= Label(rango6_frame, text="0", bg="white", fg="#8B0000", font=("Times New Roman",18,"bold"),width=5)
cartones_r6_2.pack()
cartones_r6_2_proxima = Label(rango6_frame, text = "0" ,bg="white",fg="#8B0000", font=("Times New Roman",12,"bold"),width=5)
cartones_r6_2_proxima.pack(pady=1)

Label(rango6_frame, text= "", bg="#C0C0C0", font=("Times New Roman",1),width=5).pack()

cartones_r6_3= Label(rango6_frame, text="0", bg="white", fg="#FF1493", font=("Times New Roman",18,"bold"),width=5)
cartones_r6_3.pack()
cartones_r6_3_proxima = Label(rango6_frame, text = "0" ,bg="white",fg="#FF1493", font=("Times New Roman",12,"bold"),width=5)
cartones_r6_3_proxima.pack(pady=1)

Label(rango6_frame, text= "", bg="#C0C0C0", font=("Times New Roman",1),width=5).pack()

cartones_r6_6= Label(rango6_frame, text="0", bg="white", fg="#2F4F4F", font=("Times New Roman",18,"bold"),width=5)
cartones_r6_6.pack()
cartones_r6_6_proxima = Label(rango6_frame, text = "0" ,bg="white",fg="#2F4F4F", font=("Times New Roman",12,"bold"),width=5)
cartones_r6_6_proxima.pack(pady=1)

# ------------------------Frames rango 7----------------------------------------

rango7_frame = Frame(marco)
rango7_frame.pack(expand=True, fill= BOTH, side=LEFT)
rango7_frame.config(bg="gray59")

label_R7 = Label(rango7_frame, text = "RANGO 7",bg="gray59", font=("Times New Roman",20,"bold"))
label_R7.pack()
label_R7.config(fg="black")

Label(rango7_frame, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

numero_series_rango7=Label(rango7_frame, text=0,font=("Times New Roman",22,"bold"))
numero_series_rango7.pack()
numero_series_rango7.configure(foreground="blue", bg = "white",width=3)

Label(rango7_frame, text = "SALIDAS",bg="gray59", font=("Times New Roman",13,"bold")).pack()

cartones_r7 = Label(rango7_frame, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"),width=5)
cartones_r7.pack()
cartones_r7_proxima = Label(rango7_frame, text = "0" ,bg="white",fg="blue", font=("Times New Roman",12,"bold"),width=5)
cartones_r7_proxima.pack(pady=1)

Label(rango7_frame, text= "", bg="gray59", font=("Times New Roman",1),width=5).pack()

cartones_r7_2= Label(rango7_frame, text="0", bg="white", fg="#8B0000", font=("Times New Roman",18,"bold"),width=5)
cartones_r7_2.pack()
cartones_r7_2_proxima = Label(rango7_frame, text = "0" ,bg="white",fg="#8B0000", font=("Times New Roman",12,"bold"),width=5)
cartones_r7_2_proxima.pack(pady=1)

Label(rango7_frame, text= "", bg="gray59", font=("Times New Roman",1),width=5).pack()

cartones_r7_3= Label(rango7_frame, text="0", bg="white", fg="#FF1493", font=("Times New Roman",18,"bold"),width=5)
cartones_r7_3.pack()
cartones_r7_3_proxima = Label(rango7_frame, text = "0" ,bg="white",fg="#FF1493", font=("Times New Roman",12,"bold"),width=5)
cartones_r7_3_proxima.pack(pady=1)

Label(rango7_frame, text= "", bg="gray59", font=("Times New Roman",1),width=5).pack()

cartones_r7_6= Label(rango7_frame, text="0", bg="white", fg="#2F4F4F", font=("Times New Roman",18,"bold"),width=5)
cartones_r7_6.pack()
cartones_r7_6_proxima = Label(rango7_frame, text = "0" ,bg="white",fg="#2F4F4F", font=("Times New Roman",12,"bold"),width=5)
cartones_r7_6_proxima.pack(pady=1)

# ------------------------Frames rango 8----------------------------------------

rango8_frame = Frame(marco)
rango8_frame.pack(expand=True, fill= BOTH, side=LEFT)
rango8_frame.config(bg="#C0C0C0")

label_R8 = Label(rango8_frame, text = "RANGO 8",bg="#C0C0C0", font=("Times New Roman",20,"bold"))
label_R8.pack()
label_R8.config(fg="black")

Label(rango8_frame, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

numero_series_rango8=Label(rango8_frame, text=0,font=("Times New Roman",22,"bold"))
numero_series_rango8.pack()
numero_series_rango8.configure(foreground="blue", bg = "white",width=3)

Label(rango8_frame, text = "SALIDAS",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

cartones_r8 = Label(rango8_frame, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"),width=5)
cartones_r8.pack()
cartones_r8_proxima = Label(rango8_frame, text = "0" ,bg="white",fg="blue", font=("Times New Roman",12,"bold"),width=5)
cartones_r8_proxima.pack(pady=1)

Label(rango8_frame, text= "", bg="#C0C0C0", font=("Times New Roman",1),width=5).pack()

cartones_r8_2= Label(rango8_frame, text="0", bg="white", fg="#8B0000", font=("Times New Roman",18,"bold"),width=5)
cartones_r8_2.pack()
cartones_r8_2_proxima = Label(rango8_frame, text = "0" ,bg="white",fg="#8B0000", font=("Times New Roman",12,"bold"),width=5)
cartones_r8_2_proxima.pack(pady=1)

Label(rango8_frame, text= "", bg="#C0C0C0", font=("Times New Roman",1),width=5).pack()

cartones_r8_3= Label(rango8_frame, text="0", bg="white", fg="#FF1493", font=("Times New Roman",18,"bold"),width=5)
cartones_r8_3.pack()
cartones_r8_3_proxima = Label(rango8_frame, text = "0" ,bg="white",fg="#FF1493", font=("Times New Roman",12,"bold"),width=5)
cartones_r8_3_proxima.pack(pady=1)

Label(rango8_frame, text= "", bg="#C0C0C0", font=("Times New Roman",1),width=5).pack()

cartones_r8_6= Label(rango8_frame, text="0", bg="white", fg="#2F4F4F", font=("Times New Roman",18,"bold"),width=5)
cartones_r8_6.pack()
cartones_r8_6_proxima = Label(rango8_frame, text = "0" ,bg="white",fg="#2F4F4F", font=("Times New Roman",12,"bold"),width=5)
cartones_r8_6_proxima.pack(pady=1)

# ------------------------Frames rango 9----------------------------------------

rango9_frame = Frame(marco)
rango9_frame.pack(expand=True, fill= BOTH, side=LEFT)
rango9_frame.config(bg="gray59")

label_R9 = Label(rango9_frame, text = "RANGO 9",bg="gray59", font=("Times New Roman",20,"bold"))
label_R9.pack()
label_R9.config(fg="black")

Label(rango9_frame, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

numero_series_rango9=Label(rango9_frame, text=0,font=("Times New Roman",22,"bold"))
numero_series_rango9.pack()
numero_series_rango9.configure(foreground="blue", bg = "white",width=3)

Label(rango9_frame, text = "SALIDAS",bg="gray59", font=("Times New Roman",13,"bold")).pack()

cartones_r9 = Label(rango9_frame, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"),width=5)
cartones_r9.pack()
cartones_r9_proxima = Label(rango9_frame, text = "0" ,bg="white",fg="blue", font=("Times New Roman",12,"bold"),width=5)
cartones_r9_proxima.pack(pady=1)

Label(rango9_frame, text= "", bg="gray59", font=("Times New Roman",1),width=5).pack()

cartones_r9_2= Label(rango9_frame, text="0", bg="white", fg="#8B0000", font=("Times New Roman",18,"bold"),width=5)
cartones_r9_2.pack()
cartones_r9_2_proxima = Label(rango9_frame, text = "0" ,bg="white",fg="#8B0000", font=("Times New Roman",12,"bold"),width=5)
cartones_r9_2_proxima.pack(pady=1)

Label(rango9_frame, text= "", bg="gray59", font=("Times New Roman",1),width=5).pack()

cartones_r9_3= Label(rango9_frame, text="0", bg="white", fg="#FF1493", font=("Times New Roman",18,"bold"),width=5)
cartones_r9_3.pack()
cartones_r9_3_proxima = Label(rango9_frame, text = "0" ,bg="white",fg="#FF1493", font=("Times New Roman",12,"bold"),width=5)
cartones_r9_3_proxima.pack(pady=1)

Label(rango9_frame, text= "", bg="gray59", font=("Times New Roman",1),width=5).pack()

cartones_r9_6= Label(rango9_frame, text="0", bg="white", fg="#2F4F4F", font=("Times New Roman",18,"bold"),width=5)
cartones_r9_6.pack()
cartones_r9_6_proxima = Label(rango9_frame, text = "0" ,bg="white",fg="#2F4F4F", font=("Times New Roman",12,"bold"),width=5)
cartones_r9_6_proxima.pack(pady=1)

# ------------------------Frames cierre----------------------------------------

cierre_frame = Frame(marco)
cierre_frame.pack(expand=True, fill= BOTH, side=LEFT)
cierre_frame.config(bg="#31BFE4")

Label(cierre_frame, text = " CIERRE ",bg="#31BFE4",fg="green", font=("Times New Roman",20,"bold")).pack()

Label(cierre_frame, text = "",bg="#31BFE4", font=("Arial",37,"bold")).pack()

Label(cierre_frame, text = "SALIDAS",bg="#31BFE4", font=("Times New Roman",13,"bold")).pack()

cartones_cierre = Label(cierre_frame, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"),width=5)
cartones_cierre.pack()
cartones_cierre_proxima = Label(cierre_frame, text = "0" ,bg="white",fg="blue", font=("Times New Roman",12,"bold"),width=5)
cartones_cierre_proxima.pack(pady=1)

Label(cierre_frame, text= "", bg="#31BFE4", font=("Times New Roman",1),width=5).pack()

cartones_cierre_2= Label(cierre_frame, text="0", bg="white", fg="#8B0000", font=("Times New Roman",18,"bold"),width=5)
cartones_cierre_2.pack()
cartones_cierre_2_proxima = Label(cierre_frame, text = "0" ,bg="white",fg="#8B0000", font=("Times New Roman",12,"bold"),width=5)
cartones_cierre_2_proxima.pack(pady=1)

Label(cierre_frame, text= "", bg="#31BFE4", font=("Times New Roman",1),width=5).pack()

cartones_cierre_3= Label(cierre_frame, text="0", bg="white", fg="#FF1493", font=("Times New Roman",18,"bold"),width=5)
cartones_cierre_3.pack()
cartones_cierre_3_proxima = Label(cierre_frame, text = "0" ,bg="white",fg="#FF1493", font=("Times New Roman",12,"bold"),width=5)
cartones_cierre_3_proxima.pack(pady=1)

Label(cierre_frame, text= "", bg="#31BFE4", font=("Times New Roman",1),width=5).pack()

cartones_cierre_6= Label(cierre_frame, text="0", bg="white", fg="#2F4F4F", font=("Times New Roman",18,"bold"),width=5)
cartones_cierre_6.pack()
cartones_cierre_6_proxima = Label(cierre_frame, text = "0" ,bg="white",fg="#2F4F4F", font=("Times New Roman",12,"bold"),width=5)
cartones_cierre_6_proxima.pack(pady=1)

#-----------------------------frame pico cierre-----------------------------

rango_pico_cierre_frame = Frame(marco)
rango_pico_cierre_frame.pack(expand=True, fill= BOTH, side=LEFT)
rango_pico_cierre_frame.config(bg="#31BFE4")

AA = Label(rango_pico_cierre_frame, text= "", bg="#31BFE4", font=("Times New Roman",1))
AA.pack(pady = 95)

pico_final = Label(rango_pico_cierre_frame, text = "0", bg="white",fg = "blue", font=("Times New Roman",12,"bold"))
pico_final.pack()

# ------------------------Frames total----------------------------------------

total_frame = Frame(marco)
total_frame.pack(expand=True, fill= BOTH, side=LEFT)
total_frame.config(bg="dodger blue")

Label(total_frame, text = "TOTAL",bg="dodger blue", font=("Times New Roman",20,"bold")).pack()
Label(total_frame, text = "",bg="dodger blue", font=("Arial",35,"bold")).pack()

Label(total_frame, text = "CARTONES",bg="dodger blue", font=("Times New Roman",13,"bold")).pack()

total_car_1 = Label(total_frame, text = "0", bg="white",fg ="blue", font=("Times New Roman",22,"bold"),width=5)
total_car_1.pack()

Label(total_frame, text= "", bg="dodger blue", font=("Times New Roman",1),width=5).pack()

total_car_2 = Label(total_frame, text = "0", bg="white",fg ="#8B0000", font=("Times New Roman",22,"bold"),width=5)
total_car_2.pack(pady=25)

Label(total_frame, text= "", bg="dodger blue", font=("Times New Roman",1),width=5).pack()

total_car_3 = Label(total_frame, text = "0", bg="white",fg ="#FF1493", font=("Times New Roman",22,"bold"),width=5)
total_car_3.pack()

Label(total_frame, text= "", bg="dodger blue", font=("Times New Roman",1),width=5).pack()

total_car_6 = Label(total_frame, text = "0", bg="white",fg ="#2F4F4F", font=("Times New Roman",22,"bold"),width=5)
total_car_6.pack(pady=17)

#------------------------------ zona botones liquída y atras------------------------------------------

var = IntVar()
var.set(2)


salida.set("")
cierre.set("")

validate_cierre = lambda text: text.isdecimal()

boton_liquida_1=Button(marco0, text="CIERRA 1,5€",command = lambda: liquida(1.5), bg ="blue", fg = "#F0F8FF", padx = 30, pady = 4, font=("Times New Roman", 14,"bold"), cursor="hand2", width=6)
boton_liquida_1.grid(row = 0, column = 0, padx=120, pady=5)

boton_liquida_2=Button(marco0, text="CIERRA 2€",command = lambda: liquida(2), bg="#8B0000", fg ="#F0F8FF", padx = 30, pady = 4, font=("Times New Roman", 14,"bold"),cursor="hand2", width=6, height=1 )
boton_liquida_2.grid(row = 0, column = 1, padx=80, pady=5)

Label(marco0, text = "CIERRE",bg="lightblue", font=("Times New Roman",15,"bold")).grid(row = 0, column = 2,pady = 4)
CierreTotal = Entry(marco0, validate="key", validatecommand=(marco0.register(validate_cierre), "%S"),justify= RIGHT, textvariable=cierre, font=("Arial",15,"bold"), width=6) #,validate="key",validatecommand=(marcoB.register(validate_cierre), "%S")
CierreTotal.grid(row = 0, column = 3, padx=10, pady = 10)
CierreTotal.bind("<Return>", prueba)

boton_liquida_3=Button(marco0, text="CIERRA 3€",command = lambda: liquida(3), bg="#FF1493", fg ="#F0F8FF", padx = 30, pady = 4, font=("Times New Roman", 14,"bold"),cursor="hand2", width=6, height=1 )
boton_liquida_3.grid(row = 0, column = 4, padx=80, pady=5)

boton_liquida_6=Button(marco0, text="CIERRA 6€",command = lambda: liquida(6), bg="#2F4F4F", fg ="#F0F8FF", padx = 30, pady = 4, font=("Times New Roman", 14,"bold"),cursor="hand2", width=6, height=1 )
boton_liquida_6.grid(row = 0, column = 5, padx=80, pady=5)

boton_atras=Button(marco0, text="ATRAS",command = atras, state = DISABLED, bg ="blue", fg = "#F0F8FF", font=("Times New Roman", 12,"bold") ,cursor="hand2")
boton_atras.grid(row = 0, column = 6, pady=5)

#----------------------------------------zona liquidacion rango 1----------------------------------------------

FrameLiquiR1 = Frame(marco1)
FrameLiquiR1.pack(expand=True, fill= BOTH, side=LEFT)
FrameLiquiR1.config(bg="#31BFE4")

label_R1_liquidacion = Label(FrameLiquiR1, text = "RANGO 1",bg="#31BFE4", font=("Times New Roman",20,"bold"))
label_R1_liquidacion.pack()
label_R1_liquidacion.config(fg="green")

liquidacion_liqui1 = Label(FrameLiquiR1, text = "0€", bg="white",fg="#800080", font=("Times New Roman",22,"bold"), width=7)
liquidacion_liqui1.pack()

pico_salida_liqui1 = Label(FrameLiquiR1, text = "0" ,fg="blue" ,bg="white", font=("Times New Roman",12,"bold"))
pico_salida_liqui1.pack(side=RIGHT,anchor=NW, pady = 30)


Label(FrameLiquiR1, text = "SERIES",bg="#31BFE4", font=("Times New Roman",13,"bold")).pack()

series_liquidacionr1 = Label(FrameLiquiR1, text = "0", bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_liquidacionr1.pack()

Label(FrameLiquiR1, text = "DEL - AL",bg="#31BFE4", font=("Times New Roman",13,"bold")).pack()

carton_salida_liqui1 = Label(FrameLiquiR1, text = "0", background="white",foreground="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_liqui1.pack()

#----------------------------------------zona liquidacion rango 2----------------------------------------------

FrameLiquiR2 = Frame(marco1)
FrameLiquiR2.pack(expand=True, fill= BOTH, side=LEFT)
FrameLiquiR2.config(bg="#C0C0C0")

label_R2_liquidacion = Label(FrameLiquiR2, text = "RANGO 2",bg="#C0C0C0", font=("Times New Roman",20,"bold"))
label_R2_liquidacion.pack()
label_R2_liquidacion.config(fg="black")

liquidacion_liqui2 = Label(FrameLiquiR2, text = "0€",bg="white",fg="#800080", font=("Times New Roman",22,"bold"), width=7)
liquidacion_liqui2.pack()

Label(FrameLiquiR2, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_liquidacionr2 = Label(FrameLiquiR2, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_liquidacionr2.pack()

Label(FrameLiquiR2, text = "DEL - AL",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

carton_salida_liqui2 = Label(FrameLiquiR2, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_liqui2.pack()

Label(FrameLiquiR2, text= "", bg="#C0C0C0", font=("Times New Roman",1),width=5).pack()

#----------------------------------------zona liquidacion rango 3----------------------------------------------

FrameLiquiR3 = Frame(marco1)
FrameLiquiR3.pack(expand=True, fill= BOTH, side=LEFT)
FrameLiquiR3.config(bg="gray59")

label_R3_liquidacion = Label(FrameLiquiR3, text = "RANGO 3",bg="gray59", font=("Times New Roman",20,"bold"))
label_R3_liquidacion.pack()
label_R3_liquidacion.config(fg="black")

liquidacion_liqui3 = Label(FrameLiquiR3, text = "0€",bg="white",fg="#800080", font=("Times New Roman",22,"bold"), width=7)
liquidacion_liqui3.pack()

Label(FrameLiquiR3, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_liquidacionr3 = Label(FrameLiquiR3, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_liquidacionr3.pack()

Label(FrameLiquiR3, text = "DEL - AL",bg="gray59", font=("Times New Roman",13,"bold")).pack()

carton_salida_liqui3 = Label(FrameLiquiR3, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_liqui3.pack()

#----------------------------------------zona liquidacion rango 4----------------------------------------------

FrameLiquiR4 = Frame(marco1)
FrameLiquiR4.pack(expand=True, fill= BOTH, side=LEFT)
FrameLiquiR4.config(bg="#C0C0C0")

label_R4_liquidacion = Label(FrameLiquiR4, text = "RANGO 4",bg="#C0C0C0", font=("Times New Roman",20,"bold"))
label_R4_liquidacion.pack()
label_R4_liquidacion.config(fg="black")

liquidacion_liqui4 = Label(FrameLiquiR4, text = "0€",bg="white",fg="#800080",font=("Times New Roman",22,"bold"), width=7)
liquidacion_liqui4.pack()

Label(FrameLiquiR4, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_liquidacionr4 = Label(FrameLiquiR4, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_liquidacionr4.pack()

Label(FrameLiquiR4, text = "DEL - AL",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

carton_salida_liqui4 = Label(FrameLiquiR4, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_liqui4.pack()

#----------------------------------------zona liquidacion rango 5----------------------------------------------

FrameLiquiR5 = Frame(marco1)
FrameLiquiR5.pack(expand=True, fill= BOTH, side=LEFT)
FrameLiquiR5.config(bg="gray59")

label_R5_liquidacion = Label(FrameLiquiR5, text = "RANGO 5",bg="gray59", font=("Times New Roman",20,"bold"))
label_R5_liquidacion.pack()
label_R5_liquidacion.config(fg="black")

liquidacion_liqui5 = Label(FrameLiquiR5, text = "0€",bg="white",fg="#800080", font=("Times New Roman",22,"bold"), width=7)
liquidacion_liqui5.pack()

Label(FrameLiquiR5, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_liquidacionr5 = Label(FrameLiquiR5, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_liquidacionr5.pack()

Label(FrameLiquiR5, text = "DEL - AL",bg="gray59", font=("Times New Roman",13,"bold")).pack()

carton_salida_liqui5 = Label(FrameLiquiR5, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_liqui5.pack()

#----------------------------------------zona liquidacion rango 6----------------------------------------------

FrameLiquiR6 = Frame(marco1)
FrameLiquiR6.pack(expand=True, fill= BOTH, side=LEFT)
FrameLiquiR6.config(bg="#C0C0C0")

label_R6_liquidacion = Label(FrameLiquiR6, text = "RANGO 6",bg="#C0C0C0", font=("Times New Roman",20,"bold"))
label_R6_liquidacion.pack()
label_R6_liquidacion.config(fg="black")

liquidacion_liqui6 = Label(FrameLiquiR6, text = "0€",bg="white",fg="#800080", font=("Times New Roman",22,"bold"), width=7)
liquidacion_liqui6.pack()

Label(FrameLiquiR6, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_liquidacionr6 = Label(FrameLiquiR6, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_liquidacionr6.pack()

Label(FrameLiquiR6, text = "DEL - AL",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

carton_salida_liqui6 = Label(FrameLiquiR6, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_liqui6.pack()

#----------------------------------------zona liquidacion rango 7----------------------------------------------

FrameLiquiR7 = Frame(marco1)
FrameLiquiR7.pack(expand=True, fill= BOTH, side=LEFT)
FrameLiquiR7.config(bg="gray59")

label_R7_liquidacion = Label(FrameLiquiR7, text = "RANGO 7",bg="gray59", font=("Times New Roman",20,"bold"))
label_R7_liquidacion.pack()
label_R7_liquidacion.config(fg="black")

liquidacion_liqui7 = Label(FrameLiquiR7, text = "0€",bg="white",fg="#800080", font=("Times New Roman",22,"bold"), width=7)
liquidacion_liqui7.pack()

Label(FrameLiquiR7, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_liquidacionr7 = Label(FrameLiquiR7, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_liquidacionr7.pack()

Label(FrameLiquiR7, text = "DEL - AL",bg="gray59", font=("Times New Roman",13,"bold")).pack()

carton_salida_liqui7 = Label(FrameLiquiR7, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_liqui7.pack()

#----------------------------------------zona liquidacion rango 8----------------------------------------------

FrameLiquiR8 = Frame(marco1)
FrameLiquiR8.pack(expand=True, fill= BOTH, side=LEFT)
FrameLiquiR8.config(bg="#C0C0C0")

label_R8_liquidacion = Label(FrameLiquiR8, text = "RANGO 8",bg="#C0C0C0", font=("Times New Roman",20,"bold"))
label_R8_liquidacion.pack()
label_R8_liquidacion.config(fg="black")

liquidacion_liqui8 = Label(FrameLiquiR8, text = "0",bg="white",fg="#800080", font=("Times New Roman",22,"bold"), width=7)
liquidacion_liqui8.pack()

Label(FrameLiquiR8, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_liquidacionr8 = Label(FrameLiquiR8, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_liquidacionr8.pack()

Label(FrameLiquiR8, text = "DEL - AL",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

carton_salida_liqui8 = Label(FrameLiquiR8, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_liqui8.pack()

#----------------------------------------zona liquidacion rango 9----------------------------------------------

FrameLiquiR9 = Frame(marco1)
FrameLiquiR9.pack(expand=True, fill= BOTH, side=LEFT)
FrameLiquiR9.config(bg="gray59")

label_R9_liquidacion = Label(FrameLiquiR9, text = "RANGO 9",bg="gray59", font=("Times New Roman",20,"bold"))
label_R9_liquidacion.pack()
label_R9_liquidacion.config(fg="black")

liquidacion_liqui9 = Label(FrameLiquiR9, text = "0€",bg="white",fg="#800080", font=("Times New Roman",22,"bold"), width=7)
liquidacion_liqui9.pack()

Label(FrameLiquiR9, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_liquidacionr9 = Label(FrameLiquiR9, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_liquidacionr9.pack()

Label(FrameLiquiR9, text = "DEL - AL",bg="gray59", font=("Times New Roman",13,"bold")).pack()

carton_salida_liqui9 = Label(FrameLiquiR9, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_liqui9.pack()

#----------------------------------------zona liquidacion rango cierre----------------------------------------------

FrameLiquiCierre = Frame(marco1)
FrameLiquiCierre.pack(expand=True, fill= BOTH, side=LEFT)
FrameLiquiCierre.config(bg="#31BFE4")

Label(FrameLiquiCierre, text = "CIERRE",bg="#31BFE4",fg="green", font=("Times New Roman",20,"bold")).pack()

liquidacion_liqui_cierre = Label(FrameLiquiCierre, text = "0€",bg="white",fg="#800080", font=("Times New Roman",22,"bold"),width=7)
liquidacion_liqui_cierre.pack()

pico_cierre_liqui = Label(FrameLiquiCierre, text = "0" ,fg="blue" ,bg="white", font=("Times New Roman",12,"bold"), width=1)
pico_cierre_liqui.pack(side=RIGHT,anchor=NW, pady = 30)

Label(FrameLiquiCierre, text = "SERIES",bg="#31BFE4", font=("Times New Roman",13,"bold")).pack()

series_liquidacion_cierre = Label(FrameLiquiCierre, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_liquidacion_cierre.pack()

Label(FrameLiquiCierre, text = "DEL - AL",bg="#31BFE4", font=("Times New Roman",13,"bold")).pack()

carton_salida_liqui1_cierre = Label(FrameLiquiCierre, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_liqui1_cierre.pack()

#----------------------------------------zona liquidacion rango total----------------------------------------------

FrameLiquiTotal = Frame(marco1)
FrameLiquiTotal.pack(expand=True, fill= BOTH, side=LEFT)
FrameLiquiTotal.config(bg="dodger blue")

Label(FrameLiquiTotal, text = "TOTAL",bg="dodger blue", font=("Times New Roman",20,"bold")).pack()

liquidacion_liqui_total = Label(FrameLiquiTotal, text = "0€",bg="white",fg="#800080", font=("Times New Roman",22,"bold"), width=7)
liquidacion_liqui_total.pack()

Label(FrameLiquiTotal, text = "SERIES",bg="dodger blue", font=("Times New Roman",13,"bold")).pack()
total_series_liqui = Label(FrameLiquiTotal, text = "0",bg="white",fg ="blue", font=("Times New Roman",22,"bold"), width=4)
total_series_liqui.pack()
Label(FrameLiquiTotal, text = "CARTONES",bg="dodger blue", font=("Times New Roman",13,"bold")).pack()

total_cartones_liquidacion = Label(FrameLiquiTotal, text = "0",bg="white",fg ="blue", font=("Times New Roman",18,"bold"), width=8)
total_cartones_liquidacion.pack()

#----------------------------------------zona sube/baja series rango 0------------------------------------------------------

rangoFinal0_frame = Frame(marcoFinal)
rangoFinal0_frame.pack(expand=True, fill= BOTH, side=LEFT)
rangoFinal0_frame.config(bg="gray90")

Button(rangoFinal0_frame, text="Histórico", command=poner_al_frente_root, bg= "Green", fg="White",font=("Times New Roman",15,"bold"),cursor="hand2", width=7).grid(row = 0, column = 0, padx=3, pady = 10)
Button(rangoFinal0_frame, text= "RESET", command=reset, bg= "#8B0000", fg="White",font=("Times New Roman",15,"bold"),cursor="hand2", width=7).grid(row = 1, column = 0, pady = 10)
Button(rangoFinal0_frame, text= "SALIR", command= cerrar, bg= "red", fg="White", font=("Times New Roman",15,"bold"),cursor="hand2", width=7).grid(row = 2, column = 0)

#----------------------------------------zona sube/baja series rango 1------------------------------------------------------

rangoFinal1_frame = Frame(marcoFinal)
rangoFinal1_frame.pack(expand=True, fill= BOTH, side=LEFT)
rangoFinal1_frame.config(bg="gray59")

Label(rangoFinal1_frame, text = "  RANGO 1  ",bg="gray59", font=("Times New Roman",18,"bold")).pack()

Label(rangoFinal1_frame, text = "SERIES",bg="gray59", font=("Arial",10,"bold")).pack()

numero_series1=Label(rangoFinal1_frame, text=valor1,font=("Times New Roman",17,"bold"), width=2)
numero_series1.pack()
numero_series1.configure(foreground="blue", bg = "white")

Label(rangoFinal1_frame, text="",font=("Arial",1),bg = "gray59").pack()

boton_sube_series1=Button(rangoFinal1_frame, command= lambda: incrementar(1), bg = "gray59", image=photoSube, padx = 10, pady=2,cursor="hand2")
boton_sube_series1.pack()

Label(rangoFinal1_frame, text="", font=("Times New Roman",1), bg = "gray59").pack()
boton_sube_ahora1=Button(rangoFinal1_frame, text="SUBIR", command= lambda: subir(1), bg="#8B0000", fg ="#F0F8FF", padx = 10 ,cursor="hand2")
boton_sube_ahora1.pack()
Label(rangoFinal1_frame, text="", font=("Times New Roman",1), bg = "gray59").pack()

boton_baja_series1=Button(rangoFinal1_frame, command= lambda: decrementar(1), bg = "gray59", image=photoBaja, padx = 10,cursor="hand2" )
boton_baja_series1.pack()

#----------------------------------------zona sube/baja series rango 2------------------------------------------------------

rangoFinal2_frame = Frame(marcoFinal)
rangoFinal2_frame.pack(expand=True, fill= BOTH, side=LEFT)
rangoFinal2_frame.config(bg="#C0C0C0")

Label(rangoFinal2_frame, text = " RANGO 2 ",bg="#C0C0C0", font=("Times New Roman",18,"bold")).pack()
Label(rangoFinal2_frame, text = "SERIES",bg="#C0C0C0", font=("Arial",10,"bold")).pack()

numero_series2=Label(rangoFinal2_frame, text=valor2,font=("Times New Roman",17,"bold"), width=2)
numero_series2.pack()
numero_series2.configure(foreground="blue", bg = "white")

Label(rangoFinal2_frame, text="",font=("Arial",1),bg = "#C0C0C0").pack()

boton_sube_series2=Button(rangoFinal2_frame, text="R2 +", command= lambda: incrementar(2), bg = "#C0C0C0", image=photoSube, padx = 10,cursor="hand2" )
boton_sube_series2.pack()

Label(rangoFinal2_frame, text="", font=("Times New Roman",1), bg = "#C0C0C0").pack()
boton_sube_ahora2=Button(rangoFinal2_frame, text="SUBIR", command= lambda: subir(2), bg="#8B0000", fg ="#F0F8FF", padx = 10 ,cursor="hand2")
boton_sube_ahora2.pack()
Label(rangoFinal2_frame, text="", font=("Times New Roman",1), bg = "#C0C0C0").pack()


boton_baja_series2=Button(rangoFinal2_frame, text="R2 -", command= lambda: decrementar(2), bg = "#C0C0C0", image=photoBaja, padx = 10,cursor="hand2")
boton_baja_series2.pack()

#----------------------------------------zona sube/baja series rango 3------------------------------------------------------

rangoFinal3_frame = Frame(marcoFinal)
rangoFinal3_frame.pack(expand=True, fill= BOTH, side=LEFT)
rangoFinal3_frame.config(bg="gray59")

Label(rangoFinal3_frame, text = " RANGO 3 ",bg="gray59", font=("Times New Roman",18,"bold")).pack()
Label(rangoFinal3_frame, text = "SERIES",bg="gray59", font=("Arial",10,"bold")).pack()

numero_series3=Label(rangoFinal3_frame, text=valor3, font=("Times New Roman",17,"bold"), width=2)
numero_series3.pack()
numero_series3.configure(foreground="blue", bg = "white")

Label(rangoFinal3_frame, text="",font=("Arial",1),bg = "gray59").pack()

boton_sube_series3=Button(rangoFinal3_frame, text="R3 +", command= lambda: incrementar(3), bg = "gray59", image=photoSube, padx = 10,cursor="hand2")
boton_sube_series3.pack()
boton_sube_series3.configure()

Label(rangoFinal3_frame, text="", font=("Times New Roman",1), bg = "gray59").pack()
boton_sube_ahora3=Button(rangoFinal3_frame, text="SUBIR", command= lambda: subir(3), bg="#8B0000", fg ="#F0F8FF", padx = 10 ,cursor="hand2")
boton_sube_ahora3.pack()
Label(rangoFinal3_frame, text="", font=("Times New Roman",1), bg = "gray59").pack()


boton_baja_series3=Button(rangoFinal3_frame, text="R3 -", command= lambda: decrementar(3), bg = "gray59", image=photoBaja, padx = 10,cursor="hand2" )
boton_baja_series3.pack()

#----------------------------------------zona sube/baja series rango 4------------------------------------------------------

rangoFinal4_frame = Frame(marcoFinal)
rangoFinal4_frame.pack(expand=True, fill= BOTH, side=LEFT)
rangoFinal4_frame.config(bg="#C0C0C0")

Label(rangoFinal4_frame, text = " RANGO 4 ",bg="#C0C0C0", font=("Times New Roman",18,"bold")).pack()
Label(rangoFinal4_frame, text = "SERIES",bg="#C0C0C0", font=("Arial",10,"bold")).pack()

numero_series4=Label(rangoFinal4_frame, text=valor4,font=("Times New Roman",17,"bold"), width=2)
numero_series4.pack()
numero_series4.configure(foreground="blue", bg = "white")

Label(rangoFinal4_frame, text="",font=("Arial",1),bg = "#C0C0C0").pack()

boton_sube_series4=Button(rangoFinal4_frame, text="R4 +", command= lambda: incrementar(4), bg = "#C0C0C0", image=photoSube, padx = 10,cursor="hand2")
boton_sube_series4.pack()

Label(rangoFinal4_frame, text="", font=("Times New Roman",1), bg = "#C0C0C0").pack()
boton_sube_ahora4=Button(rangoFinal4_frame, text="SUBIR", command= lambda: subir(4), bg="#8B0000", fg ="#F0F8FF", padx = 10 ,cursor="hand2")
boton_sube_ahora4.pack()
Label(rangoFinal4_frame, text="", font=("Times New Roman",1), bg = "#C0C0C0").pack()


boton_baja_series4=Button(rangoFinal4_frame, text="R4 -", command= lambda: decrementar(4), bg = "#C0C0C0", image=photoBaja, padx = 10,cursor="hand2")
boton_baja_series4.pack()

#----------------------------------------zona sube/baja series rango 5------------------------------------------------------

rangoFinal5_frame = Frame(marcoFinal)
rangoFinal5_frame.pack(expand=True, fill= BOTH, side=LEFT)
rangoFinal5_frame.config(bg="gray59")

Label(rangoFinal5_frame, text = " RANGO 5 ",bg="gray59", font=("Times New Roman",18,"bold")).pack()
Label(rangoFinal5_frame, text = "SERIES",bg="gray59", font=("Arial",10,"bold")).pack()

numero_series5=Label(rangoFinal5_frame, text=valor5,font=("Times New Roman",17,"bold"), width=2)
numero_series5.pack()
numero_series5.configure(foreground="blue", bg = "white")

Label(rangoFinal5_frame, text="",font=("Arial",1),bg = "gray59").pack()

boton_sube_series5=Button(rangoFinal5_frame, text="R5 +", command= lambda: incrementar(5), bg = "gray59", image=photoSube, padx = 10,cursor="hand2" )
boton_sube_series5.pack()

Label(rangoFinal5_frame, text="", font=("Times New Roman",1), bg = "gray59").pack()
boton_sube_ahora5=Button(rangoFinal5_frame, text="SUBIR", command= lambda: subir(5), bg="#8B0000", fg ="#F0F8FF", padx = 10 ,cursor="hand2")
boton_sube_ahora5.pack()
Label(rangoFinal5_frame, text="", font=("Times New Roman",1), bg = "gray59").pack()


boton_baja_series5=Button(rangoFinal5_frame, text="R5 -", command= lambda: decrementar(5), bg = "gray59", image=photoBaja, padx = 10,cursor="hand2" )
boton_baja_series5.pack()

#----------------------------------------zona sube/baja series rango 6------------------------------------------------------

rangoFinal6_frame = Frame(marcoFinal)
rangoFinal6_frame.pack(expand=True, fill= BOTH, side=LEFT)
rangoFinal6_frame.config(bg="#C0C0C0")

Label(rangoFinal6_frame, text = " RANGO 6 ",bg="#C0C0C0", font=("Times New Roman",18,"bold")).pack()
Label(rangoFinal6_frame, text = "SERIES",bg="#C0C0C0", font=("Arial",10,"bold")).pack()

numero_series6=Label(rangoFinal6_frame, text=valor6,font=("Times New Roman",17,"bold"), width=2)
numero_series6.pack()
numero_series6.configure(foreground="blue", bg = "white")

Label(rangoFinal6_frame, text="",font=("Arial",1),bg = "#C0C0C0").pack()

boton_sube_series6=Button(rangoFinal6_frame, text="R6 +", command= lambda: incrementar(6), bg = "#C0C0C0", image=photoSube, padx = 10 ,cursor="hand2")
boton_sube_series6.pack()

Label(rangoFinal6_frame, text="", font=("Times New Roman",1), bg = "#C0C0C0").pack()
boton_sube_ahora6=Button(rangoFinal6_frame, text="SUBIR", command= lambda: subir(6), bg="#8B0000", fg ="#F0F8FF", padx = 10 ,cursor="hand2")
boton_sube_ahora6.pack()
Label(rangoFinal6_frame, text="", font=("Times New Roman",1), bg = "#C0C0C0").pack()


boton_baja_series6=Button(rangoFinal6_frame, text="R6 -", command= lambda: decrementar(6), bg = "#C0C0C0", image=photoBaja, padx = 10,cursor="hand2" )
boton_baja_series6.pack()

#----------------------------------------zona sube/baja series rango 7------------------------------------------------------

rangoFinal7_frame = Frame(marcoFinal)
rangoFinal7_frame.pack(expand=True, fill= BOTH, side=LEFT)
rangoFinal7_frame.config(bg="gray59")

Label(rangoFinal7_frame, text = " RANGO 7 ",bg="gray59", font=("Times New Roman",18,"bold")).pack()
Label(rangoFinal7_frame, text = "SERIES",bg="gray59", font=("Arial",10,"bold")).pack()

numero_series7=Label(rangoFinal7_frame, text=valor7,font=("Times New Roman",17,"bold"), width=2)
numero_series7.pack()
numero_series7.configure(foreground="blue", bg = "white")

Label(rangoFinal7_frame, text="",font=("Arial",1),bg = "gray59").pack()

boton_sube_series7=Button(rangoFinal7_frame, text="R7 +", command= lambda: incrementar(7), bg = "gray59", image=photoSube, padx = 10,cursor="hand2" )
boton_sube_series7.pack()

Label(rangoFinal7_frame, text="", font=("Times New Roman",1), bg = "gray59").pack()
boton_sube_ahora7=Button(rangoFinal7_frame, text="SUBIR", command= lambda: subir(7), bg="#8B0000", fg ="#F0F8FF", padx = 10 ,cursor="hand2")
boton_sube_ahora7.pack()
Label(rangoFinal7_frame, text="", font=("Times New Roman",1), bg = "gray59").pack()

boton_baja_series7=Button(rangoFinal7_frame, text="R7 -", command= lambda: decrementar(7), bg = "gray59", image=photoBaja, padx = 10,cursor="hand2" )
boton_baja_series7.pack()

#----------------------------------------zona sube/baja series rango 8------------------------------------------------------

rangoFinal8_frame = Frame(marcoFinal)
rangoFinal8_frame.pack(expand=True, fill= BOTH, side=LEFT)
rangoFinal8_frame.config(bg="#C0C0C0")

Label(rangoFinal8_frame, text = " RANGO 8 ",bg="#C0C0C0", font=("Times New Roman",18,"bold")).pack()
Label(rangoFinal8_frame, text = "SERIES",bg="#C0C0C0", font=("Arial",10,"bold")).pack()

numero_series8=Label(rangoFinal8_frame, text=valor8,font=("Times New Roman",17,"bold"), width=2)
numero_series8.pack()
numero_series8.configure(foreground="blue", bg = "white")

Label(rangoFinal8_frame, text="",font=("Arial",1),bg = "#C0C0C0").pack()

boton_sube_series8=Button(rangoFinal8_frame, text="R8 +", command= lambda: incrementar(8), bg = "#C0C0C0", image=photoSube, padx = 10,cursor="hand2" )
boton_sube_series8.pack()

Label(rangoFinal8_frame, text="", font=("Times New Roman",1), bg = "#C0C0C0").pack()
boton_sube_ahora8=Button(rangoFinal8_frame, text="SUBIR", command= lambda: subir(8), bg="#8B0000", fg ="#F0F8FF", padx = 10 ,cursor="hand2")
boton_sube_ahora8.pack()
Label(rangoFinal8_frame, text="", font=("Times New Roman",1), bg = "#C0C0C0").pack()

boton_baja_series8=Button(rangoFinal8_frame, text="R8 -", command= lambda: decrementar(8), bg = "#C0C0C0", image=photoBaja, padx = 10,cursor="hand2" )
boton_baja_series8.pack()

#----------------------------------------zona sube/baja series rango 9------------------------------------------------------

rangoFinal9_frame = Frame(marcoFinal)
rangoFinal9_frame.pack(expand=True, fill= BOTH, side=LEFT)
rangoFinal9_frame.config(bg="gray59")

Label(rangoFinal9_frame, text = " RANGO 9 ",bg="gray59", font=("Times New Roman",18,"bold")).pack()
Label(rangoFinal9_frame, text = "SERIES",bg="gray59", font=("Arial",10,"bold")).pack()

numero_series9=Label(rangoFinal9_frame, text=valor9,font=("Times New Roman",17,"bold"), width=2)
numero_series9.pack()
numero_series9.configure(foreground="blue", bg = "white")

Label(rangoFinal9_frame, text="",font=("Arial",1),bg = "gray59").pack()

boton_sube_series9=Button(rangoFinal9_frame, text="R9 +", command= lambda: incrementar(9), bg = "gray59", image=photoSube, padx = 10 ,cursor="hand2")
boton_sube_series9.pack()

Label(rangoFinal9_frame, text="", font=("Times New Roman",1), bg = "gray59").pack()
boton_sube_ahora9=Button(rangoFinal9_frame, text="SUBIR", command= lambda: subir(9), bg="#8B0000", fg ="#F0F8FF", padx = 10 ,cursor="hand2")
boton_sube_ahora9.pack()
Label(rangoFinal9_frame, text="", font=("Times New Roman",1), bg = "gray59").pack()

boton_baja_series9=Button(rangoFinal9_frame, text="R9 -", command= lambda: decrementar(9), bg = "gray59", image=photoBaja, padx = 10 ,cursor="hand2")
boton_baja_series9.pack()

Label(rangoFinal9_frame, text = "",bg="gray59", font=("Arial",3)).pack()

#----------------------------------------zona sube/baja series cierre------------------------------------------------------

cierreFinal_frame = Frame(marcoFinal)
cierreFinal_frame.pack(expand=True, fill= BOTH, side=LEFT)
cierreFinal_frame.config(bg="#31BFE4")

etiqueta_vacia=Label(cierreFinal_frame, text = "",bg="#31BFE4", font=("Arial", 30))
etiqueta_vacia.pack()
boton_prepara_rectifica=Button(cierreFinal_frame, text="  COMENZAR  ",command = PreparaRectifica, bg="#8B0000", fg ="#F0F8FF", padx = 22, pady = 4, font=("Times New Roman", 15,"bold"),cursor="hand2" )
boton_prepara_rectifica.pack()
etiquita_instrucciones_inicial=Label(cierreFinal_frame, text = "Prepare series y pulse\neste botón para comenzar", font=("Arial", 14))
etiquita_instrucciones_inicial.pack()
etiquita_instrucciones_inicial.config(foreground="black", background="#31BFE4")

parpadeo_inicial(etiquita_instrucciones_inicial)

#---------------------------------------------------------------------------------------------------------------------

# Ventana historico

root = Toplevel()
root.title("Historico")
root.attributes('-fullscreen', True)
root.config(bg="#000099")

medio = Frame(root)
medio.config(bg="white")
medio.pack()
Label(medio, text="PARTIDA ACTUAL", bg="#000099", fg="white", font=("Times New Roman",15,"bold")).pack()

# Historico 1
marco_historico_1 = Frame(root)
marco_historico_1.pack(expand=True, fill= BOTH)
marco_historico_1.config(bg="lightblue")

# Historico_1 rango_1
frame_histortico_1_rango_1 = Frame(marco_historico_1)
frame_histortico_1_rango_1.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_1_rango_1.config(bg="#31BFE4")

label_historico_1_rango1 = Label(frame_histortico_1_rango_1, text = "RANGO 1",bg="#31BFE4", font=("Times New Roman",16,"bold"))
label_historico_1_rango1.pack()
#label_historico_1_rango1.config(fg="green")

liquidacion_historico_1_rango1 = Label(frame_histortico_1_rango_1, text = "0€", bg="white",fg="#800080", font=("Times New Roman",18,"bold"), width=7)
liquidacion_historico_1_rango1.pack()

pico_salida_historico_1_rango_1 = Label(frame_histortico_1_rango_1, text = "0" ,fg="blue" ,bg="white", font=("Times New Roman",12,"bold"))
pico_salida_historico_1_rango_1.pack(side=RIGHT,anchor=NW, pady = 30)

Label(frame_histortico_1_rango_1, text = "SERIES",bg="#31BFE4", font=("Times New Roman",13,"bold")).pack()

series_histirico_1_rango_1 = Label(frame_histortico_1_rango_1, text = "0", bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=2)
series_histirico_1_rango_1.pack()

carton_salida_historico_1_rango_1 = Label(frame_histortico_1_rango_1, text = "0", background="white",foreground="blue", font=("Times New Roman",16,"bold"), width=8)
carton_salida_historico_1_rango_1.pack(pady=1)

# Historico_1 rango_2
frame_histortico_1_rango_2 = Frame(marco_historico_1)
frame_histortico_1_rango_2.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_1_rango_2.config(bg="#C0C0C0")

label_historico_1_rango2 = Label(frame_histortico_1_rango_2, text = "RANGO 2",bg="#C0C0C0", font=("Times New Roman",16,"bold"))
label_historico_1_rango2.pack()
label_historico_1_rango2.config(fg="black")

liquidacion_historico_1_rango2 = Label(frame_histortico_1_rango_2, text = "0€",bg="white",fg="#800080", font=("Times New Roman",18,"bold"), width=7)
liquidacion_historico_1_rango2.pack()

Label(frame_histortico_1_rango_2, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_1_rango_2 = Label(frame_histortico_1_rango_2, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=2)
series_histirico_1_rango_2.pack()

carton_salida_historico_1_rango_2 = Label(frame_histortico_1_rango_2, text = "0",bg="white",fg="blue", font=("Times New Roman",16,"bold"), width=8)
carton_salida_historico_1_rango_2.pack(pady=1)

# Historico_1 rango_3
frame_histortico_1_rango_3 = Frame(marco_historico_1)
frame_histortico_1_rango_3.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_1_rango_3.config(bg="gray59")

label_historico_1_rango2 = Label(frame_histortico_1_rango_3, text = "RANGO 3",bg="gray59", font=("Times New Roman",16,"bold"))
label_historico_1_rango2.pack()
label_historico_1_rango2.config(fg="black")

liquidacion_historico_1_rango3 = Label(frame_histortico_1_rango_3, text = "0€",bg="white",fg="#800080", font=("Times New Roman",18,"bold"), width=7)
liquidacion_historico_1_rango3.pack()

Label(frame_histortico_1_rango_3, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_1_rango_3 = Label(frame_histortico_1_rango_3, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=2)
series_histirico_1_rango_3.pack()

carton_salida_historico_1_rango_3 = Label(frame_histortico_1_rango_3, text = "0",bg="white",fg="blue", font=("Times New Roman",16,"bold"), width=8)
carton_salida_historico_1_rango_3.pack(pady=1)

# Historico_1 rango_4
frame_histortico_1_rango_4 = Frame(marco_historico_1)
frame_histortico_1_rango_4.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_1_rango_4.config(bg="#C0C0C0")

label_historico_1_rango4 = Label(frame_histortico_1_rango_4, text = "RANGO 4",bg="#C0C0C0", font=("Times New Roman",16,"bold"))
label_historico_1_rango4.pack()
label_historico_1_rango4.config(fg="black")

liquidacion_historico_1_rango4 = Label(frame_histortico_1_rango_4, text = "0€",bg="white",fg="#800080",font=("Times New Roman",18,"bold"), width=7)
liquidacion_historico_1_rango4.pack()

Label(frame_histortico_1_rango_4, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_1_rango_4 = Label(frame_histortico_1_rango_4, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=2)
series_histirico_1_rango_4.pack()

carton_salida_historico_1_rango_4 = Label(frame_histortico_1_rango_4, text = "0",bg="white",fg="blue",font=("Times New Roman",16,"bold"), width=8)
carton_salida_historico_1_rango_4.pack(pady=1)

# Historico_1 rango_5
frame_histortico_1_rango_5 = Frame(marco_historico_1)
frame_histortico_1_rango_5.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_1_rango_5.config(bg="gray59")

label_historico_1_rango5 = Label(frame_histortico_1_rango_5, text = "RANGO 5",bg="gray59", font=("Times New Roman",16,"bold"))
label_historico_1_rango5.pack()
label_historico_1_rango5.config(fg="black")

liquidacion_historico_1_rango5 = Label(frame_histortico_1_rango_5, text = "0€",bg="white",fg="#800080",font=("Times New Roman",18,"bold"), width=7)
liquidacion_historico_1_rango5.pack()

Label(frame_histortico_1_rango_5, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_1_rango_5 = Label(frame_histortico_1_rango_5, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=2)
series_histirico_1_rango_5.pack()

carton_salida_historico_1_rango_5 = Label(frame_histortico_1_rango_5, text = "0",bg="white",fg="blue",font=("Times New Roman",16,"bold"), width=8)
carton_salida_historico_1_rango_5.pack(pady=1)

# Historico_1 rango_6
frame_histortico_1_rango_6 = Frame(marco_historico_1)
frame_histortico_1_rango_6.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_1_rango_6.config(bg="#C0C0C0")

label_historico_1_rango6 = Label(frame_histortico_1_rango_6, text = "RANGO 6",bg="#C0C0C0", font=("Times New Roman",16,"bold"))
label_historico_1_rango6.pack()
label_historico_1_rango6.config(fg="black")

liquidacion_historico_1_rango6 = Label(frame_histortico_1_rango_6, text = "0€",bg="white",fg="#800080",font=("Times New Roman",18,"bold"), width=7)
liquidacion_historico_1_rango6.pack()

Label(frame_histortico_1_rango_6, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_1_rango_6 = Label(frame_histortico_1_rango_6, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=2)
series_histirico_1_rango_6.pack()

carton_salida_historico_1_rango_6 = Label(frame_histortico_1_rango_6, text = "0",bg="white",fg="blue",font=("Times New Roman",16,"bold"), width=8)
carton_salida_historico_1_rango_6.pack(pady=1)

# Historico 1 rango_7
frame_histortico_1_rango_7 = Frame(marco_historico_1)
frame_histortico_1_rango_7.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_1_rango_7.config(bg="gray59")

label_historico_1_rango7 = Label(frame_histortico_1_rango_7, text = "RANGO 7",bg="gray59", font=("Times New Roman",16,"bold"))
label_historico_1_rango7.pack()
label_historico_1_rango7.config(fg="black")

liquidacion_historico_1_rango7 = Label(frame_histortico_1_rango_7, text = "0€",bg="white",fg="#800080",font=("Times New Roman",18,"bold"), width=7)
liquidacion_historico_1_rango7.pack()

Label(frame_histortico_1_rango_7, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_1_rango_7 = Label(frame_histortico_1_rango_7, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=2)
series_histirico_1_rango_7.pack()

carton_salida_historico_1_rango_7 = Label(frame_histortico_1_rango_7, text = "0",bg="white",fg="blue",font=("Times New Roman",16,"bold"), width=8)
carton_salida_historico_1_rango_7.pack(pady=1)

# Historico_1 rango_8
frame_histortico_1_rango_8 = Frame(marco_historico_1)
frame_histortico_1_rango_8.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_1_rango_8.config(bg="#C0C0C0")

label_historico_1_rango8 = Label(frame_histortico_1_rango_8, text = "RANGO 8",bg="#C0C0C0", font=("Times New Roman",16,"bold"))
label_historico_1_rango8.pack()
label_historico_1_rango8.config(fg="black")

liquidacion_historico_1_rango8 = Label(frame_histortico_1_rango_8, text = "0€",bg="white",fg="#800080",font=("Times New Roman",18,"bold"), width=7)
liquidacion_historico_1_rango8.pack()

Label(frame_histortico_1_rango_8, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_1_rango_8 = Label(frame_histortico_1_rango_8, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=2)
series_histirico_1_rango_8.pack()

carton_salida_historico_1_rango_8 = Label(frame_histortico_1_rango_8, text = "0",bg="white",fg="blue",font=("Times New Roman",16,"bold"), width=8)
carton_salida_historico_1_rango_8.pack(pady=1)

# Historico_1 rango_9
frame_histortico_1_rango_9 = Frame(marco_historico_1)
frame_histortico_1_rango_9.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_1_rango_9.config(bg="gray59")

label_historico_1_rango9 = Label(frame_histortico_1_rango_9, text = "RANGO 9",bg="gray59", font=("Times New Roman",16,"bold"))
label_historico_1_rango9.pack()
label_historico_1_rango9.config(fg="black")

liquidacion_historico_1_rango9 = Label(frame_histortico_1_rango_9, text = "0€",bg="white",fg="#800080",font=("Times New Roman",18,"bold"), width=7)
liquidacion_historico_1_rango9.pack()

Label(frame_histortico_1_rango_9, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_1_rango_9 = Label(frame_histortico_1_rango_9, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=2)
series_histirico_1_rango_9.pack()

carton_salida_historico_1_rango_9 = Label(frame_histortico_1_rango_9, text = "0",bg="white",fg="blue",font=("Times New Roman",16,"bold"), width=8)
carton_salida_historico_1_rango_9.pack(pady=1)

# Historico 1 Cierre
frame_histortico_1_cierre = Frame(marco_historico_1)
frame_histortico_1_cierre.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_1_cierre.config(bg="#31BFE4")

Label(frame_histortico_1_cierre, text = "CIERRE",bg="#31BFE4", font=("Times New Roman",16,"bold")).pack()

liquidacion_historico_1_cierre = Label(frame_histortico_1_cierre, text = "0€",bg="white",fg="#800080", font=("Times New Roman",18,"bold"),width=7)
liquidacion_historico_1_cierre.pack()

pico_historico_1_cierre = Label(frame_histortico_1_cierre, text = "0" ,fg="blue" ,bg="white", font=("Times New Roman",12,"bold"), width=1)
pico_historico_1_cierre.pack(side=RIGHT,anchor=NW, pady = 30)

Label(frame_histortico_1_cierre, text = "SERIES",bg="#31BFE4", font=("Times New Roman",13,"bold")).pack()

series_historico_1_cierre = Label(frame_histortico_1_cierre, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=2)
series_historico_1_cierre.pack()

carton_salida_historico_1_cierre = Label(frame_histortico_1_cierre, text = "0",bg="white",fg="blue", font=("Times New Roman",16,"bold"), width=8)
carton_salida_historico_1_cierre.pack(pady=1)

# historico 1 total

Frame_historico_1_Total = Frame(marco_historico_1)
Frame_historico_1_Total.pack(expand=True, fill= BOTH, side=LEFT)
Frame_historico_1_Total.config(bg="dodger blue")

Label(Frame_historico_1_Total, text = "TOTAL",bg="dodger blue", font=("Times New Roman",16,"bold")).pack()

liquidacion_historico_1_total = Label(Frame_historico_1_Total, text = "0€",bg="white",fg="#800080", font=("Times New Roman",18,"bold"), width=7)
liquidacion_historico_1_total.pack()

Label(Frame_historico_1_Total, text = "SERIES",bg="dodger blue", font=("Times New Roman",13,"bold")).pack()
total_series_historico_1 = Label(Frame_historico_1_Total, text = "0",bg="white",fg ="blue", font=("Times New Roman",18,"bold"), width=4)
total_series_historico_1.pack()
Label(Frame_historico_1_Total, text = "CARTONES",bg="dodger blue", font=("Times New Roman",8,"bold")).pack()

total_cartones_historico_1 = Label(Frame_historico_1_Total, text = "0",bg="white",fg ="blue", font=("Times New Roman",15,"bold"), width=8)
total_cartones_historico_1.pack(pady=2)

# Medio 1
medio1 = Frame(root)
medio1.config(bg="white")
medio1.pack()
Label(medio1, text="PARTIDAS ANTERIONES",bg="#000099", fg="white", font=("Times New Roman",15,"bold")).pack()

# Historico 2
marco_historico_2 = Frame(root)
marco_historico_2.pack(expand=True, fill= BOTH)
marco_historico_2.config(bg="lightblue")

# Historico_2 rango_1
frame_histortico_2_rango_1 = Frame(marco_historico_2)
frame_histortico_2_rango_1.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_2_rango_1.config(bg="#31BFE4")

pico_salida_historico_2_rango_1 = Label(frame_histortico_2_rango_1, text = "0" ,fg="blue" ,bg="white", font=("Times New Roman",12,"bold"))
pico_salida_historico_2_rango_1.pack(side=RIGHT,anchor=NW, pady = 30)


Label(frame_histortico_2_rango_1, text = "SERIES",bg="#31BFE4", font=("Times New Roman",13,"bold")).pack()

series_histirico_2_rango_1 = Label(frame_histortico_2_rango_1, text = "0", bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_histirico_2_rango_1.pack()

carton_salida_historico_2_rango_1 = Label(frame_histortico_2_rango_1, text = "0", background="white",foreground="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_2_rango_1.pack(pady=1)

# Historico_2 rango_2
frame_histortico_2_rango_2 = Frame(marco_historico_2)
frame_histortico_2_rango_2.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_2_rango_2.config(bg="#C0C0C0")

Label(frame_histortico_2_rango_2, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_2_rango_2 = Label(frame_histortico_2_rango_2, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_histirico_2_rango_2.pack()

carton_salida_historico_2_rango_2 = Label(frame_histortico_2_rango_2, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_2_rango_2.pack(pady=1)

Label(frame_histortico_2_rango_2, text= "", bg="#C0C0C0", font=("Times New Roman",1),width=5).pack()

# Historico 2 rango_3
frame_histortico_2_rango_3 = Frame(marco_historico_2)
frame_histortico_2_rango_3.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_2_rango_3.config(bg="gray59")

Label(frame_histortico_2_rango_3, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_2_rango_3 = Label(frame_histortico_2_rango_3, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_histirico_2_rango_3.pack()

carton_salida_historico_2_rango_3 = Label(frame_histortico_2_rango_3, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_2_rango_3.pack(pady=1)

# Historico 2 rango_4
frame_histortico_2_rango_4 = Frame(marco_historico_2)
frame_histortico_2_rango_4.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_2_rango_4.config(bg="#C0C0C0")

Label(frame_histortico_2_rango_4, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_2_rango_4 = Label(frame_histortico_2_rango_4, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_2_rango_4.pack()

carton_salida_historico_2_rango_4 = Label(frame_histortico_2_rango_4, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_2_rango_4.pack(pady=1)

# Historico 2 rango_5
frame_histortico_2_rango_5 = Frame(marco_historico_2)
frame_histortico_2_rango_5.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_2_rango_5.config(bg="gray59")

Label(frame_histortico_2_rango_5, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_2_rango_5 = Label(frame_histortico_2_rango_5, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_2_rango_5.pack()

carton_salida_historico_2_rango_5 = Label(frame_histortico_2_rango_5, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_2_rango_5.pack(pady=1)

# Historico 2 rango_6
frame_histortico_2_rango_6 = Frame(marco_historico_2)
frame_histortico_2_rango_6.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_2_rango_6.config(bg="#C0C0C0")

Label(frame_histortico_2_rango_6, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_2_rango_6 = Label(frame_histortico_2_rango_6, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_2_rango_6.pack()

carton_salida_historico_2_rango_6 = Label(frame_histortico_2_rango_6, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_2_rango_6.pack(pady=1)

# Historico_2 rango_7
frame_histortico_2_rango_7 = Frame(marco_historico_2)
frame_histortico_2_rango_7.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_2_rango_7.config(bg="gray59")

Label(frame_histortico_2_rango_7, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_2_rango_7 = Label(frame_histortico_2_rango_7, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_2_rango_7.pack()

carton_salida_historico_2_rango_7 = Label(frame_histortico_2_rango_7, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_2_rango_7.pack(pady=1)

# Historico_2 rango_8
frame_histortico_2_rango_8 = Frame(marco_historico_2)
frame_histortico_2_rango_8.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_2_rango_8.config(bg="#C0C0C0")

Label(frame_histortico_2_rango_8, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_2_rango_8 = Label(frame_histortico_2_rango_8, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_2_rango_8.pack()

carton_salida_historico_2_rango_8 = Label(frame_histortico_2_rango_8, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_2_rango_8.pack(pady=1)

# Historico_2 rango_9
frame_histortico_2_rango_9 = Frame(marco_historico_2)
frame_histortico_2_rango_9.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_2_rango_9.config(bg="gray59")

Label(frame_histortico_2_rango_9, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_2_rango_9 = Label(frame_histortico_2_rango_9, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_2_rango_9.pack()

carton_salida_historico_2_rango_9 = Label(frame_histortico_2_rango_9, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_2_rango_9.pack(pady=1)

# Historico 2 Cierre
frame_histortico_2_cierre = Frame(marco_historico_2)
frame_histortico_2_cierre.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_2_cierre.config(bg="#31BFE4")

pico_historico_2_cierre = Label(frame_histortico_2_cierre, text = "0" ,fg="blue" ,bg="white", font=("Times New Roman",12,"bold"), width=1)
pico_historico_2_cierre.pack(side=RIGHT,anchor=NW, pady = 30)

Label(frame_histortico_2_cierre, text = "SERIES",bg="#31BFE4", font=("Times New Roman",13,"bold")).pack()

series_historico_2_cierre = Label(frame_histortico_2_cierre, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_historico_2_cierre.pack()

carton_salida_historico_2_cierre = Label(frame_histortico_2_cierre, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_2_cierre.pack(pady=1)

# historico 2 liquidacion

Frame_historico_2_Total = Frame(marco_historico_2)
Frame_historico_2_Total.pack(expand=True, fill= BOTH, side=LEFT)
Frame_historico_2_Total.config(bg="dodger blue")

Label(Frame_historico_2_Total, text = "SERIES",bg="dodger blue", font=("Times New Roman",13,"bold")).pack()
total_series_historico_2 = Label(Frame_historico_2_Total, text = "0",bg="white",fg ="blue", font=("Times New Roman",22,"bold"), width=4)
total_series_historico_2.pack()
Label(Frame_historico_2_Total, text = "CARTONES",bg="dodger blue", font=("Times New Roman",8,"bold")).pack()

total_cartones_historico_2 = Label(Frame_historico_2_Total, text = "0",bg="white",fg ="blue", font=("Times New Roman",15,"bold"), width=8)
total_cartones_historico_2.pack(pady=2)

# Medio 2
medio2 = Frame(root)
medio2.config(bg="white")
medio2.pack()
Label(medio2, text="",bg="#000099", font=("Times New Roman",2,"bold")).pack()#, font=("Times New Roman",5,"bold")

# Historico 3
marco_historico_3 = Frame(root)
marco_historico_3.pack(expand=True, fill= BOTH)
marco_historico_3.config(bg="lightblue")

# Historico_3 rango_1
frame_histortico_3_rango_1 = Frame(marco_historico_3)
frame_histortico_3_rango_1.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_3_rango_1.config(bg="#31BFE4")

pico_salida_historico_3_rango_1 = Label(frame_histortico_3_rango_1, text = "0" ,fg="blue" ,bg="white", font=("Times New Roman",12,"bold"))
pico_salida_historico_3_rango_1.pack(side=RIGHT,anchor=NW, pady = 30)

Label(frame_histortico_3_rango_1, text = "SERIES",bg="#31BFE4", font=("Times New Roman",13,"bold")).pack()

series_histirico_3_rango_1 = Label(frame_histortico_3_rango_1, text = "0", bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_histirico_3_rango_1.pack()

carton_salida_historico_3_rango_1 = Label(frame_histortico_3_rango_1, text = "0", background="white",foreground="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_3_rango_1.pack(pady=1)

# Historico_3 rango_2
frame_histortico_3_rango_2 = Frame(marco_historico_3)
frame_histortico_3_rango_2.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_3_rango_2.config(bg="#C0C0C0")

Label(frame_histortico_3_rango_2, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_3_rango_2 = Label(frame_histortico_3_rango_2, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_histirico_3_rango_2.pack()

carton_salida_historico_3_rango_2 = Label(frame_histortico_3_rango_2, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_3_rango_2.pack(pady=1)

Label(frame_histortico_3_rango_2, text= "", bg="#C0C0C0", font=("Times New Roman",1),width=5).pack()

# Historico 3 rango_3
frame_histortico_3_rango_3 = Frame(marco_historico_3)
frame_histortico_3_rango_3.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_3_rango_3.config(bg="gray59")

Label(frame_histortico_3_rango_3, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_3_rango_3 = Label(frame_histortico_3_rango_3, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_histirico_3_rango_3.pack()

carton_salida_historico_3_rango_3 = Label(frame_histortico_3_rango_3, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_3_rango_3.pack(pady=1)

# Historico 3 rango_4
frame_histortico_3_rango_4 = Frame(marco_historico_3)
frame_histortico_3_rango_4.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_3_rango_4.config(bg="#C0C0C0")

Label(frame_histortico_3_rango_4, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_3_rango_4 = Label(frame_histortico_3_rango_4, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_3_rango_4.pack()

carton_salida_historico_3_rango_4 = Label(frame_histortico_3_rango_4, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_3_rango_4.pack(pady=1)

# Historico 3 rango_5
frame_histortico_3_rango_5 = Frame(marco_historico_3)
frame_histortico_3_rango_5.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_3_rango_5.config(bg="gray59")

Label(frame_histortico_3_rango_5, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_3_rango_5 = Label(frame_histortico_3_rango_5, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_3_rango_5.pack()

carton_salida_historico_3_rango_5 = Label(frame_histortico_3_rango_5, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_3_rango_5.pack(pady=1)

# Historico 3 rango_6
frame_histortico_3_rango_6 = Frame(marco_historico_3)
frame_histortico_3_rango_6.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_3_rango_6.config(bg="#C0C0C0")

Label(frame_histortico_3_rango_6, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_3_rango_6 = Label(frame_histortico_3_rango_6, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_3_rango_6.pack()

carton_salida_historico_3_rango_6 = Label(frame_histortico_3_rango_6, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_3_rango_6.pack(pady=1)

# Historico_3 rango_7
frame_histortico_3_rango_7 = Frame(marco_historico_3)
frame_histortico_3_rango_7.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_3_rango_7.config(bg="gray59")

Label(frame_histortico_3_rango_7, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_3_rango_7 = Label(frame_histortico_3_rango_7, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_3_rango_7.pack()

carton_salida_historico_3_rango_7 = Label(frame_histortico_3_rango_7, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_3_rango_7.pack(pady=1)

# Historico_3 rango_8
frame_histortico_3_rango_8 = Frame(marco_historico_3)
frame_histortico_3_rango_8.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_3_rango_8.config(bg="#C0C0C0")

Label(frame_histortico_3_rango_8, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_3_rango_8 = Label(frame_histortico_3_rango_8, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_3_rango_8.pack()

carton_salida_historico_3_rango_8 = Label(frame_histortico_3_rango_8, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_3_rango_8.pack(pady=1)

# Historico_3 rango_9
frame_histortico_3_rango_9 = Frame(marco_historico_3)
frame_histortico_3_rango_9.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_3_rango_9.config(bg="gray59")

Label(frame_histortico_3_rango_9, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_3_rango_9 = Label(frame_histortico_3_rango_9, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_3_rango_9.pack()

carton_salida_historico_3_rango_9 = Label(frame_histortico_3_rango_9, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_3_rango_9.pack(pady=1)

# Historico 3 Cierre
frame_histortico_3_cierre = Frame(marco_historico_3)
frame_histortico_3_cierre.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_3_cierre.config(bg="#31BFE4")

pico_historico_3_cierre = Label(frame_histortico_3_cierre, text = "0" ,fg="blue" ,bg="white", font=("Times New Roman",12,"bold"), width=1)
pico_historico_3_cierre.pack(side=RIGHT,anchor=NW, pady = 30)

Label(frame_histortico_3_cierre, text = "SERIES",bg="#31BFE4", font=("Times New Roman",13,"bold")).pack()

series_historico_3_cierre = Label(frame_histortico_3_cierre, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_historico_3_cierre.pack()

carton_salida_historico_3_cierre = Label(frame_histortico_3_cierre, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_3_cierre.pack(pady=1)

# historico 3 liquidacion

Frame_historico_3_Total = Frame(marco_historico_3)
Frame_historico_3_Total.pack(expand=True, fill= BOTH, side=LEFT)
Frame_historico_3_Total.config(bg="dodger blue")

Label(Frame_historico_3_Total, text = "SERIES",bg="dodger blue", font=("Times New Roman",13,"bold")).pack()
total_series_historico_3 = Label(Frame_historico_3_Total, text = "0",bg="white",fg ="blue", font=("Times New Roman",22,"bold"), width=4)
total_series_historico_3.pack()
Label(Frame_historico_3_Total, text = "CARTONES",bg="dodger blue", font=("Times New Roman",8,"bold")).pack()

total_cartones_historico_3 = Label(Frame_historico_3_Total, text = "0",bg="white",fg ="blue", font=("Times New Roman",15,"bold"), width=8)
total_cartones_historico_3.pack(pady=2)

# Medio 3
medio3 = Frame(root)
medio3.config(bg="white")
medio3.pack()
Label(medio3, text="",bg="#000099", font=("Times New Roman",2,"bold")).pack()

# Historico 4
marco_historico_4 = Frame(root)
marco_historico_4.pack(expand=True, fill= BOTH)
marco_historico_4.config(bg="lightblue")

# Historico_4 rango_1
frame_histortico_4_rango_1 = Frame(marco_historico_4)
frame_histortico_4_rango_1.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_4_rango_1.config(bg="#31BFE4")

pico_salida_historico_4_rango_1 = Label(frame_histortico_4_rango_1, text = "0" ,fg="blue" ,bg="white", font=("Times New Roman",12,"bold"))
pico_salida_historico_4_rango_1.pack(side=RIGHT,anchor=NW, pady = 30)


Label(frame_histortico_4_rango_1, text = "SERIES",bg="#31BFE4", font=("Times New Roman",13,"bold")).pack()

series_histirico_4_rango_1 = Label(frame_histortico_4_rango_1, text = "0", bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_histirico_4_rango_1.pack()

carton_salida_historico_4_rango_1 = Label(frame_histortico_4_rango_1, text = "0", background="white",foreground="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_4_rango_1.pack(pady=1)

# Historico_4 rango_2
frame_histortico_4_rango_2 = Frame(marco_historico_4)
frame_histortico_4_rango_2.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_4_rango_2.config(bg="#C0C0C0")

Label(frame_histortico_4_rango_2, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_4_rango_2 = Label(frame_histortico_4_rango_2, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_histirico_4_rango_2.pack()

carton_salida_historico_4_rango_2 = Label(frame_histortico_4_rango_2, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_4_rango_2.pack(pady=1)

Label(frame_histortico_4_rango_2, text= "", bg="#C0C0C0", font=("Times New Roman",1),width=5).pack()

# Historico 4 rango_3
frame_histortico_4_rango_3 = Frame(marco_historico_4)
frame_histortico_4_rango_3.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_4_rango_3.config(bg="gray59")

Label(frame_histortico_4_rango_3, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_4_rango_3 = Label(frame_histortico_4_rango_3, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_histirico_4_rango_3.pack()

carton_salida_historico_4_rango_3 = Label(frame_histortico_4_rango_3, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_4_rango_3.pack(pady=1)

# Historico 4 rango_4
frame_histortico_4_rango_4 = Frame(marco_historico_4)
frame_histortico_4_rango_4.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_4_rango_4.config(bg="#C0C0C0")

Label(frame_histortico_4_rango_4, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_4_rango_4 = Label(frame_histortico_4_rango_4, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_4_rango_4.pack()

carton_salida_historico_4_rango_4 = Label(frame_histortico_4_rango_4, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_4_rango_4.pack(pady=1)

# Historico 4 rango_5
frame_histortico_4_rango_5 = Frame(marco_historico_4)
frame_histortico_4_rango_5.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_4_rango_5.config(bg="gray59")

Label(frame_histortico_4_rango_5, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_4_rango_5 = Label(frame_histortico_4_rango_5, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_4_rango_5.pack()

carton_salida_historico_4_rango_5 = Label(frame_histortico_4_rango_5, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_4_rango_5.pack(pady=1)

# Historico 4 rango_6
frame_histortico_4_rango_6 = Frame(marco_historico_4)
frame_histortico_4_rango_6.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_4_rango_6.config(bg="#C0C0C0")

Label(frame_histortico_4_rango_6, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_4_rango_6 = Label(frame_histortico_4_rango_6, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_4_rango_6.pack()

carton_salida_historico_4_rango_6 = Label(frame_histortico_4_rango_6, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_4_rango_6.pack(pady=1)

# Historico_4 rango_7
frame_histortico_4_rango_7 = Frame(marco_historico_4)
frame_histortico_4_rango_7.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_4_rango_7.config(bg="gray59")

Label(frame_histortico_4_rango_7, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_4_rango_7 = Label(frame_histortico_4_rango_7, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_4_rango_7.pack()

carton_salida_historico_4_rango_7 = Label(frame_histortico_4_rango_7, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_4_rango_7.pack(pady=1)

# Historico_4 rango_8
frame_histortico_4_rango_8 = Frame(marco_historico_4)
frame_histortico_4_rango_8.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_4_rango_8.config(bg="#C0C0C0")

Label(frame_histortico_4_rango_8, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_4_rango_8 = Label(frame_histortico_4_rango_8, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_4_rango_8.pack()

carton_salida_historico_4_rango_8 = Label(frame_histortico_4_rango_8, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_4_rango_8.pack(pady=1)

# Historico_4 rango_9
frame_histortico_4_rango_9 = Frame(marco_historico_4)
frame_histortico_4_rango_9.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_4_rango_9.config(bg="gray59")

Label(frame_histortico_4_rango_9, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_4_rango_9 = Label(frame_histortico_4_rango_9, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_4_rango_9.pack()

carton_salida_historico_4_rango_9 = Label(frame_histortico_4_rango_9, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_4_rango_9.pack(pady=1)

# Historico 4 Cierre
frame_histortico_4_cierre = Frame(marco_historico_4)
frame_histortico_4_cierre.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_4_cierre.config(bg="#31BFE4")

pico_historico_4_cierre = Label(frame_histortico_4_cierre, text = "0" ,fg="blue" ,bg="white", font=("Times New Roman",12,"bold"), width=1)
pico_historico_4_cierre.pack(side=RIGHT,anchor=NW, pady = 30)

Label(frame_histortico_4_cierre, text = "SERIES",bg="#31BFE4", font=("Times New Roman",13,"bold")).pack()

series_historico_4_cierre = Label(frame_histortico_4_cierre, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_historico_4_cierre.pack()

carton_salida_historico_4_cierre = Label(frame_histortico_4_cierre, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_4_cierre.pack(pady=1)

# historico 4 liquidacion

Frame_historico_4_Total = Frame(marco_historico_4)
Frame_historico_4_Total.pack(expand=True, fill= BOTH, side=LEFT)
Frame_historico_4_Total.config(bg="dodger blue")

Label(Frame_historico_4_Total, text = "SERIES",bg="dodger blue", font=("Times New Roman",13,"bold")).pack()
total_series_historico_4 = Label(Frame_historico_4_Total, text = "0",bg="white",fg ="blue", font=("Times New Roman",22,"bold"), width=4)
total_series_historico_4.pack()
Label(Frame_historico_4_Total, text = "CARTONES",bg="dodger blue", font=("Times New Roman",8,"bold")).pack()

total_cartones_historico_4 = Label(Frame_historico_4_Total, text = "0",bg="white",fg ="blue", font=("Times New Roman",15,"bold"), width=8)
total_cartones_historico_4.pack(pady=2)

# Medio 4
medio4 = Frame(root)
medio4.config(bg="white")
medio4.pack()
Label(medio4, text="",bg="#000099", font=("Times New Roman",2,"bold")).pack()

# Historico 5
marco_historico_5 = Frame(root)
marco_historico_5.pack(expand=True, fill= BOTH)
marco_historico_5.config(bg="lightblue")

# Historico_5 rango_1
frame_histortico_5_rango_1 = Frame(marco_historico_5)
frame_histortico_5_rango_1.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_5_rango_1.config(bg="#31BFE4")

pico_salida_historico_5_rango_1 = Label(frame_histortico_5_rango_1, text = "0" ,fg="blue" ,bg="white", font=("Times New Roman",12,"bold"))
pico_salida_historico_5_rango_1.pack(side=RIGHT,anchor=NW, pady = 30)


Label(frame_histortico_5_rango_1, text = "SERIES",bg="#31BFE4", font=("Times New Roman",13,"bold")).pack()

series_histirico_5_rango_1 = Label(frame_histortico_5_rango_1, text = "0", bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_histirico_5_rango_1.pack()

carton_salida_historico_5_rango_1 = Label(frame_histortico_5_rango_1, text = "0", background="white",foreground="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_5_rango_1.pack(pady=1)

# Historico_5 rango_2
frame_histortico_5_rango_2 = Frame(marco_historico_5)
frame_histortico_5_rango_2.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_5_rango_2.config(bg="#C0C0C0")

Label(frame_histortico_5_rango_2, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_5_rango_2 = Label(frame_histortico_5_rango_2, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_histirico_5_rango_2.pack()

carton_salida_historico_5_rango_2 = Label(frame_histortico_5_rango_2, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_5_rango_2.pack(pady=1)

Label(frame_histortico_5_rango_2, text= "", bg="#C0C0C0", font=("Times New Roman",1),width=5).pack()

# Historico 5 rango_3
frame_histortico_5_rango_3 = Frame(marco_historico_5)
frame_histortico_5_rango_3.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_5_rango_3.config(bg="gray59")

Label(frame_histortico_5_rango_3, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_5_rango_3 = Label(frame_histortico_5_rango_3, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_histirico_5_rango_3.pack()

carton_salida_historico_5_rango_3 = Label(frame_histortico_5_rango_3, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_5_rango_3.pack(pady=1)

# Historico 5 rango_4
frame_histortico_5_rango_4 = Frame(marco_historico_5)
frame_histortico_5_rango_4.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_5_rango_4.config(bg="#C0C0C0")

Label(frame_histortico_5_rango_4, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_5_rango_4 = Label(frame_histortico_5_rango_4, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_5_rango_4.pack()

carton_salida_historico_5_rango_4 = Label(frame_histortico_5_rango_4, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_5_rango_4.pack(pady=1)

# Historico 5 rango_5
frame_histortico_5_rango_5 = Frame(marco_historico_5)
frame_histortico_5_rango_5.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_5_rango_5.config(bg="gray59")

Label(frame_histortico_5_rango_5, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_5_rango_5 = Label(frame_histortico_5_rango_5, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_5_rango_5.pack()

carton_salida_historico_5_rango_5 = Label(frame_histortico_5_rango_5, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_5_rango_5.pack(pady=1)

# Historico 5 rango_6
frame_histortico_5_rango_6 = Frame(marco_historico_5)
frame_histortico_5_rango_6.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_5_rango_6.config(bg="#C0C0C0")

Label(frame_histortico_5_rango_6, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_5_rango_6 = Label(frame_histortico_5_rango_6, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_5_rango_6.pack()

carton_salida_historico_5_rango_6 = Label(frame_histortico_5_rango_6, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_5_rango_6.pack(pady=1)

# Historico_5 rango_7
frame_histortico_5_rango_7 = Frame(marco_historico_5)
frame_histortico_5_rango_7.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_5_rango_7.config(bg="gray59")

Label(frame_histortico_5_rango_7, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_5_rango_7 = Label(frame_histortico_5_rango_7, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_5_rango_7.pack()

carton_salida_historico_5_rango_7 = Label(frame_histortico_5_rango_7, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_5_rango_7.pack(pady=1)

# Historico_5 rango_8
frame_histortico_5_rango_8 = Frame(marco_historico_5)
frame_histortico_5_rango_8.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_5_rango_8.config(bg="#C0C0C0")

Label(frame_histortico_5_rango_8, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_5_rango_8 = Label(frame_histortico_5_rango_8, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_5_rango_8.pack()

carton_salida_historico_5_rango_8 = Label(frame_histortico_5_rango_8, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_5_rango_8.pack(pady=1)

# Historico_5 rango_9
frame_histortico_5_rango_9 = Frame(marco_historico_5)
frame_histortico_5_rango_9.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_5_rango_9.config(bg="gray59")

Label(frame_histortico_5_rango_9, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_5_rango_9 = Label(frame_histortico_5_rango_9, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_5_rango_9.pack()

carton_salida_historico_5_rango_9 = Label(frame_histortico_5_rango_9, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_5_rango_9.pack(pady=1)

# Historico 5 Cierre
frame_histortico_5_cierre = Frame(marco_historico_5)
frame_histortico_5_cierre.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_5_cierre.config(bg="#31BFE4")

pico_historico_5_cierre = Label(frame_histortico_5_cierre, text = "0" ,fg="blue" ,bg="white", font=("Times New Roman",12,"bold"), width=1)
pico_historico_5_cierre.pack(side=RIGHT,anchor=NW, pady = 30)

Label(frame_histortico_5_cierre, text = "SERIES",bg="#31BFE4", font=("Times New Roman",13,"bold")).pack()

series_historico_5_cierre = Label(frame_histortico_5_cierre, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_historico_5_cierre.pack()

carton_salida_historico_5_cierre = Label(frame_histortico_5_cierre, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_5_cierre.pack(pady=1)

# historico 5 liquidacion

Frame_historico_5_Total = Frame(marco_historico_5)
Frame_historico_5_Total.pack(expand=True, fill= BOTH, side=LEFT)
Frame_historico_5_Total.config(bg="dodger blue")

Label(Frame_historico_5_Total, text = "SERIES",bg="dodger blue", font=("Times New Roman",13,"bold")).pack()
total_series_historico_5 = Label(Frame_historico_5_Total, text = "0",bg="white",fg ="blue", font=("Times New Roman",22,"bold"), width=4)
total_series_historico_5.pack()
Label(Frame_historico_5_Total, text = "CARTONES",bg="dodger blue", font=("Times New Roman",8,"bold")).pack()

total_cartones_historico_5 = Label(Frame_historico_5_Total, text = "0",bg="white",fg ="blue", font=("Times New Roman",15,"bold"), width=8)
total_cartones_historico_5.pack(pady=2)

# Medio 5
medio5 = Frame(root)
medio5.config(bg="white")
medio5.pack()
Label(medio5, text="",bg="#000099", font=("Times New Roman",2,"bold")).pack()

# Historico 6
marco_historico_6 = Frame(root)
marco_historico_6.pack(expand=True, fill= BOTH)
marco_historico_6.config(bg="lightblue")

# Historico_6 rango_1
frame_histortico_6_rango_1 = Frame(marco_historico_6)
frame_histortico_6_rango_1.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_6_rango_1.config(bg="#31BFE4")

pico_salida_historico_6_rango_1 = Label(frame_histortico_6_rango_1, text = "0" ,fg="blue" ,bg="white", font=("Times New Roman",12,"bold"))
pico_salida_historico_6_rango_1.pack(side=RIGHT,anchor=NW, pady = 30)


Label(frame_histortico_6_rango_1, text = "SERIES",bg="#31BFE4", font=("Times New Roman",13,"bold")).pack()

series_histirico_6_rango_1 = Label(frame_histortico_6_rango_1, text = "0", bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_histirico_6_rango_1.pack()

carton_salida_historico_6_rango_1 = Label(frame_histortico_6_rango_1, text = "0", background="white",foreground="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_6_rango_1.pack(pady=1)

# Historico_6 rango_2
frame_histortico_6_rango_2 = Frame(marco_historico_6)
frame_histortico_6_rango_2.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_6_rango_2.config(bg="#C0C0C0")

Label(frame_histortico_6_rango_2, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_6_rango_2 = Label(frame_histortico_6_rango_2, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_histirico_6_rango_2.pack()

carton_salida_historico_6_rango_2 = Label(frame_histortico_6_rango_2, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_6_rango_2.pack(pady=1)

Label(frame_histortico_6_rango_2, text= "", bg="#C0C0C0", font=("Times New Roman",1),width=5).pack()

# Historico 6 rango_3
frame_histortico_6_rango_3 = Frame(marco_historico_6)
frame_histortico_6_rango_3.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_6_rango_3.config(bg="gray59")

Label(frame_histortico_6_rango_3, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_6_rango_3 = Label(frame_histortico_6_rango_3, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_histirico_6_rango_3.pack()

carton_salida_historico_6_rango_3 = Label(frame_histortico_6_rango_3, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_6_rango_3.pack(pady=1)

# Historico 6 rango_4
frame_histortico_6_rango_4 = Frame(marco_historico_6)
frame_histortico_6_rango_4.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_6_rango_4.config(bg="#C0C0C0")

Label(frame_histortico_6_rango_4, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_6_rango_4 = Label(frame_histortico_6_rango_4, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_6_rango_4.pack()

carton_salida_historico_6_rango_4 = Label(frame_histortico_6_rango_4, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_6_rango_4.pack(pady=1)

# Historico 6 rango_5
frame_histortico_6_rango_5 = Frame(marco_historico_6)
frame_histortico_6_rango_5.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_6_rango_5.config(bg="gray59")

Label(frame_histortico_6_rango_5, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_6_rango_5 = Label(frame_histortico_6_rango_5, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_6_rango_5.pack()

carton_salida_historico_6_rango_5 = Label(frame_histortico_6_rango_5, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_6_rango_5.pack(pady=1)

# Historico 6 rango_6
frame_histortico_6_rango_6 = Frame(marco_historico_6)
frame_histortico_6_rango_6.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_6_rango_6.config(bg="#C0C0C0")

Label(frame_histortico_6_rango_6, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_6_rango_6 = Label(frame_histortico_6_rango_6, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_6_rango_6.pack()

carton_salida_historico_6_rango_6 = Label(frame_histortico_6_rango_6, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_6_rango_6.pack(pady=1)

# Historico 6 rango_7
frame_histortico_6_rango_7 = Frame(marco_historico_6)
frame_histortico_6_rango_7.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_6_rango_7.config(bg="gray59")

Label(frame_histortico_6_rango_7, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_6_rango_7 = Label(frame_histortico_6_rango_7, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_6_rango_7.pack()

carton_salida_historico_6_rango_7 = Label(frame_histortico_6_rango_7, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_6_rango_7.pack(pady=1)

# Historico 6 rango_8
frame_histortico_6_rango_8 = Frame(marco_historico_6)
frame_histortico_6_rango_8.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_6_rango_8.config(bg="#C0C0C0")

Label(frame_histortico_6_rango_8, text = "SERIES",bg="#C0C0C0", font=("Times New Roman",13,"bold")).pack()

series_histirico_6_rango_8 = Label(frame_histortico_6_rango_8, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_6_rango_8.pack()

carton_salida_historico_6_rango_8 = Label(frame_histortico_6_rango_8, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_6_rango_8.pack(pady=1)

# Historico 6 rango_9
frame_histortico_6_rango_9 = Frame(marco_historico_6)
frame_histortico_6_rango_9.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_6_rango_9.config(bg="gray59")

Label(frame_histortico_6_rango_9, text = "SERIES",bg="gray59", font=("Times New Roman",13,"bold")).pack()

series_histirico_6_rango_9 = Label(frame_histortico_6_rango_9, text = "0",bg="white",fg="blue",font=("Times New Roman",22,"bold"), width=2)
series_histirico_6_rango_9.pack()

carton_salida_historico_6_rango_9 = Label(frame_histortico_6_rango_9, text = "0",bg="white",fg="blue",font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_6_rango_9.pack(pady=1)

# Historico 6 Cierre
frame_histortico_6_cierre = Frame(marco_historico_6)
frame_histortico_6_cierre.pack(expand=True, fill= BOTH, side=LEFT)
frame_histortico_6_cierre.config(bg="#31BFE4")

pico_historico_6_cierre = Label(frame_histortico_6_cierre, text = "0" ,fg="blue" ,bg="white", font=("Times New Roman",12,"bold"), width=1)
pico_historico_6_cierre.pack(side=RIGHT,anchor=NW, pady = 30)

Label(frame_histortico_6_cierre, text = "SERIES",bg="#31BFE4", font=("Times New Roman",13,"bold")).pack()

series_historico_6_cierre = Label(frame_histortico_6_cierre, text = "0",bg="white",fg="blue", font=("Times New Roman",22,"bold"), width=2)
series_historico_6_cierre.pack()

carton_salida_historico_6_cierre = Label(frame_histortico_6_cierre, text = "0",bg="white",fg="blue", font=("Times New Roman",18,"bold"), width=8)
carton_salida_historico_6_cierre.pack(pady=1)

# historico 6 liquidacion

Frame_historico_6_Total = Frame(marco_historico_6)
Frame_historico_6_Total.pack(expand=True, fill= BOTH, side=LEFT)
Frame_historico_6_Total.config(bg="dodger blue")

Label(Frame_historico_6_Total, text = "SERIES",bg="dodger blue", font=("Times New Roman",8,"bold")).pack()
total_series_historico_6 = Label(Frame_historico_6_Total, text = "0",bg="white",fg ="blue", font=("Times New Roman",22,"bold"), width=4)
total_series_historico_6.pack()
Label(Frame_historico_6_Total, text = "CARTONES",bg="dodger blue", font=("Times New Roman",8,"bold")).pack()

total_cartones_historico_6 = Label(Frame_historico_6_Total, text = "0",bg="white",fg ="blue", font=("Times New Roman",15,"bold"), width=8)
total_cartones_historico_6.pack(pady=2)

# Medio 6
medio6 = Frame(root)
medio6.config(bg="white")
medio6.pack()
Label(medio6, text="",bg="#000099", font=("Times New Roman",2,"bold")).pack()

# boton cierra ventana historico
boton_cerrar = Button(root, text="Cerrar", command=poner_al_frente_raiz, bg="Red", fg ="#F0F8FF", padx = 30, pady = 4, font=("Times New Roman", 14,"bold"),cursor="hand2", width=6, height=1)
boton_cerrar.pack(pady=5)#lambda: poner_al_frente(raiz)

SalidaEntry_1.focus_set()

#-------------------- memoria--------------------------------
def escribir_memoria():
	global valor1; global valor2; global valor3; global valor4; global valor5; global valor6; global valor7; global valor8;  global valor9
	try:
	    with open("memoria.txt", "r") as archivo:
	        lineas = archivo.readlines()
	        dato1 = (lineas[0].strip() if len(lineas) >= 1 else "")
	        dato2 = (lineas[1].strip() if len(lineas) >= 2 else "")
	        dato3 = (lineas[2].strip() if len(lineas) >= 3 else "")
	        dato4 = (lineas[3].strip() if len(lineas) >= 4 else "")
	        dato5 = (lineas[4].strip() if len(lineas) >= 5 else "")
	        dato6 = (lineas[5].strip() if len(lineas) >= 6 else "")
	        dato7 = (lineas[6].strip() if len(lineas) >= 7 else "")
	        dato8 = (lineas[7].strip() if len(lineas) >= 8 else "")
	        dato9 = (lineas[8].strip() if len(lineas) >= 9 else "")
	        dato10 = (lineas[9].strip() if len(lineas) >= 10 else "")
	        dato11 = (lineas[10].strip() if len(lineas) >= 11 else "")
	        dato12 = (lineas[11].strip() if len(lineas) >= 12 else "")
	        dato13 = (lineas[12].strip() if len(lineas) >= 13 else "")
	        dato14 = (lineas[13].strip() if len(lineas) >= 14 else "")
	        dato15 = (lineas[14].strip() if len(lineas) >= 15 else "")
	        dato16 = (lineas[15].strip() if len(lineas) >= 16 else "")
	        dato17 = (lineas[16].strip() if len(lineas) >= 17 else "")
	        dato18 = (lineas[17].strip() if len(lineas) >= 18 else "")

	        numero_series_rango1.config(text=int(dato1))
	        numero_series_rango2.config(text=int(dato2))
	        numero_series_rango3.config(text=int(dato3))
	        numero_series_rango4.config(text=int(dato4))
	        numero_series_rango5.config(text=int(dato5))
	        numero_series_rango6.config(text=int(dato6))
	        numero_series_rango7.config(text=int(dato7))
	        numero_series_rango8.config(text=int(dato8))
	        numero_series_rango9.config(text=int(dato9))
	        
	        valor1 = int(dato10)
	        valor2 = int(dato11)
	        valor3 = int(dato12)
	        valor4 = int(dato13)
	        valor5 = int(dato14)
	        valor6 = int(dato15)
	        valor7 = int(dato16)
	        valor8 = int(dato17)
	        valor9 = int(dato18)
	        numero_series1.config(text=valor1)
	        numero_series2.config(text=valor2)
	        numero_series3.config(text=valor3)
	        numero_series4.config(text=valor4)
	        numero_series5.config(text=valor5)
	        numero_series6.config(text=valor6)
	        numero_series7.config(text=valor7)
	        numero_series8.config(text=valor8)
	        numero_series9.config(text=valor9)
	except FileNotFoundError:
	    pass
escribir_memoria()
raiz.mainloop()  