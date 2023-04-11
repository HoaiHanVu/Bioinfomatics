def Neighbors(text, k, d):
    neighbors = {}
    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i : i + k]
        for i in range(len(pattern)):
            for nu in "ACGT":
                if nu != pattern[i]:
                    tmp = pattern[: i] + nu + pattern[i + 1: ]
                    if CheckSmallerGivenDist(pattern, tmp, d):
                        if tmp in neighbors:
                            neighbors[tmp] += 1
                        else:
                            neighbors[tmp] = 1
    return neighbors

def CheckSmallerGivenDist(a, b, d):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
            if count > d:
                return False
    if count <= d:
        return True