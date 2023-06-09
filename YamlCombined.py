import sys
import csv
import yaml


def dump_data_to_yaml(data_list, yaml_file):
    yaml_data = {"device": {data["hostname"]: data for data in data_list}}

    with open(yaml_file, "w") as file:
        yaml.dump(yaml_data, file, sort_keys=False, default_flow_style=False, indent=4)

    print(f"Data written to YAML file '{yaml_file}' successfully.")


def create_data_list_manual():
    hostname = input("Please provide a hostname: ")
    ip = input("Please provide an IP address: ")
    username = input("Please provide a username: ")
    password = input("Please provide a password: ")
    secret = input("Please provide the secret: ")
    start = input("Please provide the starting point: ")
    switches = int(input("Please provide the number of switches: "))

    ip_parts = ip.split(".")

    data_list = []

    for i in range(1, switches + 1):
        current_hostname = f"{hostname}{start}"

        if i > 1:
            ip_parts[3] = str(int(ip_parts[3]) + 1)
            ip = ".".join(ip_parts)

        data = {
            "device_type": "cisco_xe",
            "hostname": str(current_hostname),
            "ip": str(ip),
            "username": str(username),
            "password": str(password),
            "port": 22,
            "secret": str(secret),
        }

        data_list.append(data)
        start = str(int(start) + 1)

    return data_list


def create_data_list_csv(filepath):
    data_list = []

    with open(filepath, "r") as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader, 1):
            data = {
                "device_type": "cisco_xe",
                "hostname": row["hostname"],
                "ip": row["ip"],
                "username": row["username"],
                "password": row["password"],
                "port": 22,
                "secret": row["secret"]
            }
            data_list.append(data)

    return data_list


def main():
    if len(sys.argv) < 2:
        data_list = create_data_list_manual()
    else:
        choice = sys.argv[1]

        if choice == "-i":
            if len(sys.argv) < 3:
                print("No filepath provided. Please try again. Try -i [Filepath.csv]")
                return
            else:
                filepath = sys.argv[2]
                try:
                    with open(filepath, "r"):
                        data_list = create_data_list_csv(filepath)
                except FileNotFoundError:
                    print(f"File not found: {filepath}")
                    return
        else:
            print("Invalid choice. Please try again. Try -i [Filepath.csv]")
            return

    output_file = "connection.yml"

    if len(sys.argv) > 3 and sys.argv[3] == "-o":
        if len(sys.argv) > 4:
            output_file = sys.argv[4]

    dump_data_to_yaml(data_list, output_file)


if __name__ == "__main__":
    main()
