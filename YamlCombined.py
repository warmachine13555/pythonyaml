import csv
import yaml


def dump_data_to_yaml(data_list, yaml_file):
    yaml_data = {"device": {f"csr{i}": data for i, data in enumerate(data_list, 1)}}

    with open(yaml_file, "w") as file:
        yaml.dump(yaml_data, file, sort_keys=False, default_flow_style=False, indent=4)

    print(f"Data written to YAML file '{yaml_file}' successfully.")


def create_data_list_manual():
    switch_suffix = input("Please provide a Switch Suffix: ")
    subnet = input("Please provide a Subnet: ")
    username = input("Please provide a username: ")
    password = input("Please provide a password: ")
    start = input("Please provide the starting point: ")
    switches = int(input("Please provide the number of switches: "))

    subnet_parts = subnet.split(".")

    data_list = []

    for i in range(1, switches + 1):
        current_suffix = f"{switch_suffix}{start}"

        if i > 1:
            subnet_parts[3] = str(int(subnet_parts[3]) + 1)
            subnet = ".".join(subnet_parts)

        data = {
            "switch_suffix": str(current_suffix),
            "ip": str(subnet),
            "username": str(username),
            "password": str(password),
            "port": 22,
            "secret": "admin",
        }

        data_list.append(data)
        start = str(int(start) + 1)

    return data_list


def create_data_list_csv():
    csv_file = "data.csv"
    data_list = []

    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader, 1):
            data = {
                "switch_suffix": row["switch_suffix"],
                "subnet": row["subnet"],
                "username": row["username"],
                "password": row["password"],
                "port": 22,
                "secret": "admin"
            }
            data_list.append(data)

    return data_list




def main():
    choice = input("Enter 1 for manual entry or 2 for CSV import: ")

    if choice == "1":
        data_list = create_data_list_manual()
    elif choice == "2":
        data_list = create_data_list_csv()
    else:
        print("Invalid choice. Please try again.")
        return

    dump_data_to_yaml(data_list, "config.yml")


if __name__ == "__main__":
    main()
