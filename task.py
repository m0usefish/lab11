import csv

try:
    csvfile = open("lab11.csv", "r")

    reader = csv.DictReader(csvfile, delimiter = ",")

    print("Country Name: 2018 [YR2018] - 2019 [YR2019]")

    for row in reader:

        print(row['Country Name'], ': ', row["2018 [YR2018]"],'-', row["2019 [YR2019]"])

    csvfile.close

except:

    print("Файл Lab11.csv не знайдено!")


def search_and_write_to_csv(country_names, output_filename):
    try:
        with open("lab11.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=",")
            rows_to_write = []

            for row in reader:
                if row['Country Name'] in country_names:
                    rows_to_write.append(row)

            if rows_to_write:
                with open(output_filename, 'w', newline='') as output_csv:
                    fieldnames = reader.fieldnames
                    writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
                    writer.writeheader()

                    writer.writerows(rows_to_write)

                print(f"Results for {', '.join(country_names)} written to {output_filename}")
            else:
                print("No matching data found for the specified countries.")

    except FileNotFoundError:
        print("File Lab11.csv not found!")


user_input_countries = input("Enter country names (comma-separated): ").split(',')
output_file_name = "search_results.csv"

search_and_write_to_csv(user_input_countries, output_file_name)