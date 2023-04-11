def SkewArray(text):
    skew = [0] * (len(text) + 1)
    for i in range(0, len(text)):
        if text[i] == 'G':
            skew[i + 1] = skew[i] + 1
        elif text[i] == 'C':
            skew[i + 1] = skew[i] - 1
        else:
            skew[i + 1] = skew[i]
    return skew