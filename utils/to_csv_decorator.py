import csv


def to_csv_decorator(original_function):
    def wrapper():
        descriptions, result, has_records = original_function()

        if not has_records:
            return

        choice = ""

        while choice not in {"Y", "N"}:
            choice = input("Would you like to export the data to a csv file? (Y/N):").upper()

        if choice == "Y":
            try:
                with open("output.csv", "w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(descriptions)
                    for row in result:
                        writer.writerow(row)
                    print("File output.csv written successfully")

            except Exception as e:
                print("File writing failed")
                print(f"Exception {e}")

    return wrapper
