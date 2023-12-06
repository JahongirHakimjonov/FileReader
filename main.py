import csv
import os


class FileReader:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def read_files(self):
        data_list = []

        files = [f for f in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f))]

        for file_name in files:
            file_path = os.path.join(self.folder_path, file_name)

            with open(file_path, 'r') as file:
                lines = file.readlines()

                name = lines[0].strip()
                price = lines[1].strip()
                description = lines[2].strip()

                data_list.append({'name': name, 'price': price, 'description': description})

        return data_list

    def write_to_csv(self, csv_file_path, data_list):
        with open(csv_file_path, 'w', newline='') as csvfile:
            fieldnames = ['name', 'price', 'description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for data in data_list:
                writer.writerow(data)


if __name__ == "__main__":
    folder_path = "descriptions"
    csv_file_path = "output.csv"

    file_reader = FileReader(folder_path)
    data_list = file_reader.read_files()

    file_reader.write_to_csv(csv_file_path, data_list)
