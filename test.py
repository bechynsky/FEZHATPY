import ADS7830

ads = ADS7830.ADS7830(1, 0x48)

for i in range(0,8):
    print "{0}: {1}".format(i, ads.Read(i))
