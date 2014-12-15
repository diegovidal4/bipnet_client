from utils import Utils
from rfid import RFID_Controller
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
import sys,time



if __name__=="__main__":
	while(1):
		rfid_tag=RFID_Controller()
		current_tag=0
		while(current_tag==rfid_tag.last_tag):
			time.sleep(0.1)

		current_tag=rfid_tag.last_tag
		print "Cambio el tag!:%s" % current_tag 

		#Verificar si el tag es valido
		#tag_valido=urllib2.urlopen("http://example.com/foo/bar").read()
		if tag_valido: #(string del camilo)
			
		else:

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
