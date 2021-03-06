from utils import Utils
from rfid import RFID_Controller
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
from Phidgets.Devices.RFID import RFID, RFIDTagProtocol
import sys,time
from evdev import InputDevice, ecodes
import lcd_kp as lcd



if __name__=="__main__":
	precio_min=10

	#Inicializamos el RFID
	rfid_tag=RFID_Controller()
	rfid_tag.displayDeviceInfo()
	print("Turning on the RFID antenna....")
	rfid_tag.rfid.setAntennaOn(True)
	try:
	   rfid_tag.rfid.write("Some Tag", RFIDTagProtocol.PHIDGET_RFID_PROTOCOL_PHIDGETS)
	except PhidgetException as e:
		print("Phidget Exception %i: %s" % (e.code, e.details))
	current_tag=0
	#Inicializamos clase con herramientas
	tools=Utils()
	#Inicializamos el lcd
	lcd.setup()
  	lcd.lcd_init()
  	lcd.lcd_clean()
	lcd.lcd_string("BIPnet WIFI")
	dev = InputDevice("/dev/input/by-id/usb-05d5_KEYBOARD-event-kbd")
	#KeyPad a usar
	dev.grab()
	while(1):
		dev = InputDevice("/dev/input/by-id/usb-05d5_KEYBOARD-event-kbd")
		#KeyPad a usar
		dev.grab()
		#Loop para no dejar que otro tag interfiera
		while(current_tag==rfid_tag.last_tag):
			time.sleep(0.1)
		current_tag=rfid_tag.last_tag
		print "Cambio el tag!:%s" % current_tag
		#Verificar si el tag es valido
		data=tools.tag_valido(current_tag)
		print data
		if data: #(string del camilo)
			nombre=data['username']
			lcd.lcd_clean()
			lcd.lcd_string("Bienvenido "+nombre)
			lcd.lcd_goto(2,0)
			lcd.lcd_string("Saldo:"+str(data["balance"]))
			time.sleep(3)
			#Obtener la informacion del usuario (nombre,saldo,tipo_usuario)
			#imprimir que debe ingresar la cantidad a utilizar
			lcd.lcd_clean()
			lcd.lcd_string("Ingrese tiempo ")
			lcd.lcd_goto(2,0)
			cantidad=int(lcd.kp_input(dev))
			print "Cantidad:%i" % cantidad

			#Ciclo saldo invalido
			if data["typeUser"]!="Admin":
				while cantidad*precio_min > data["balance"]:
					lcd.lcd_clean()
					lcd.lcd_string("Tiempo excede saldo")
					lcd.lcd_goto(2,0)
					lcd.lcd_string("Ingreselo nuevamente")
					time.sleep(3)
					lcd.lcd_clean()
					lcd.lcd_string("Ingrese tiempo ")
					lcd.lcd_goto(2,0)
					cantidad=int(lcd.kp_input(dev))

				lcd.lcd_clean()
				lcd.lcd_string("Precio:"+str(cantidad*precio_min))
				lcd.lcd_goto(2,0)
				lcd.lcd_string("1. Si, 2. No :")
				acepto=''
			else:
				acepto=1
			#loop para esperar el evento de boton
			while acepto=='':
				time.sleep(0.1)
				acepto=lcd.kp_input(dev)
			print "acepto?:%i" % int(acepto)
			if int(acepto)!=1:
				lcd.lcd_string("Gracias")
				time.sleep(3)
				current_tag=0
			else:
				tools.restar_monto(data,cantidad*precio_min)
				lcd.lcd_clean()
				lcd.lcd_string("Creando red wifi...")
				tools.hostapd("stop")
				password=tools.set_hostapd_conf()
				print "Password:"+password
				tools.hostapd("start")
				lcd.lcd_clean()
				lcd.lcd_string("Red:BIPnet")
				lcd.lcd_goto(2,0)
				lcd.lcd_string("Pass:"+password)
				time.sleep(15)
				lcd.lcd_clean()
				lcd.lcd_string("Gracias")
				tools.clock(60*cantidad)
				current_tag=0
				rfid_tag.last_tag=0
			#Ingresar el cupon
			# lcd.lcd_clean()
			# lcd.lcd_string("Tienes Cupon?")
			# lcd.lcd_goto(2,0)
			# lcd.lcd_string("1. Si, 2. No :")
			# tiene_cupon=''
			# #loop para esperar el evento de boton
			# while tiene_cupon=='':
			# 	time.sleep(0.1)
			# 	tiene_cupon=lcd.kp_input(dev)
			# print "Tiene cupon?:%i" % int(tiene_cupon)
			# if int(tiene_cupon)==1:
			# 	precio_total=cantidad*precio_min
			# else:
		elif data and int(data["balance"])==0:
			lcd.lcd_clean()
			lcd.lcd_string("Tag sin saldo")
			lcd.lcd_goto(2,0)
			lcd.lcd_string("Recargar")
			time.sleep(3)
			lcd.lcd_clean()
			lcd.lcd_string("BIPnet WIFI")
			current_tag=0
			rfid_tag.last_tag=0
		else:
			lcd.lcd_clean()
			lcd.lcd_string("Tag Invalido")
			time.sleep(3)
			lcd.lcd_clean()
			lcd.lcd_string("BIPnet WIFI")
			current_tag=0
			rfid_tag.last_tag=0
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
