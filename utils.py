import string
import random
import subprocess
import sys,time

class Utils:
    def pass_generator(self,size=6,chars=string.ascii_lowercase + string.digits):
    	return ''.join(random.choice(chars) for _ in range(size))

    def clock(self,seconds):
        if seconds > 60:
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


    def hostapd(self,command='status'):
        subprocess.check_call(['service','hostapd',command])