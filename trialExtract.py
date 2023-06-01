import json

commonPorts = [80, 443]


def ip_extract(json_data):
    ip_addresses = []
    data = json.loads(json_data)

    for ip, ports in data["scan"].items():
        for a in ports:
            ip_addresses.append(f"{ip}:{a['port']}")
    return ip_addresses


json_files = ["192_ip_blocks.json", "172_ip_blocks.json", "10_ip_blocks.json`"]
all_ips = []

for file in json_files:
    with open(file, "r") as f:
        json_data = f.read()

    ips = ip_extract(json_data)

    all_ips.extend(ips)
# print(all_ips)
for i in commonPorts:
    with open("ip_addresses.txt", "w") as extract:
        with open(f"{i}.txt", "w") as output_file:
            for ip in all_ips:
                extract.write(ip + "\n")
                newIps = ip.split(":")
                a, b = newIps
                if int(b) == i:
                    output_file.write(f"{a}:{b}" + "\n")
print("ip addresses saved to ip_address.txt")
