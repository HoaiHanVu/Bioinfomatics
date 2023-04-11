def FrequentWordWithMismatches(text, k, d):
    neighbors = {}
    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i : i + k]
        if d == 0:
            for i in range(n - k + 1):
                if text[i : i + k] == pattern:
                    if pattern in neighbors:
                        neighbors[pattern] += 1
                    else:
                        neighbors[pattern] = 1
        else:
            neighbors = Neighbors(text, k, d)
    patterns = []
    max_val = max(neighbors.values())
    for key in neighbors:
        if neighbors[key] == max_val:
            patterns.append(key)
    return patterns

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