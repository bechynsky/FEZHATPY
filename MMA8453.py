import smbus

# Datashet for MMA8453
# http://cache.freescale.com/files/sensors/doc/data_sheet/MMA8453Q.pdf
class MMA8453:
    # busid - 1 for new Raspberry Pi, 0 for old versions
    # address - I2C address of MMA8453, base is 0x1C
    def __init__(self, busid, address):
        self._bus = smbus.SMBus(busid)
        self._address = address
        # start accelerometer in 10-bit mode
        # see page 37 in chapter 6.7 Control Registers
        self._bus.write_byte_data(self._address, 0x2A, 0x01)

    # returns arry x, y, z
    def read(self):
        rawValues = []
        # read data for x, y, z
        # see page 20 in chapter 6.1 Data Register
        for i in range(1,9):
            rawValues.append(self._bus.read_byte_data(self._address, i))

        return rawValues
        
if __name__ == "__main__":
    acc = MMA8453(1, 0x1C)
    print acc.read()