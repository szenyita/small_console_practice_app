from utils.max_element_length import max_element_length

def formatted_print(descriptions, result):
    if len(descriptions) == 0 and len(result) == 0:
        print("No such record")
        return

    descriptions_length = max_element_length(descriptions)
    result_length = max_element_length(result)

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
