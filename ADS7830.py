import smbus

# http://www.ti.com/lit/ds/symlink/ads7830.pdf
class ADS7830:
    def __init__(self, busid, address):
        self.bus = smbus.SMBus(busid)
        self.address = address

    def Read(self, channel):
        channelAddress = 0b10000100 | ((channel / 2) if (channel % 2 == 0) else ((channel / 2) + 4)) << 4
	self.bus.write_byte(self.address, channelAddress)
        adcValue = self.bus.read_byte(self.address)
        return adcValue


if __name__ == "__main__":
    ads = ADS7830(1, 0x48)
    for i in range(0,8):
        print "Channel {0}: {1}".format(i, ads.Read(i))
