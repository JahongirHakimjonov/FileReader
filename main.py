import csv
import os


class FileReader:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def read_files(self):
        data = []
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(self.folder_path, filename)
                with open(file_path, "r", encoding="utf-8") as file:
                    lines = file.readlines()
                    if len(lines) >= 3:
                        name = lines[0].strip()
                        price = lines[1].strip()
                        description = lines[2].strip()
                        data.append({"name": name, "price": price, "description": description})
        return data

    def write_to_csv(self, output_file="output.csv"):
        data = self.read_files()
        if data:
            with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
                fieldnames = ["name", "price", "description"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter="|")
                writer.writeheader()
                for row in data:
                    writer.writerow(row)
            print(f"Data has been written to {output_file} successfully.")
        else:
            print("No data to write.")


# FileReader class'ini instansiyalash
folder_path = "descriptions"
file_reader = FileReader(folder_path)

# Ma'lumotlarni o'qish va CSV ga yozish
file_reader.write_to_csv()
