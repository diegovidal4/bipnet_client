import string
import random
import subprocess
import sys,time
import urllib2,json

class Utils:
    def pass_generator(self,size=6,chars=string.ascii_lowercase + string.digits):
    	return ''.join(random.choice(chars) for _ in range(size))

    def clock(self,seconds):
        minutes=seconds/60
        for remaining_min in range(minutes,0,-1):
            for remaining_seg in range(60, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("{:2d} minutes and {:2d} seconds remaining.".format(remaining_min,remaining_seg)) 
                sys.stdout.flush()
                time.sleep(1)
        sys.stdout.write("\r")
        sys.stdout.flush()    
        sys.stdout.write("\rComplete!\n")

    #Configura hostapd y retorna las password generada
    def set_hostapd_conf(self):
        password=self.pass_generator(8)
        hostapd_conf="interface=wlan0\nssid=BIPnet\nhw_mode=g\nchannel=6\nauth_algs=1\nwmm_enabled=0\nwpa=2\nwpa_passphrase=%s\nwpa_key_mgmt=WPA-PSK\nwpa_pairwise=TKIP\nrsn_pairwise=CCMP\n" % password
        with open('/etc/hostapd/hostapd.conf','w') as conf_file:
            conf_file.write(hostapd_conf)
        return password

    def hostapd(self,command='status'):
        p=subprocess.Popen(["sh","rebootAp.sh",command])
        out, err = p.communicate()
        return out

    def verificar_cupon(self,cupon):
        response = urllib2.urlopen("https://amber-heat-2069.firebaseapp.com/api/verify/cupon/"+cupon)
        data = json.loads(response.read())
        print data
        return (True,30)

    def tag_valido(self,current_tag):
        tag_valido=urllib2.urlopen("http://csz-embebidosproj.nodejitsu.com/api/verify/user/tag?cardId="+current_tag)
        data = json.loads(tag_valido.read())
        if data['message']=="usuario valido":
            return data
        else:
            return False

if __name__=="__main__":
    tools=Utils()
    data=tools.tag_valido("4d004a9d26")
    if data:
        print "buena"
        print data
    else:
        print "nedde"
    # print "Password:"+tools.set_hostapd_conf()
    # print "Cerrando hostapd"
    # print tools.hostapd("stop")
    # print "Iniciando hostapd"
    # print tools.hostapd("start")
