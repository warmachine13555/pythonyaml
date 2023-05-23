import csv
import yaml

def csv_to_yaml(csv_file, yaml_file):

    data_list = []


    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data = {
                "switch_suffix": row["switch_suffix"],
                "subnet": row["subnet"],
                "username": row["username"],
                "password": row["password"]
            }
            data_list.append(data)


    yaml.add_representer(list, lambda dumper, data: dumper.represent_sequence("tag:yaml.org,2002:seq", data, flow_style=False))
    yaml.add_representer(str, lambda dumper, data: dumper.represent_scalar("tag:yaml.org,2002:str", data, style=""))


    yaml_data = {"device": data_list}


    with open(yaml_file, "w") as file:
        yaml.dump(yaml_data, file, sort_keys=False)

    print(f"Data written to YAML file '{yaml_file}' successfully.")


csv_file = "data.csv"
yaml_file = "config.yml"


csv_to_yaml(csv_file, yaml_file)
