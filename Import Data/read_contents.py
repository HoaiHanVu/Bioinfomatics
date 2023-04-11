def read_contents(filepath, mode, multi = None):
    with open(filepath, mode) as f:
        contents = f.read()
    if multi == None:
        return contents
    else:
        pos = []
        for i in range(len(contents)):
            if contents[i] == "\n":
                pos.append(i)
        pat = contents[:pos[0]]
        text = contents[pos[0] + 1 : pos[1]]
        num = contents[pos[1] + 1 : pos[2]]
        if num.isdigit():
            num = int(num)
        return pat, text, num