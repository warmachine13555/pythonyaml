import csv

csv_file = "data.csv"

headers = ["hostname", "ip", "username", "password", "secret"]

data = [
    ["sw-1", "10.0.0.1", "admin", "admin", "secret"],
    ["sw-2", "10.0.0.6", "admin", "admin", "secret"],
]

with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)

print(f"Test CSV file '{csv_file}' generated successfully.")
