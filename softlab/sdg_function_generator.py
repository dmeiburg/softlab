"""Implements interface for Siglent SDG2000X function generators"""

import pyvisa


class SDGFunctionGenerator():
    """Class with methods to controll Siglent SDG2000X function generators.

    Attributes
    ----------
    device: pyvisa.resources.TCPIPInstrument
    """

    def __init__(self, ip):
        """Establishes connection to device

        Parameters
        ----------
        ip : string
            ip address of the function generator
        """
        rm = pyvisa.ResourceManager()
        self.device = rm.open_resource("TCPIP::{}".format(ip))

    def query(self, scpi):
        """Sends SCPI command to device and returns response.

        Parameters
        ----------
        scpi : string
            SCPI command
        """
        return self.device.query(scpi)

    def idn(self):
        """Gets device identification.
        """
        return self.query("*IDN?")
