from utils import Utils
from rfid import RFID_Controller
import sys

if __name__=="__main__":
	rfid_tag=RFID_Controller()
	#Se crea la variable con toda la configuracion a escribir en hostapd

	#Escribimos el archivo


	print("Press Enter to quit...")

	chr = sys.stdin.read(1)
	print("Cerrando...")

	try:
	    rfid.closePhidget()
	except PhidgetException as e:
	    print("Phidget Exception %i: %s" % (e.code, e.details))
	    print("Exiting....")
	    exit(1)

	print("Listo!.")
	exit(0)
	#tools.clock(60)
	# try:
	# 	tools.hostapd('restart')
		
	# except:
	# 	print "Error: Hostapd no encontrado"
