from utils import Utils
from rfid import RFID_Controller
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
import sys,time
import lcd_kp as lcd



if __name__=="__main__":
	tools=Utils()
	rfid_tag=RFID_Controller()
	current_tag=0
	while(1):
		while(current_tag==rfid_tag.last_tag):
			time.sleep(0.1)

		current_tag=rfid_tag.last_tag
		print "Cambio el tag!:%s" % current_tag 

		#Verificar si el tag es valido
		tag_valido=tools.tag_valido(current_tag)
		#tag_valido=urllib2.urlopen("http://example.com/foo/bar").read()
		lcd.lcd_clean()
        lcd.lcd_string("User Id:")
        lcd.lcd_goto(2,0)
        lcd.lcd_string(current_tag)
		if tag_valido: #(string del camilo)
			#Obtener la informacion del usuario (nombre,saldo,tipo_usuario)
			#imprimir que debe ingresar la cantidad a utilizar
			cantidad=int(raw_input("Ingrese la cantidad:"))

			#Ingresar el cupon
			print ("Tienes Cupon?")
			print ("1. Si, 2. No")
			tiene_cupon=int(raw_input())
			if tiene_cupon==1:
				tools.menu_cupon(cantidad)
			#Levantar el hostapd con la clave generada por la aplicacion


		#
		#Se crea la variable con toda la configuracion a escribir en hostapd
		#Escribimos el archivo
	# print("Press Enter to quit...")

	# chr = sys.stdin.read(1)
	# print("Cerrando...")

	

	# print("Listo!.")
	# exit(0)
	#tools.clock(60)
	# try:
	# 	tools.hostapd('restart')
		
	# except:
	# 	print "Error: Hostapd no encontrado"
