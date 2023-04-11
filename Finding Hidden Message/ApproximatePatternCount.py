def ApproximatePatternCount(pattern, text, d):
    matching = []
    n = len(text)
    k = len(pattern)
    for i in range(n - k + 1):
        count = 0
        tmp = text[i : i + k]
        for j in range(k):
            if tmp[j] != pattern[j]:
                count += 1
                if count > d:
                    break
        if count <= d:
            matching.append(tmp)
    return len(matching)