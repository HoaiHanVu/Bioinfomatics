def read_txt(filepath, mode):
    with open(filepath, mode) as f:
        contents = f.read()
    return contents