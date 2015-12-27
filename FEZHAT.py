import ADS7830

class FEZHAT:
    
    def __init__(self):
        self._ads = ADS7830.ADS7830(1, 0x48)
        
    def get_light():
        return self._ads.read(5) / 255.0
    
    # http://ww1.microchip.com/downloads/en/DeviceDoc/20001942F.pdf
    def get_temperature():
        # see page 8
        return (((3.3 / 255) * self._ads.read(4)) - 400) / 19.5


if __name__ == "__main__":
    fh = FEZHAT()
    print fh.get_light()
    print fh.get_temperature()