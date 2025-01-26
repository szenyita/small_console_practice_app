def max_res_element_len(result):
    length = 0
    for row in result:
        for element in row:
            length = max(length, len(str(element)))
    return length