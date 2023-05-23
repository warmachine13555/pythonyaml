import yaml

switch_suffix = input("Please provide a Switch Suffix: ")
subnet = input("Please provide a Subnet: ")
username = input("Please provide a username: ")
password = input("Please provide a password: ")
start = input("Please provide the starting point: ")
switches = int(input("Please provide the number of switches: "))
config = "config.yml"

data_list = []

subnet_parts = subnet.split(".")

data = {
    "device": {}
}

for i in range(1, switches + 1):
    current_suffix = f"{switch_suffix}{start}"

    if i > 1:
        subnet_parts[3] = str(int(subnet_parts[3]) + 1)
        subnet = ".".join(subnet_parts)

    data["device"][f"csr{i}"] = {
        "switch_suffix": str(current_suffix),
        "ip": str(subnet),
        "username": str(username),
        "password": str(password),
        "port": 22,
        "secret": "admin",
    }

    start = str(int(start) + 1)

data_list.append(data)

yaml.Dumper.ignore_aliases = lambda *args: True
yaml.SafeDumper.add_representer(
    dict, yaml.SafeDumper.represent_dict
)

with open("config.yml", "w") as f:
    yaml.dump(data_list, f, sort_keys=False, indent=4, default_flow_style=False)

print("Data written to YAML file successfully.")
