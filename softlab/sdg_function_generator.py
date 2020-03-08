import pyvisa


class SDGFunctionGenerator():
    def __init__(self, ip):
        rm = pyvisa.ResourceManager()
        self.device = rm.open_resource("TCPIP::{}".format(ip))

    def query(self, q):
        return self.device.query(q)

    def idn(self):
        return self.query("*IDN?")
