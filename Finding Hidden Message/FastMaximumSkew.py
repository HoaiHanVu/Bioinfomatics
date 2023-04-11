def FastMaximumSkew(text):
    array = SkewArray(text)
    max_val = max(array)
    num_max = array.count(max_val)
    stop = 0
    position = []
    for i in range(len(array)):
        if array[i] == max_val:
            position.append(i)
            stop += 1
            if stop == num_max:
                break
    return position

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