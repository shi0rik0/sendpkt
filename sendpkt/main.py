import argparse
import random
import time

from scapy.all import *


def get_random_id():
    alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)] + [
        chr(i) for i in range(ord("0"), ord("9") + 1)
    ]
    return "".join(random.choices(alphabet, k=6))


def main():
    parser = argparse.ArgumentParser(
        prog="sendpkt",
        description="Send NUM TCP packets with ID to DESTINATION.",
        # epilog="Text at the bottom of help",
    )

    parser.add_argument("destination")
    parser.add_argument("-n", "--num", type=int)
    parser.add_argument("-i", "--id")

    args = parser.parse_args()

    if args.id is None:
        args.id = get_random_id()

    if args.num is None:
        args.num = 2**30

    destination: str = args.destination
    id_: str = args.id
    num: int = args.num

    addr, port = destination.split(":")
    port = int(port)
    ip = IP(dst=addr)
    tcp = TCP(dport=port)
    print(f"Sending to {destination} with id {id_}")
    for i in range(1, num + 1):
        send(ip / tcp / f"{id_} {i} {time.time_ns()}", verbose=0)


if __name__ == "__main__":
    main()
