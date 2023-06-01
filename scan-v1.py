import json
import masscan
import pyfiglet
import json

Banner = pyfiglet.figlet_format("block scanner")
print(Banner)


# * Defining block function
def block_scan(ip_range, filename, ports):
    mas = masscan.PortScanner(masscan_search_path=("masscan/bin/masscan",))
    mas.scan(ip_range, ports=ports, arguments="--max-rate 1000000", sudo=True)
    with open(filename, "w") as f:
        f.write(mas.scan_result)


block_scan("10.0.0.0/8", "10_ip_blocks.json", "80,443")
block_scan("172.16.0.0/12", "172_ip_blocks.json", "80,443")
block_scan("192.168.0.0/16", "192_ip_blocks.json", "80,443")
