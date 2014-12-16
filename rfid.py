from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
from Phidgets.Events.Events import AttachEventArgs, DetachEventArgs, ErrorEventArgs, OutputChangeEventArgs, TagEventArgs
from Phidgets.Devices.RFID import RFID, RFIDTagProtocol
from utils import Utils


class RFID_Controller:

	def __init__(self):
		self.last_tag=0
		try:
			self.rfid = RFID()
			self.rfid.setOnAttachHandler(self.rfidAttached)
			self.rfid.setOnDetachHandler(self.rfidDetached)
			self.rfid.setOnErrorhandler(self.rfidError)
			self.rfid.setOnOutputChangeHandler(self.rfidOutputChanged)
			self.rfid.setOnTagHandler(self.rfidTagGained)
			self.rfid.setOnTagLostHandler(self.rfidTagLost)
			self.rfid.openPhidget()
		except RuntimeError as e:
			print("Runtime Exception: %s" % e.details)
			print("Exiting....")
			exit(1)
		try:
			print("Turning on the RFID antenna...")
			self.rfid.setAntennaOn(True)
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
		self.last_tag=e.tag
		self.rfid.setLEDOn(1)

	def rfidTagLost(self,e):
		source = e.device
		self.rfid.setLEDOn(0)
		#print("RFID %i: Tag Lost: %s" % (source.getSerialNum(), e.tag))
	def end_program(self):
		try:
			self.rfid.closePhidget()
		except PhidgetException as e:
			print("Phidget Exception %i: %s" % (e.code, e.details))
			print("Exiting....")
			exit(1)
		print("Done.")
		exit(0)