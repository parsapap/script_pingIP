import argparse
from pythonping import ping

# import requests
# from asyncping3 import ping

parser = argparse.ArgumentParser(description="A script for getting optimal IPs with best pings",
                                 epilog='created by Team5')
parser.add_argument('-f', '--filename', help="file name with txt extension", required=True)
parser.add_argument('-p', '--ping', type=float, help="optimal ping", required=True)
parser.add_argument('-n', '--name', help='filename for saving result', default='best_ping.txt')
args = parser.parse_args()

with open(args.filename) as f:
    ips = map(lambda ip: ip.strip(), f.readlines())

list_of_ip = [ip for ip in ips]
lst = [i+"\n" for i in list_of_ip if ping(i).rtt_avg_ms <= args.ping]

with open(args.name, 'w') as f:
    f.writelines(lst)
    f.write('\n')
# print(ping('62.102.148.68').rtt_avg_ms)
