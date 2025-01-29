import csv
from textwrap import dedent
from re import search

class Utility:

    @staticmethod
    def get_res_lens(result):
        lens = [0] * len(result[0])
        for row in result:
            for i, element in enumerate(row):
                lens[i] = max(lens[i], len(str(element)))
        return lens

    def formatted_print(self, descriptions, result):
        if len(result) == 0:
            print("No such record")
            return False

        desc_lens = [len(str(description)) for description in descriptions]
        res_lens_ = self.get_res_lens(result)

        lens = [max(desc_lens[i], res_lens_[i]) for i in range(len(desc_lens))]
        length = (sum(lens))

        horizontal_border = "+" + "-" * (length + 3 * len(descriptions) - 1) + "+"

        print(horizontal_border)

        for i, description in enumerate(descriptions):
            print(f"| {description:{lens[i]}} ", end="")
        print("| ")

        print(horizontal_border)

        for row in result:
            for i, field in enumerate(row):
                print(f"| {field:{lens[i]}} ", end="")
            print("| ")

        print(horizontal_border)

        return True

    @staticmethod
    def get_descriptions(cursor_description):
        return [description[0] for description in cursor_description]

    pattern = "\d{4}-\d{2}-\d{2}"

    def is_date(self, date_of_creation):
        if len(date_of_creation) == 10 and search(self.pattern, date_of_creation):
            is_leap_year = False
            year = int(date_of_creation.split("-")[0])
            month = int(date_of_creation.split("-")[1])
            day = int(date_of_creation.split("-")[2])

            if year % 400 == 0:
                is_leap_year = True
            elif year % 100 == 0:
                is_leap_year = False
            elif year % 4 == 0:
                is_leap_year = True

            if month == 0 or month > 12 or day == 0 or day > 31:
                return False

            if is_leap_year and month == 2 and day > 29:
                return False

            elif not is_leap_year and month == 2 and day > 28:
                return False

            return True

        return False

    @staticmethod
    def max_res_element_len(result):
        length = 0

        for row in result:
            for element in row:
                length = max(length, len(str(element)))

        return length


    welcome = dedent(
        """
        *****************************
        * Airport Management System *
        *****************************
        """
    )

    prompt = dedent(
        """
        Choose one of the following options by pressing its number:
        1. List all Boeing planes
        2. Add a new plane
        3. Change incorrect \"Boieng\" plane name
        4. List airports in a selected city
        5. Delete a plane
        6. List cities with Boeing planes between specified dates
        7. Quit the program

        Choice: 
        """.rstrip() + " "
    )

    goodbye = dedent(
        """
        ***********
        * Goodbye *
        ***********
        """
    )

    @staticmethod
    def to_csv_decorator(original_function):
        def wrapper(*args, **kwargs):
            descriptions, result, has_records = original_function(*args, **kwargs)

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
