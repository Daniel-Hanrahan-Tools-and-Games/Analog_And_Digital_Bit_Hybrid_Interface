from spidev import SpiDev

class MCP3008:
    # sets up the MCP3008 ADC
    def __init__(self, bus = 0, device = 0):
        self.bus, self.device = bus, device
        self.spi = SpiDev()
        self.open()
        self.spi.max_speed_hz = 1000000
    
    # opens MCP3008 ADC
    def open(self):
        self.spi.open(self.bus, self.device)
        self.spi.max_speed_hz = 1000000
    
    # reads from channel 0
    def read0(self, channel = 0):
        adc = self.spi.xfer2([1, (8 + channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data
    
    # reads from channel 1
    def read1(self, channel = 1):
        adc = self.spi.xfer2([1, (8 + channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data
    
    # reads from channel 2
    def read2(self, channel = 2):
        adc = self.spi.xfer2([1, (8 + channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data
    
    # closes ADC
    def close(self):
        self.spi.close()