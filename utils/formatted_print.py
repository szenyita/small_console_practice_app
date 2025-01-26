from utils.max_res_element_len import max_res_element_len


def formatted_print(descriptions, result):
    if len(result) == 0:
        print("No such record")
        return False

    descriptions_length = max(len(str(element)) for element in descriptions)
    result_length = max_res_element_len(result)

    length = max(descriptions_length, result_length)
    horizontal_border = "+" + "-" * (length * len(descriptions) + len(descriptions) * 2 + len(descriptions) - 1) + "+"

    print(horizontal_border)

    for description in descriptions:
        print(f"| {description:{length}} ", end="")
    print("| ")

    print(horizontal_border)

    for row in result:
        for field in row:
            print(f"| {field:{length}} ", end="")
        print("| ")

    print(horizontal_border)
