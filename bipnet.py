from utils import Utils
from rfid import RFID_Controller
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
import sys

if __name__=="__main__":
	rfid_tag=RFID_Controller()
    current_tag=0

    while(current_tag==rfid_tag.last_tag):
    	time.sleep(0.1)

    current_tag=rfid_tag.last_tag
    print "Cambio el tag!:%s" % current_tag 

	#Se crea la variable con toda la configuracion a escribir en hostapd
	#Escribimos el archivo
	print("Press Enter to quit...")

	chr = sys.stdin.read(1)
	print("Cerrando...")

	try:
	    rfid_tag.rfid.closePhidget()
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
