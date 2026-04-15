class IPAddress:
    def __init__(self,ip,mask):
        self._ip = ip
        self._mask = mask

    def __str__(self):
        return f'IPAddress {self._ip}/{self._mask}'
    

ip = IPAddress('10.01.01.01','45')
print(ip)