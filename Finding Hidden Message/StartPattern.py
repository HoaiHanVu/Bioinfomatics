def StartPattern(text, pattern):
    pos = []
    k = len(pattern)
    for i in range(0, len(text) - k + 1):
        tmp = text[i : i + k]
        if tmp == pattern:
            pos.append(i)
    return pos