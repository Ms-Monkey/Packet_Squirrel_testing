#!/usr/bin/python
import click
from pcapfile import savefile
from beautifultable import BeautifulTable

@click.command()
@click.option("--file", required=True, help="path and file to be read")

def main(file):
    testcap = open(file, 'rb')
    pcap = savefile.load_savefile(testcap, layers=2, verbose=True)
    print_table(pcap.packets)


def print_table(packets):
    counter = 0
    table = BeautifulTable()
    table.column_headers = ["Source", "Destination"]

    for packet in packets:
        table.append_row([packet.packet.src, packet.packet.dst])
        if counter > 10:
            break
        counter = counter + 1
    print(table)


if __name__ == '__main__':
    main()
