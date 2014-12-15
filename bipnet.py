from utils import Utils
from rfid import RFID_Controller
import sys

if __name__=="__main__":
	rfid_tag=RFID_Controller()
	#Se crea la variable con toda la configuracion a escribir en hostapd

	#Escribimos el archivo


	print("Press Enter to quit...")

	chr = sys.stdin.read(1)
	#tools.clock(60)
	# try:
	# 	tools.hostapd('restart')
		
	# except:
	# 	print "Error: Hostapd no encontrado"
