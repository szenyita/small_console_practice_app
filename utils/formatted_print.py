from utils.get_res_lens import get_res_lens


def formatted_print(descriptions, result):
    if len(result) == 0:
        print("No such record")
        return False

    desc_lens = [len(str(element)) for element in descriptions]
    res_lens_ = get_res_lens(result)

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
