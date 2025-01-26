def get_res_lens(result):
    lens = [0] * len(result[0])
    for row in result:
        for i, element in enumerate(row):
            lens[i] = max(lens[i], len(str(element)))
    return lens