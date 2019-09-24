#!/usr/bin/python
import click
from pcapfile import savefile

@click.command()
@click.option("--file", required=True, help="path and file to be read")

def main(file):
    testcap = open(file, 'rb')
    pcap = savefile.load_savefile(testcap, layers=2, verbose=True)

    print(pcap.packets[0].packet.__dict__)
    print(pcap.packets[0].packet.src)
    print(pcap.packets[0].packet.dst)
    exit()

    counter = 0
    for packet in pcap.packets:
        print(type(packet))
        if type(packet) == 'str':
            continue
        print(type(packet))
        if counter > 10:
            exit()
        print(packet.payload)
        counter = counter+1


if __name__ == '__main__':
    main()
