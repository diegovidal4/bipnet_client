import utils

if __name__=="__main__":
	#Se genera un string aleatorio de largo 6 para la password
	password=utils.pass_generator()
	print "La password es:%s" % password
	#Se crea la variable con toda la configuracion a escribir en hostapd
	hostapd_conf="interface=wlan0\nssid=BIPnet\nhw_mode=g\nchannel=6\nauth_algs=1\nwmm_enabled=0\nwpa=2\nwpa_passphrase=%s\nwpa_key_mgmt=WPA-PSK\nwpa_pairwise=TKIP\nrsn_pairwise=CCMP\n" % password
	print hostapd_conf

	#Escribimos el archivo
	with open('/etc/hostapd/hostapd.conf','w') as conf_file:
		conf_file.write(hostapd_conf)

	utils.hostapd()
	utils.clock(120)
