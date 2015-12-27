import ADS7830
import RPi.GPIO as GPIO
 
class FEZHAT:
    AIN1 = 1
    AIN2 = 2
    AIN3 = 3
    AIN6 = 6
    AIN7 = 7
    
    GIO26 = 26
    GIO16 = 16
    
    SW_DIO18 = 18
    SW_DIO22 = 22
    
    LED = 24
    
    def __init__(self):
        self._ads = ADS7830.ADS7830(1, 0x48)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.LED, GPIO.OUT)
        
    def get_light(self):
        return self._ads.read(5) / 255.0
    
    # http://ww1.microchip.com/downloads/en/DeviceDoc/20001942F.pdf
    def get_temperature(self):
        # see page 8
        return (((3300 / 255) * self._ads.read(4)) - 400) / 19.5

    def read_analog(self, channel):
        return self._ads.read(channel)
        
    def led_on(self):
        GPIO.output(self.LED, GPIO.HIGH)

    def led_off(self):
        GPIO.output(self.LED, GPIO.LOW)

if __name__ == "__main__":
    fh = FEZHAT()
    print fh.get_light()
    print fh.get_temperature()
    print fh.read_analog(FEZHAT.AIN1)
    fh.led_on()
