def read_text_k_d(filepath, mode):
    with open(filepath, mode) as file:
        contents = file.read()
    pos = []
    for i in range(len(contents)):
        if contents[i] == "\n":
            pos.append(i)
    text = contents[: pos[0]]
    k = int(contents[pos[0] + 1 : pos[0] + 2])
    d = int(contents[pos[1] - 1: pos[1]])
    return text, k, d