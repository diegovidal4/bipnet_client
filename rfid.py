from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
from Phidgets.Events.Events import AttachEventArgs, DetachEventArgs, ErrorEventArgs, OutputChangeEventArgs, TagEventArgs
from Phidgets.Devices.RFID import RFID, RFIDTagProtocol
from utils import Utils
import urllib2


class RFID_Controller:

	def __init__(self):
		try:
			self.rfid = RFID()
			self.rfid.openPhidget()
			self.rfid.setOnAttachHandler(self.rfidAttached)
			#self.rfid.setOnDetachHandler(self.rfidDetached)
			self.rfid.setOnErrorhandler(self.rfidError)
			#self.rfid.setOnOutputChangeHandler(self.rfidOutputChanged)
			self.rfid.setOnTagHandler(self.rfidTagGained)
			#self.rfid.setOnTagLostHandler(self.rfidTagLost)
		except RuntimeError as e:
			print("Runtime Exception: %s" % e.details)
			print("Exiting....")
			exit(1)
		except PhidgetException as e:
			print("Phidget Exception %i: %s" % (e.code, e.details))
			exit(1)

	def rfidAttached(self,e):
		attached = e.device
		print("RFID %i Attached!" % (attached.getSerialNum()))

	def rfidDetached(self,e):
		detached = e.device
		print("RFID %i Detached!" % (detached.getSerialNum()))

	def rfidError(self,e):
		try:
			source = e.device
			print("RFID %i: Phidget Error %i: %s" % (source.getSerialNum(), e.eCode, e.description))
		except PhidgetException as e:
			print("Phidget Exception %i: %s" % (e.code, e.details))

	def rfidOutputChanged(self,e):
		source = e.device
		print("RFID %i: Output %i State: %s" % (source.getSerialNum(), e.index, e.state))

	def rfidTagGained(self,e):
		tools=Utils()
		source = e.device
		self.rfid.setLEDOn(1)
		print("Tag leido:"+e.tag)
		#Verificar si el tag es valido
		#tag_valido=urllib2.urlopen("http://example.com/foo/bar").read()
		#Se llama a la configuracion de hostapd
		password=tools.set_hostapd_conf()
		print "Password generada:%s" % password
		#print("RFID %i: Tag Read: %s" % (source.getSerialNum(), e.tag))

	def rfidTagLost(self,e):
		source = e.device
		self.rfid.setLEDOn(0)
		#print("RFID %i: Tag Lost: %s" % (source.getSerialNum(), e.tag))