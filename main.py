import csv
import os


class FileReader:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def read_files(self):
        data_list = []

        # folder_path ichidagi barcha fayllarni olish
        files = [f for f in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f))]

        for file_name in files:
            file_path = os.path.join(self.folder_path, file_name)

            # Faylni oqish
            with open(file_path, 'r') as file:
                lines = file.readlines()

                # Fayl ichidagi ma'lumotlarni olish
                name = lines[0].strip()
                price = lines[1].strip()
                description = lines[2].strip()

                data_list.append({'name': name, 'price': price, 'description': description})

        return data_list

    def write_to_csv(self, csv_file_path, data_list):
        # Ma'lumotlarni CSV fayliga yozish
        with open(csv_file_path, 'w', newline='') as csvfile:
            fieldnames = ['name', 'price', 'description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # CSV faylning ustunlarini yozish
            writer.writeheader()

            # Ma'lumotlarni yozish
            for data in data_list:
                writer.writerow(data)


# FileReader klassini ishlatish
if __name__ == "__main__":
    folder_path = "descriptions"  # Ma'lumotlar uchun papkangizning nomi
    csv_file_path = "output.csv"  # CSV fayli uchun nom

    file_reader = FileReader(folder_path)
    data_list = file_reader.read_files()

    # CSV fayliga yozish
    file_reader.write_to_csv(csv_file_path, data_list)
