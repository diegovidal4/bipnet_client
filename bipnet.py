from utils import Utils
from rfid import RFID_Controller
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
import sys,time
from evdev import InputDevice, ecodes
import lcd_kp as lcd



if __name__=="__main__":
	rfid_tag=RFID_Controller()
	current_tag=0
	#Inicializamos clase con herramientas
	tools=Utils()
	#Inicializamos el lcd
	lcd.setup()
  	lcd.lcd_init()
  	lcd.lcd_clean()
	lcd.lcd_string("BIPnet WIFI")
  	#KeyPad a usar
	dev = InputDevice("/dev/input/by-id/usb-05d5_KEYBOARD-event-kbd")
	dev.grab() # mio!
	while(1):
		while(current_tag==rfid_tag.last_tag):
			time.sleep(0.1)
		current_tag=rfid_tag.last_tag
		print "Cambio el tag!:%s" % current_tag

		#Verificar si el tag es valido
		tag_valido=tools.tag_valido(current_tag)
		nombre="Diego"
		#tag_valido=urllib2.urlopen("http://example.com/foo/bar").read()
		if tag_valido: #(string del camilo)
			lcd.lcd_clean()
			lcd.lcd_string("Bienvenido "+nombre)
			time.sleep(3)
			#Obtener la informacion del usuario (nombre,saldo,tipo_usuario)
			#imprimir que debe ingresar la cantidad a utilizar
			lcd.lcd_clean()
			lcd.lcd_string("Ingrese tiempo ")
			lcd.lcd_goto(2,0)
			cantidad=int(lcd.kp_input(dev))
			print "Cantidad:"+cantidad
			#Ingresar el cupon
			lcd.lcd_clean()
			lcd.lcd_string("Tienes Cupon?")
			lcd.lcd_goto(2,0)
			lcd.lcd_string("1. Si, 2. No")
			tiene_cupon=int(lcd.kp_input(dev))
			print "Tiene cupon?:"+tiene_cupon
			if tiene_cupon==1:
				tools.menu_cupon(cantidad)
		else:
			lcd.lcd_clean()
			lcd.lcd_string("Tag Invalido")
			time.sleep(3)
			lcd.lcd_clean()
			lcd.lcd_string("BIPnet WIFI")
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
