import csv
import json


def save_to_json(file_path, data):
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


def load_json(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        return data


def convert_to_csv(data: [], path):
    if not data:
        print("No objects provided. CSV file not created.")
        return

    # Extract fieldnames from the keys of the first object (assuming all objects have identical keys)
    fieldnames = list(data[0].keys())

    with open(path, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write each object as a row in the CSV
        for obj in data:
            writer.writerow(obj)

    print(f"CSV file '{path}' has been created successfully.")
